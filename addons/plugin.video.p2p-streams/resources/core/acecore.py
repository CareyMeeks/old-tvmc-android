# -*- coding: utf-8 -*-

""" p2p-streams  (c)  2014 enen92 fightnight

    This file contains the acestream console of the addon. Initial versions were coded by Nouismons and so, this file is based on his work.
    
    Classes:
    
    Logger() -> Log class
    _TSPlayer(xbmc.Player) -> Inheritance of the xbmc.Player class for acestreams
    TSengine() -> Acestreamengine class, start functions, etc
    TSServ(threading.Thread) ->  Acestreamengine service class
    OverlayText(object) -> Overlaytext displayed on player
        

"""

import httplib,urllib,urllib2,re,sys,subprocess,os,socket,threading,time,random,json,xbmcplugin,xbmcgui,xbmc,xbmcaddon,xbmcvfs
from utils.pluginxbmc import *

""" Fixed variables """

aceport=int(settings.getSetting('aceporta'))
server_ip=settings.getSetting('ip_addr')
if settings.getSetting('save')=='true': save=False
else: save=False
if settings.getSetting('ace-debug')=='true': alog=True
else: alog=False
if (sys.platform == 'win32') or (sys.platform == 'win64'): pwin=True
else: pwin=False


""" Function and class list """


def show_Msg(heading, message, times = 3000, pics = addon_icon):
    try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading.encode('utf-8'), message.encode('utf-8'), times, pics.encode('utf-8')))
    except Exception, e:
        print( '[%s]: ShowMessage: Transcoding UTF-8 failed [%s]' % (addon_id, e), 2 )
        try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
        except Exception, e:
            print( '[%s]: ShowMessage: exec failed [%s]' % (addon_id, e), 3 )

class Logger():
    def __init__(self,Name):
        self.started=False
        self.name=Name
        self.link=None
    def out(self,txt):
        if alog:
            print "%s:%s"%(self.name,txt)


class _TSPlayer(xbmc.Player):

    def __init__( self):
        self.started=False
        self.log=Logger("TSPlayer")
        self.log.out('init')
        self.active=True
        self.link=None
        self.vod=True
        self.duration=None
        self.coms=[]
    def onPlayBackPaused( self ):
        self.log.out('paused')
        
    def onPlayBackStarted( self ):
        xbmc.executebuiltin('XBMC.ActivateWindow("fullscreenvideo")')
        self.started=True
        self.log.out('started')
        if self.vod:
            try: 
                self.duration= int(xbmc.Player().getTotalTime()*1000)
                comm='DUR '+self.link.replace('\r','').replace('\n','')+' '+str(self.duration)
                self.coms.append(comm)
            except: pass
        
        comm='PLAYBACK '+self.link.replace('\r','').replace('\n','')+' 0'
        self.coms.append(comm)
        xbmc.sleep(2500)

    def onPlayBackResumed(self):
        self.log.out("play resume")
        
    def onPlayBackEnded(self):
        self.log.out("play ended")
        self.active=False
        comm='PLAYBACK '+self.link.replace('\r','').replace('\n','')+' 100'
        self.coms.append(comm)
        
    def onPlayBackStopped(self):
        self.log.out("play stop")
        self.active=False
        if settings.getSetting('engine-status') == "true": 
                try:lat123._close()
                except:pass

    def __del__(self):
        self.log.out('delete')
    


class TSengine():

    def __init__(self):
        xbmc.Player().stop()
        self.log=Logger("TSEngine")
        self.push=Logger('OUT')
        self.alive=True
        self.progress = xbmcgui.DialogProgress()
        self.player=None
        self.files={}
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.settimeout(3)
        self.progress.create(translate(40000),translate(40052))
        self.tsserv =None
        self.conn=False
        self.title=None
        self.filename=None
        self.mode=None
        self.url=None
        self.local=False
        self.saved=False
        self.pos=[25,50,75,100]
        l=False
        while xbmc.Player().isPlaying(): 
            l=True
            if xbmc.abortRequested:
                self.log.out("XBMC asked to abort request")
                return False
            if self.progress.iscanceled():
                return False
            xbmc.sleep(300)
        
        settings.setSetting('active','1')
        if l: xbmc.sleep(500)

    def ts_init(self):
        self.tsserv = TSServ(self._sock)
        self.tsserv.start()
        comm="HELLOBG"
        self.TSpush(comm)
        self.progress.update(0,translate(1104)," ")
        while not self.tsserv.version:
            if xbmc.abortRequested:
                self.log.out("XBMC asked to abort request")
                return False
            if self.progress.iscanceled():
                return False
            time.sleep(1)
        ready='READY'
        if self.tsserv.key:
            import hashlib
            sha1 = hashlib.sha1()
            pkey=self.tsserv.pkey
            sha1.update(self.tsserv.key+pkey)
            key=sha1.hexdigest()
            pk=pkey.split('-')[0]
            key="%s-%s"%(pk,key)
            ready='READY key=%s'% key
        if self.progress.iscanceled():
            self.err=1
            return False        
        self.TSpush(ready)
        return True
    
    def sm(self,msg):
        show_Msg('AceStream',msg)
    
    def connect(self):
        server_ip='127.0.0.1'
        servip=settings.getSetting('ip_addr')
        aceport=int(settings.getSetting('aceporta'))
        self.log.out('Trying to connect')
        self.progress.update(0,translate(1001),' ')
        if pwin:
            res=self.startWin()
            aceport=self.getWinPort()
            if not aceport: 
                res=self.startWin()
                if not res: return False
        elif xbmc.getCondVisibility('System.Platform.OSX'):
            self.log.out("Trying to connect OSX engine")
            res=self.startosx()
        else:
            self.log.out('try to connect to Linux engine')
            self.log.out('Connecting to %s:%s'%(servip,aceport))
            try:
                self._sock.connect((servip, aceport))
                self.log.out('Connected to %s:%s'%(servip,aceport))
                return True
            except:
                res=self.startLin()
                if not res: return False
        i=30
        while (i>1):
            self.progress.update(0,translate(40046),translate(40049) + str('%s'%i) + ' ' + translate(40050) )
            try:
                if pwin: aceport=self.getWinPort()
                self._sock.connect((servip, aceport))
                self.log.out('Connected to %s:%s'%(servip,aceport))     
                i=0
                return True
            except:
                self.log.out('Failed to connect to %s:%s'%(servip,aceport))   
            if self.progress.iscanceled():
                return False
                break
            i=i-1
            xbmc.sleep(1000)
            if xbmc.getCondVisibility('system.platform.OSX'):
                self._sock.close()
                self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sm('Cant connect')
        return False
            

    def startosx(self):
        self.log.out('try to start OSX engine')
        import subprocess
        enviro = {'VERSIONER_PYTHON_PREFER_32_BIT': 'no', 'TERM_PROGRAM_VERSION': '326','PATH': '/opt/local/bin:/opt/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin', 'TERM_PROGRAM': 'Apple_Terminal', 'LANG': 'en_GB.UTF-8', 'TERM': 'xterm-256color', 'Apple_PubSub_Socket_Render': '/tmp/launch-clnRhS/Render', 'VERSIONER_PYTHON_VERSION': '2.7', 'SHLVL': '2', 'SECURITYSESSIONID': '186a4', 'TMPDIR': '/var/folders/gg/4_z3kg_j4lb5zqlqntr_wbv00000gn/T/', 'TERM_SESSION_ID': 'DE9554D2-3F7B-4D47-B90A-BABAAC003473', 'SSH_AUTH_SOCK': '/tmp/launch-CepH8L/Listeners', 'SHELL': '/bin/bash', '_': '/usr/bin/python', '__CF_USER_TEXT_ENCODING': '0x1F5:0:0','__CHECKFIX1436934': '1'}
        try:
            self.proc = subprocess.Popen(['python',xbmc.translatePath(os.path.join(pastaperfil,'acestream','ace','start.py'))],shell=False,env=enviro)
        except:
            self.sm('Not Installed')
            self.log.out('Not Installed')
            self.progress.update(0,'AceStream not installed','')
            return False       
        self.log.out('Engine starting')
        return True


    def startLin(self):
        self.log.out('try to start Lin engine')
        import subprocess
        if xbmc.getCondVisibility('System.Platform.Android') or settings.getSetting('force_android') == "true":
            try:
                xbmc.executebuiltin('XBMC.StartAndroidActivity("org.acestream.engine")')
            except:
                self.sm("Not installed")
                self.log.out("Not installed")
                self.progress.update(0,"Acestreamengine.apk not installed","")
        else:
            print "Linux not android.."
            if os.uname()[4] == "armv6l" or os.uname()[4] == "armv7l":
                try:
                    self.proc = subprocess.Popen([settings.getSetting('python_cmd'),os.path.join(pastaperfil,'acestream','ace','start.py')])
                except:
                    self.sm("Not installed")
                    self.log.out("Not installed")
                    self.progress.update(0,"Acestream engine not installed")

            elif settings.getSetting('openeleci386') == "true":
                try:
                    command = ["sh",os.path.join(pastaperfil,'acestream','start.sh')]
                    if settings.getSetting('total_max_download_rate') != "0":
                        command.append('--download-limit')
                        command.append(settings.getSetting('total_max_download_rate'))
                    if settings.getSetting('total_max_upload_rate') != "0":
                        command.append('--upload-limit')
                        command.append(settings.getSetting('total_max_upload_rate'))
                    self.proc = subprocess.Popen(command)
                except:
                    self.sm("Not installed")
                    self.log.out("Not installed")
                    self.progress.update(0,"Acestream engine not installed")
            else:
                print("Not armv7 or armv6")
                if settings.getSetting('ace_cmd') == "0":
                    acefolder = os.path.join(pastaperfil,'acestream')
                    acebin = os.path.join(pastaperfil,'acestream','acestreamengine')
                    command = [acebin,'--client-console','--lib-path',acefolder]
                    if settings.getSetting('total_max_download_rate') != "0":
                        command.append('--download-limit')
                        command.append(settings.getSetting('total_max_download_rate'))
                    if settings.getSetting('total_max_upload_rate') != "0":
                        command.append('--upload-limit')
                        command.append(settings.getSetting('total_max_upload_rate'))
                    print command
                elif settings.getSetting('ace_cmd') == "1": command = ["acestreamengine","--client-console"]
                elif settings.getSetting('ace_cmd') == "2": command = settings.getSetting('ace_cmd_alternative').split(' ')
                try:
                    self.proc = subprocess.Popen(command)
                except:
                    self.sm('Not Installed')
                    self.log.out('Not Installed')
                    self.progress.update(0,'AceStream not installed','')
                    return False
        self.log.out('Engine starting')
        return True
                    
    def startWin(self):
        try:
            needed_value='ace_engine.exe'
            path_value=os.path.join(pastaperfil,'acestream',needed_value)
            self.log.out("Try to start %s"%needed_value)
            self.progress.update(0,'Starting ASEngine','')
            os.startfile(path_value)
            self.log.out('AceStream Engine starting')
        except:
            self.sm('Not Installed')
            self.log.out('Not Installed')
            self.progress.update(0,'AceStream not installed','')
            return False
        return True

    def getWinPort(self):
        try:
            path=os.path.join(pastaperfil,'acestream')
            pfile= os.path.join( path,'acestream.port')
            gf = open(pfile, 'r')
            aceport=int(gf.read())
        except: 
            return False
        self.log.out('get aceport - %s'%aceport)
        return aceport
      
    def TSpush(self,command):
        self.push.out(command)
        try:
            self._sock.send(command+'\r\n')
        except: 
            self.push.out("!!!Error!!!")
    
    def get_link(self, index=0, title='', icon='', thumb=''):     
        self.title=title
        self.log.out("play")
        self.tsserv.ind=index
        self.progress.update(89,translate(1005),'')
        for k,v in self.files.iteritems():
            if v==index: self.filename=urllib.unquote(k).replace('/','_').replace('\\','_')
        try:    
            avail=os.path.exists(self.filename.decode('utf-8'))
        except:
            try:
                avail=os.path.exists(self.filename)
                self.filename=self.filename.encode('utf-8')
            except: self.filename='temp.avi'
        self.log.out('Starting file:%s'%self.filename)
        
        try: self.filename=settings.getSetting('folder')+self.filename
        except: 
            self.filename=None
            save=False
        
        self.log.out('Get filename to save:%s'%self.filename)
        spons=''
        if self.mode!='PID': spons=' 0 0 0'
        comm='START '+self.mode+ ' ' + self.url + ' '+ str(index) + spons
        self.TSpush(comm)
        self.progress.update(89,translate(1004),'')
        while not self.tsserv.got_url and not self.progress.iscanceled() and not self.tsserv.err:
            self.progress.update(int(self.tsserv.proc),self.tsserv.label,self.tsserv.line)
            xbmc.sleep(200)
            if xbmc.abortRequested:
                self.log.out("XBMC is shutting down")
                break
        if self.tsserv.err: self.sm('Failed to load file')
        self.progress.update(100,translate(1005),'')
        if settings.getSetting('save')=='true': save=True
        else: save=False

        if self.tsserv.event and save:
            self.progress.update(0,translate(400006)," ")
            comm='SAVE %s path=%s'%(self.tsserv.event[0]+' '+self.tsserv.event[1],urllib.quote(self.filename))
            self.TSpush(comm)
            self.tsserv.event=None
            succ=True

            while not os.path.exists(self.filename.decode('utf-8')) and not self.progress.iscanceled():
                if xbmc.abortRequested or self.progress.iscanceled():
                    self.log.out("XBMC asked to abort request")
                    succ=False
                    break
                xbmc.sleep(200)
            if not succ: return False
            self.tsserv.got_url=self.filename.decode('utf-8')
            self.local=True
            
        self.active=True
        self.progress.close()
        return self.tsserv.got_url
    
    def play_url_ind(self, index=0, title='', icon='', thumb=''):
        self.lnk=self.get_link(index,title,icon,thumb)
        if not self.lnk: return False
        if settings.getSetting('aceplay_type') == str(1):
                if ":6878/" in self.lnk: self.lnk = self.lnk.replace(":6878",":" + settings.getSetting('playerport'))
        if self.progress:self.progress.close()
        item = xbmcgui.ListItem(title,iconImage="DefaultVideo.png", thumbnailImage=thumb)
        item.setPath(path=self.lnk)
        if settings.getSetting('engine-status') == "true":
                global lat123 
                lat123 = OverlayText()
        xbmcplugin.setResolvedUrl(int(sys.argv[1]),True,item)
        xbmc.sleep(100)
        self.player=_TSPlayer()
        self.player.vod=True
        self.player.link=self.tsserv.got_url
        self.log.out('play')
        self.player.link=self.lnk
        if self.progress:self.progress.close()
        if self.local: 
            if int(sys.argv[1]) < 0:
                xbmc.Player().play(self.lnk,item)
        else:
            xbmc.sleep(50)
            if int(sys.argv[1]) < 0:
                self.player.play(self.lnk,item)
            show_window = False
            while self.player.active and not self.local:
                if settings.getSetting('engine-status') == "true":
                        if show_window == False and xbmc.getCondVisibility('Window.IsActive(videoosd)'):
                                lat123.show()
                                show_window = True
                        elif not xbmc.getCondVisibility('Window.IsActive(videoosd)'):
                                try:
                                        lat123.hide()
                                except: pass
                                show_window = False
                self.loop()
                xbmc.sleep(300)
                if xbmc.abortRequested:
                    self.log.out("XBMC asked to abort request")
                    break
            self.log.out('ended play')
      
    def loop(self):
        pos=self.pos
        
        if len(self.player.coms)>0:
            comm=self.player.coms[0]
            self.player.coms.remove(comm)
            self.TSpush(comm)
        
        if self.player.isPlaying():
            if self.player.getTotalTime()>0: cpos= int((1-(self.player.getTotalTime()-self.player.getTime())/self.player.getTotalTime())*100)
            else: cpos=0
            if cpos in pos: 
                pos.remove(cpos)
                comm='PLAYBACK '+self.player.link.replace('\r','').replace('\n','')+' %s'%cpos
                self.TSpush(comm)
        
        if self.tsserv.event and save:
            self.log.out('Try to save file in loop')
            comm='SAVE %s path=%s'%(self.tsserv.event[0]+' '+self.tsserv.event[1],urllib.quote(self.filename))
            self.TSpush(comm)
            self.tsserv.event=None
            succ=True
            self.saved=True
        
        if self.saved and self.player.started:
            self.log.out('saving content')
            if  self.player.isPlaying() and os.path.exists(self.filename.decode('utf-8')): 
                xbmc.sleep(10000)
                self.log.out('Start local file')
                self.tsserv.got_url=self.filename
                self.local=True
                
                self.sm('Start Local File')
                try: time1=self.player.getTime()
                except: time1=0
                
                i = xbmcgui.ListItem("***%s"%self.title)
                i.setProperty('StartOffset', str(time1))
                self.log.out('Play local file')
                self.local=True
                self.player.active=False 
        

    def load_torrent(self, torrent, mode, host=server_ip, port=aceport ):
        self.mode=mode
        self.url=torrent
        if not self.connect(): 
            
            return False
        if not self.ts_init(): 
            self.sm('Initialization Failed')
            return False
        self.conn=True
        self.progress.update(0,translate(1102),"")
        
        if mode!='PID': spons=' 0 0 0'
        else: spons=''
        comm='LOADASYNC '+ str(random.randint(0, 0x7fffffff)) +' '+mode+' ' + torrent + spons
        self.TSpush(comm)

        while not self.tsserv.files and not self.progress.iscanceled():
            if xbmc.abortRequested:
                self.log.out("XBMC is shutting down")
                break
            if self.tsserv.err:
                self.log.out("Failed to load files")
                break
            xbmc.sleep(200)
        if self.progress.iscanceled(): 
            return False
        if not self.tsserv.files: 
            self.sm('Failed to load list files')
            return False
        self.filelist=self.tsserv.files
        self.file_count = self.tsserv.count
        self.files={}
        self.progress.update(89,translate(40043),'')
        if self.file_count>1:
            flist=json.loads(self.filelist)
            for list in flist['files']:
                self.files[urllib.unquote_plus(urllib.quote(list[0]))]=list[1]
        elif self.file_count==1:
            flist=json.loads(self.filelist)
            list=flist['files'][0]
            self.files[urllib.unquote_plus(urllib.quote(list[0]))]=list[1]

        self.progress.update(100,translate(40051),'')
        
        return "Ok"

    def end(self):
        if settings.getSetting("kill_type") == "1" or xbmc.getCondVisibility('System.Platform.Android') or xbmc.getCondVisibility('system.platform.windows'):
            self.active=False
            comm='SHUTDOWN'
            if self.conn:self.TSpush(comm)
            self.log.out("Ending")
            try: self._sock.shutdown(socket.SHUT_WR)
            except: pass
            if self.tsserv: self.tsserv.active=False
            if self.tsserv: self.tsserv.join()
            self.log.out("end thread")
            self._sock.close()
            self.log.out("socket closed")
            if self.progress:self.progress.close()

            if settings.getSetting('engine-status') == "true": 
                try:lat123._close()
                except:pass

            if xbmc.getCondVisibility('system.platform.windows'):
                if settings.getSetting('shutdown-engine') == "true":
                    subprocess.Popen('taskkill /F /IM ace_engine.exe /T',shell=True)
                else: pass
            elif xbmc.getCondVisibility('system.platform.linux'):
                if settings.getSetting('shutdown-engine') == "true":
                    try:
                        self.proc.kill()
                        self.proc.wait()
                        if settings.getSetting('openelecx86_64') == "true" or settings.getSetting('openeleci386') == "true":
                            os.system("kill $(ps aux | grep '[a]cestream' | awk '{print $1}')")
                    except: pass
            elif xbmc.getCondVisibility('system.platform.OSX'):
                if settings.getSetting('shutdown-engine') == "true":
                    try:
                        self.proc.kill()
                        self.proc.wait()
                    except: pass

        if settings.getSetting("kill_type") == "0" and not xbmc.getCondVisibility('System.Platform.Android') and not xbmc.getCondVisibility('system.platform.windows'):
            if xbmc.getCondVisibility('system.platform.linux'):
                os.system("kill $(ps aux | grep '[a]cestream' | awk '{print $1}')")
                os.system("kill $(ps aux | grep '[a]cestream' | awk '{print $2}')")
                os.system("kill $(ps aux | grep '[s]tart.py' | awk '{print $2}')")
                if settings.getSetting('save') != "true":
                    try:
                        cache_file = self.lnk.split('/')[-2]
                        acestream_cachefolder_file = os.path.join(os.getenv("HOME"),'.ACEStream','cache',cache_file)
                        xbmcvfs.delete(acestream_cachefolder_file)
                    except: pass
                          
            elif xbmc.getCondVisibility('system.platform.OSX'):
                os.system("kill $(ps aux | grep '[s]tart.py')")
                if settings.getSetting('save') != "true":
                    try:
                        cache_file = self.lnk.split('/')[-2]
                        acestream_cachefolder_file = os.path.join(os.getenv("HOME"),'.ACEStream','cache',cache_file)
                        xbmcvfs.delete(acestream_cachefolder_file)
                    except: pass

            self.active=False
            self.log.out("Force Killing")
            try: self._sock.shutdown(socket.SHUT_WR)
            except: pass
            if self.tsserv: self.tsserv.active=False
            if self.tsserv: self.tsserv.join()
            self.log.out("end thread")
            self._sock.close()
            self.log.out("socket closed")
            if self.progress:self.progress.close()
            

        
    def __del__(self):
        settings.setSetting('active','0')
        
class TSServ(threading.Thread):

    def __init__(self,_socket):
        self.pkey='n51LvQoTlJzNGaFxseRK-uvnvX-sD4Vm5Axwmc4UcoD-jruxmKsuJaH0eVgE'
        threading.Thread.__init__(self)
        self.log=Logger("TSServer")
        self.inc=Logger('IN')
        self.log.out("init")
        self.sock=_socket
        self.daemon = True
        self.active = True
        self.err = False
        self.buffer=65020
        self.temp=""
        self.msg=None
        
        self.version=None

        self.fileslist=None
        self.files=None
        self.key=None
        self.count=None
        self.ind=None
        
        self.got_url=None
        self.event=None
        self.proc=0
        self.label=''
        self.line=''
        self.pause=False
    def run(self):
        while self.active and not self.err:

            try:
                self.last_received=self.sock.recv(self.buffer)
            except: self.last_received=''

            ind=self.last_received.find('\r\n')
            cnt=self.last_received.count('\r\n')

            if ind!=-1 and cnt==1:
                self.last_received=self.temp+self.last_received[:ind]
                self.temp=''
                self.exec_com()
            elif cnt>1:
                fcom=self.last_received
                ind=1
                while ind!=-1:
                    ind=fcom.find('\r\n')
                    self.last_received=fcom[:ind]
                    self.exec_com()
                    fcom=fcom[(ind+2):]
            elif ind==-1: 
                self.temp=self.temp+self.last_received
                self.last_received=None



        self.log.out('Daemon Dead')
                
    def exec_com(self):
        
        self.inc.out(self.last_received)
        line=self.last_received
        comm=self.last_received.split(' ')[0]
        params=self.last_received.split(' ')[1::]
        self.msg=line
        if settings.getSetting('ace-debug') == "true":
            print('Sent command: ' + str(comm))
        if comm=='HELLOTS':
            try: self.version=params[0].split('=')[1]
            except: self.version='1.0.6'
            try: 
            	match = re.compile('key=(.*)').findall(line)
            	self.key = match[0].split(' ')[0]
            except: self.key=None
        elif comm=='LOADRESP':
            fil = line
            ll= fil[fil.find('{'):len(fil)]
            self.fileslist=ll

            json_files=json.loads(self.fileslist)
            try:
                aa=json_files['infohash']
                if json_files['status']==2:
                    self.count=len(json_files['files'])
                if json_files['status']==1:
                    self.count=1
                if json_files['status']==0:
                    self.count=None
                self.files=self.fileslist.split('\n')[0]
                self.fileslist=None
                self.log.out("files:%s"%self.files) 
            except:
                self.count=None
                self.fileslist=None
                self.err=True
        elif comm=='EVENT':
            if self.last_received.split(' ')[1]=='cansave':
                event=self.last_received.split(' ')[2:4]
                ind= event[0].split('=')[1]
                if int(ind)==int(self.ind): self.event=event
            if self.last_received.split(' ')[1]=='getuserdata':
                self.sock.send('USERDATA [{"gender": 1}, {"age": 3}]\r\n')
                
        elif comm=='START' or comm=='PLAY': 
            servip=settings.getSetting('ip_addr')
            self.got_url=self.last_received.split(' ')[1].replace('127.0.0.1',servip) # 
            self.log.out('Get Link:%s'%self.got_url)
            self.params=self.last_received.split(' ')[2:]
            if 'stream=1' in self.params: self.log.out('Live Stream')
            else: self.log.out('VOD Stream')
        elif comm=='RESUME': self.pause=0
        elif comm=='PAUSE': self.pause=1   
        if comm=="STATUS": self.showStats(line)   
        
    def showStats(self,params):
        params=params.split(' ')[1]
        ss=re.compile('main:[a-z]+',re.S)
        s1=re.findall(ss, params)[0]
        st=s1.split(':')[1]
        self.proc=0
        self.label=" "
        self.line=" "

        if st=='idle':
            self.label=translate(1105)
            if settings.getSetting('ace-debug') == "true":
                print('Received command Engine idle' )

        elif st=='starting':
            self.label=translate(40055)
            if settings.getSetting('ace-debug') == "true":
                print('Received command starting TS' )

        elif st=='err':
            self.label=translate(1011)
            self.err="dl"
            if settings.getSetting('ace-debug') == "true":
                print('Received command ERROR!' )

        elif st=='check': 
            self.label=translate(1103)
            self.proc=int(params.split(';')[1])
            if settings.getSetting('ace-debug') == "true":
                print('Received command check' )

        elif st=='prebuf':   
            self.proc=int( params.split(';')[1] )+0.1
            self.label=translate(1100)
            self.line='Seeds:%s Download:%sKb/s'%(params.split(';')[8],params.split(';')[5])  
            engine_data = { "action": str(translate(1100)), "percent": str(params.split(';')[1])+ "%","download":str(params.split(';')[5]) + " Kb/s", "upload":str(params.split(';')[7]) + " Kb/s","seeds":str(params.split(';')[8]),"total_download":str(int(params.split(';')[10])/(1024*1024))+'Mb',"total_upload":str(int(params.split(';')[12])/(1024*1024))+'Mb' }
            if settings.getSetting('ace-debug') == "true":
                print('Received command: ' + str(engine_data) )

        elif st=='loading':
            self.label=translate(40043)
            if settings.getSetting('ace-debug') == "true":
                print('Received command loading' )

        elif st=='dl':
            engine_data = { "action": str(translate(50010)), "percent": str(params.split(';')[1])+ "%","download":str(params.split(';')[3]) + " Kb/s", "upload":str(params.split(';')[5]) + " Kb/s","seeds":str(params.split(';')[6]),"total_download":str(int(params.split(';')[8])/(1024*1024))+'Mb',"total_upload":str(int(params.split(';')[10])/(1024*1024))+'Mb' }
            if settings.getSetting('engine-status') == "true":
                try:
                        lat123.set_information(engine_data)
                except: pass
            if settings.getSetting('ace-debug') == "true":
                print('Received command: ' + str(engine_data) )

        elif st=='buf':
            engine_data = { "action": str(translate(50008)), "percent": str(params.split(';')[1])+ "%","download":str(params.split(';')[5]) + " Kb/s", "upload":str(params.split(';')[7]) + " Kb/s","seeds":str(params.split(';')[8]),"total_download":str(int(params.split(';')[10])/(1024*1024))+"Mb","total_upload":str(int(params.split(';')[12])/(1024*1024))+"Mb" }
            if settings.getSetting('engine-status') == "true":
                try:
                        lat123.set_information(engine_data)
                except: pass
            if settings.getSetting('ace-debug') == "true":
                print('Received command: ' + str(engine_data) )


    def end(self):
        self.active = False
        self.daemon = False
        self.log.out('Daemon Fully Dead')



class OverlayText(object):
        def __init__(self):
                self.showing = False
                self.window = xbmcgui.Window(12005)
                origin_x = 920
                origin_y = 90
                #main window
                self._background = xbmcgui.ControlImage(origin_x, origin_y, 340, 280, os.path.join(addonpath,"resources","art","lateral-fundo.png"))
                self._acestreamlogo = xbmcgui.ControlImage(origin_x + 30, origin_y + 20, 40, 35, os.path.join(addonpath,"resources","art","acestreamlogo.png"))
                self._supseparator = xbmcgui.ControlImage(origin_x, origin_y + 65, 330, 1, os.path.join(addonpath,"resources","art","lateral-separador.png"))
                self._botseparator = xbmcgui.ControlImage(origin_x, origin_y + 260, 330, 1, os.path.join(addonpath,"resources","art","lateral-separador.png"))
                self._title = xbmcgui.ControlLabel(origin_x+100, origin_y + 25, 200, 20, str(translate(50000)), font='font13', textColor='0xFFEB9E17')
                self._total_stats_label = xbmcgui.ControlLabel(origin_x+125, origin_y + 175, 200, 20, str(translate(50005)), font='font10', textColor='0xFFEB9E17')
                #labels
                self._action = xbmcgui.ControlLabel(origin_x+20, origin_y + 80, 200, 20, str(translate(50001)), font='font10')
                self._download = xbmcgui.ControlLabel(origin_x+20, origin_y + 105, 200, 20, str(translate(50002)), font='font10')
                self._upload = xbmcgui.ControlLabel(origin_x+20, origin_y + 130, 200, 20, str(translate(50003)), font='font10')
                self._seeds = xbmcgui.ControlLabel(origin_x+20, origin_y + 155, 200, 20, str(translate(50004)), font='font10')
                self._total_download = xbmcgui.ControlLabel(origin_x+20, origin_y + 205, 200, 20, str(translate(50006)), font='font10')
                self._total_upload = xbmcgui.ControlLabel(origin_x+20, origin_y + 230, 200, 20, str(translate(50007)), font='font10')
                #values
                self._action_value = xbmcgui.ControlLabel(origin_x+80, origin_y + 80, 200, 20,'N/A', font='font10')
                self._percent_value = xbmcgui.ControlLabel(origin_x+280, origin_y + 80, 200, 20,'N/A', font='font10')
                self._download_value = xbmcgui.ControlLabel(origin_x+105, origin_y + 105, 200, 20,'N/A', font='font10')
                self._upload_value = xbmcgui.ControlLabel(origin_x+85, origin_y + 130, 200, 20,'N/A', font='font10')
                self._seeds_value = xbmcgui.ControlLabel(origin_x+75, origin_y + 155, 200, 20,'N/A', font='font10')
                self._total_download_value = xbmcgui.ControlLabel(origin_x+120, origin_y + 205, 200, 20,'N/A', font='font10')
                self._total_upload_value = xbmcgui.ControlLabel(origin_x+100, origin_y + 230, 200, 20,'N/A', font='font10')


        def show(self):
                self.showing=True
                self.window.addControl(self._background)
                self.window.addControl(self._acestreamlogo)
                self.window.addControl(self._supseparator)
                self.window.addControl(self._botseparator)
                self.window.addControl(self._title)
                self.window.addControl(self._action)
                self.window.addControl(self._download)
                self.window.addControl(self._upload)
                self.window.addControl(self._seeds)
                self.window.addControl(self._total_stats_label)
                self.window.addControl(self._total_download)
                self.window.addControl(self._total_upload)
                self.window.addControl(self._action_value)
                self.window.addControl(self._download_value)
                self.window.addControl(self._upload_value)
                self.window.addControl(self._seeds_value)
                self.window.addControl(self._total_download_value)
                self.window.addControl(self._total_upload_value)
                self.window.addControl(self._percent_value)


        def hide(self):
                self.showing=False
                self.window.removeControl(self._total_download)
                self.window.removeControl(self._total_upload)
                self.window.removeControl(self._action_value)
                self.window.removeControl(self._download_value)
                self.window.removeControl(self._upload_value)
                self.window.removeControl(self._seeds_value)
                self.window.removeControl(self._total_download_value)
                self.window.removeControl(self._total_upload_value)
                self.window.removeControl(self._percent_value)
                self.window.removeControl(self._title)
                self.window.removeControl(self._action)
                self.window.removeControl(self._download)
                self.window.removeControl(self._upload)
                self.window.removeControl(self._seeds)
                self.window.removeControl(self._total_stats_label)
                self.window.removeControl(self._acestreamlogo)
                self.window.removeControl(self._supseparator)
                self.window.removeControl(self._botseparator)
                self.window.removeControl(self._background)


        def set_information(self,engine_data):
                if self.showing == True:
                        self._action_value.setLabel(engine_data["action"])
                        self._percent_value.setLabel(engine_data["percent"])
                        self._download_value.setLabel(engine_data["download"])
                        self._upload_value.setLabel(engine_data["upload"])
                        self._seeds_value.setLabel(engine_data["seeds"])
                        self._total_download_value.setLabel(engine_data["total_download"])
                        self._total_upload_value.setLabel(engine_data["total_upload"])
                else: pass


        def _close(self):
                if self.showing:
                        self.hide()
                else:
                        pass
                try: 
                        self.window.clearProperties()
                        print("OverlayText window closed")
                except: pass

    
