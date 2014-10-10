import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import re, string, sys, os
import urlresolver
from TheYid.common.addon import Addon
from TheYid.common.net import Net
from htmlentitydefs import name2codepoint as n2cp
import HTMLParser

addon_id = 'plugin.video.allinone'
plugin = xbmcaddon.Addon(id=addon_id)
net = Net()
addon = Addon('plugin.video.allinone', sys.argv)
DB = os.path.join(xbmc.translatePath("special://database"), 'allinone.db')
BASE_URL = 'http://oneclickwatch.org/'
BASE_URL1 = 'http://awesomedl.ru/'
BASE_URL3 = 'http://viooz.pw/'
BASE_URL4 = 'http://ultra-vid.com/'###
BASE_URL10 = 'http://www.myvideolinks.eu/'
BASE_URL12 = 'http://www.flixanity.is/'
BASE_URL14 = 'http://www.channelcut.me/'
BASE_URL15 = 'http://primeflicks.me/'
BASE_URL20 = 'http://world4ufree.com/'
BASE_URL21 = 'http://movies2k.eu/'
BASE_URL23 = 'http://300mbmovies4u.com/'
BASE_URL25 = 'http://www.rapgrid.com/'
BASE_URL29 = 'http://shows4u.info/'
BASE_URL30 = 'http://www.tupeliculashd.com/'
BASE_URL32 = 'http://www.tvhq.info/'
BASE_URL35 = 'https://raw.githubusercontent.com/TheYid/yidpics/master'
BASE_URL38 = 'http://www.movierulz.com/'
BASE_URL39 = 'http://wrestlingrulez.net/'
BASE_URL40 = 'http://www.uwatchfree.net/'
BASE_URL40a = 'http://www.uwatchfree.net/genres/'
BASE_URL41 = 'http://undergroundflix.com/'

#### PATHS ##########
AddonPath = addon.get_path()
IconPath = AddonPath + "/icons/"
FanartPath = AddonPath + "/icons/"

##### Queries ##########
mode = addon.queries['mode']
url = addon.queries.get('url', None)
content = addon.queries.get('content', None)
query = addon.queries.get('query', None)
startPage = addon.queries.get('startPage', None)
numOfPages = addon.queries.get('numOfPages', None)
listitem = addon.queries.get('listitem', None)
urlList = addon.queries.get('urlList', None)
section = addon.queries.get('section', None)

##################################### GetTitles ################################ GetTitles ############################################### GetTitles ######################################

#------------------------------------------------------------------------------- oneclickwatch ------------------------------------------------------------------------------#

def GetTitles(section, url, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                       
                match = re.compile('<h2.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')    
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- ADL -----------------------------------------------------------------------------------------#

def GetTitles1(section, url, startPage= '1', numOfPages= '1'): 
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>\s*?<div class="postmeta-primary">\s*?<span class="meta_date">.+?</span> <span class="meta_categories">.+?<a href=".+?" rel="tag">.+?</a></span>\s*?</div>\s*?<img width="280" src="(.+?)" class="alignleft" alt="" />', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles1', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')      
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------- viooz ----------------------------------------------------------------------------------------------#

def GetTitles3(section, url, startPage= '1', numOfPages= '1'): 
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('postsbody.+?href="(.+?)".+?="(.+?)">.+?src=".+?src=(.+?)&amp;.+?"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles3', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')           
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------- ultra-vid ------------------------------------------------------------------------------------------------------#

def GetTitles4(section, url, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                      
                match = re.compile('<span class="itemdets"> <a href="(.+?)" title="(.+?)"> </span><center><img src="(.+?)" alt=".+?" /></center><span class="morelink"> <a href=".+?" title=".+?"></a> </span></div><div class="boxitem">', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles4', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')       
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------- myvideolinks --------------------------------------------------------------------------------------#

def GetTitles10(section, url, startPage= '1', numOfPages= '1'): 
    try:
        print 'allinone get Movie Titles Menu %s' % url
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                        
                match = re.compile('<a href=".+?" rel="bookmark" title=".+?"> <img src="(.+?)"  title=".+?" class="alignleft" alt=".+?" /></a>\s*?<h4><a href="(.+?)" rel="bookmark" title="(.+?)">.+?</a></h4>', re.DOTALL).findall(html)
                for img, movieUrl, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks7', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')      
                addon.add_directory({'mode': 'GetTitles10', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')         
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- flixanity movie 1 ----------------------------------------------------------------------------------------#

def GetTitles12(section, url, startPage= '1', numOfPages= '1'): 
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + startPage + ''
                        html = net.http_GET(pageUrl).content
                match = re.compile('<a href="(.+?)" class="item" title="">\s*?<img class="img-preview spec-border"  src="(.+?)"', re.DOTALL).findall(html)
                for img, movieUrl in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip().replace('(', '').replace(')', ''))
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks1a', 'section': section, 'url': movieUrl}, {'title':  movieUrl}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles12', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------- flixanity movie categories -------------------------------------------------------------------------------------------#

def Categories(url):  #movie-tags
        url = BASE_URL12 + '/movie-tags/'
        html = net.http_GET(BASE_URL12).content
        match = re.compile('<li><a href=.+?/movie-tags/(.+?)">(.+?)<').findall(html)
        for cat, title in match:
                url = url + cat
                addon.add_directory({'mode': 'GetTitles31', 'url': url, 'startPage': '1', 'numOfPages': '1'}, {'title':  title + '...    (Newest 1st)'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Categories1(url):  #imdb_rating
        url = BASE_URL12 + '/movie-tags/'
        html = net.http_GET(BASE_URL12).content
        match = re.compile('<li><a href=.+?/movie-tags/(.+?)">(.+?)<').findall(html)
        for cat, title in match:
                url = url + cat
                addon.add_directory({'mode': 'GetTitles31', 'url': url + '/imdb_rating/', 'startPage': '1', 'numOfPages': '1'}, {'title':  title + '...    (IMDB)'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Categories2(url):  #abc
        url = BASE_URL12 + '/movie-tags/'
        html = net.http_GET(BASE_URL12).content
        match = re.compile('<li><a href=.+?/movie-tags/(.+?)">(.+?)<').findall(html)
        for cat, title in match:
                url = url + cat
                addon.add_directory({'mode': 'GetTitles31', 'url': url + '/abc/', 'startPage': '1', 'numOfPages': '1'}, {'title':  title + '...    (ABC)'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles31(section, url, startPage= '1', numOfPages= '1'): 
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + startPage + ''
                        html = net.http_GET(pageUrl).content
                match = re.compile('<div class="ribbon-wrapper"><div class="ribbon black">.+?</div></div>\s*?<a href=".+?" class="item" title="">\s*?<img class="img-preview spec-border"  src="(.+?)" alt=" " style=".+?"/>\s*?</a>\s*?</div>\s*?<div class="back">\s*?<h3><a href="(.+?)">(.+?)</a></h3>', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks1a', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles31', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------- flixanity tv -----------------------------------------------------------------------------------------#

def GetTitles27(section, url, startPage= '1', numOfPages= '1'): #2nd
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<a class="link" href="(.+?)" title="(.+?)">.+?<span',re.DOTALL).findall(html)
        for movieUrl, name in match:
                addon.add_directory({'mode': 'GetLinks1a', 'section': section, 'url': movieUrl}, {'title':  name.strip()},img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------#

def GetTitles27a(section, url, startPage= '1', numOfPages= '1'): #1st
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + startPage + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('img-preview spec-border.+?src=".+?src=(.+?)&amp;.+?".+?href="(.+?)".+?>.+?<.+?', re.DOTALL).findall(html)
                for img, movieUrl in match:
                        addon.add_directory({'mode': 'GetTitles27', 'section': section, 'url': movieUrl}, {'title':  movieUrl.replace('http://www.flixanity.is/show/', '').replace('-', ' ')}, img= img, fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------- channelcut ---------------------------------------------------------------------------------#

def GetTitles14(section, url, startPage= '1', numOfPages= '1'): 
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                     
                match = re.compile('<h1 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h1>', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'cc.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles14', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------------- undergroundflix ---------------------------------------------------------------------------------#

def GetTitles41(section, url, startPage= '1', numOfPages= '1'): 
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                     
                match = re.compile('<h4><a href="(.+?)" title="(.+?)">.+?</a></h4>', re.DOTALL).findall(html)
                for movieUrl, name in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img=IconPath + 'uf.png', fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles41', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site mite be down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------ primeflicks movie -----------------------------------------------------------------------------------#

def GetTitles15(section, url, startPage= '1', numOfPages= '1'): 
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + startPage + ''
                        html = net.http_GET(pageUrl).content                   
                match = re.compile('img-preview spec-border.+?src=".+?src=(.+?)&amp;.+?".+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
                for img, movieUrl, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks1', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles15', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- primeflicks tv ----------------------------------------------------------------------------------#

def GetTitles15a(section, url, startPage= '1', numOfPages= '1'): #2nd
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<a class="link" href="(.+?)">.+?<span class="tv_episode_name"> - (.+?)</span></a>',re.DOTALL).findall(html)
        for movieUrl, name in match:
                addon.add_directory({'mode': 'GetLinks1', 'section': section, 'url': movieUrl}, {'title':  name.strip()},img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------#

def GetTitles15b(section, url, startPage= '1', numOfPages= '1'): #1st
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + startPage + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('img-preview spec-border.+?src=".+?src=(.+?)&amp;.+?".+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
                for img, movieUrl, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetTitles15a', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------- world4ufree -----------------------------------------------------------------------------------------#

def GetTitles20(section, url, startPage= '1', numOfPages= '1'): 
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                    
                match = re.compile('<div class="cover"><a href="(.+?)" title="(.+?)"><img src="(.+?)" alt=.+? class=.+? width=.+? height=.+? /></a></div>', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles20', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png') 
        setView('tvshows', 'tvshows-view')        
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------- movies2k.eu ------------------------------------------------------------------------------------------#

def GetTitles21(section, url, startPage= '1', numOfPages= '1'): 
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<h2.+?href="(.+?)".+?>(.+?)<.+?src="(.+?)".+?', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles21', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png') 
        setView('tvshows', 'tvshows-view')  
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------- 300mbmovies4u ------------------------------------------------------------------------------------------#

def GetTitles23(section, url, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<div class="cover"><a href="(.+?)".+?.+?<img src="(.+?)".+?alt="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles23', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view') 
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------- rapgrid ----------------------------------------------------------------------------------------#

def GetTitles25(section, url, startPage= '1', numOfPages= '1'): #rapgrid
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content
                match = re.compile('<div class="battleTeaserPhoto"><a href="(.+?)" title="(.+?)"><img src="(.+?)" width="150" height="113"/></a></div>', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks5', 'section': section, 'url': 'http://www.rapgrid.com/' + movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------- shows4u -----------------------------------------------------------------------------------#

def GetTitles28(section, url, startPage= '1', numOfPages= '1'):  #2nd
        pageUrl = url
        html = net.http_GET(pageUrl).content
        match = re.compile('<a class="link" href="(.+?)" title="(.+?)"',re.DOTALL).findall(html)
        for movieUrl, name in match:
                addon.add_directory({'mode': 'GetLinks8', 'section': section, 'url': movieUrl}, {'title':  name.strip()},img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------#

def GetTitles28a(section, url, startPage= '1', numOfPages= '1'): #1st
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + startPage + ''
                        html = net.http_GET(pageUrl).content
                match = re.compile('<img class="img-preview spec-border"  src=".+?src=(.+?)&amp;.+?" alt=" ".+?<a class="link" href="(.+?)" title="(.+?)">',re.DOTALL).findall(html)
                if not match:
                    match = re.compile('<img class="img-preview spec-border show-thumbnail"  src=".+?src=(.+?)&amp;.+?" alt=" ".+?<a class="link" href="(.+?)" title="(.+?)">',re.DOTALL).findall(html)
                for img, movieUrl, name in match:
                        addon.add_directory({'mode': 'GetTitles28', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles28a', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------ tupeliculashd -----------------------------------------------------------------------------------------------------#

def GetTitles30(section, url, startPage= '1', numOfPages= '1'): #1st
        pageUrl = url
        html = net.http_GET(pageUrl).content
        match = re.compile("<a dir='ltr' href='(.+?)'>(.+?)</a>",re.DOTALL).findall(html)
        for movieUrl, name in match:
                addon.add_directory({'mode': 'GetTitles30a', 'section': section, 'url': movieUrl}, {'title': name.strip()},img= 'http://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/750px-Flag_of_Spain.svg.png', fanart=FanartPath + 'fanart.png') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles30a(section, url, startPage= '1', numOfPages= '1'): #2nd
        pageUrl = url
        html = net.http_GET(pageUrl).content
        match = re.compile("<h2 class='post-title entry-title'>\s*?<a href='(.+?)'>(.+?)</a>",re.DOTALL).findall(html)
        for movieUrl, name in match:
                addon.add_directory({'mode': 'GetTitles30b', 'section': section, 'url': movieUrl}, {'title': name.strip()},img= 'http://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/750px-Flag_of_Spain.svg.png', fanart=FanartPath + 'fanart.png') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles30b(section, url, startPage= '1', numOfPages= '1'): #3rd
        pageUrl = url
        html = net.http_GET(pageUrl).content
        match = re.compile('<iframe src="http://api.video.mail.ru(.+?)" width=".+?" height=".+?"',re.DOTALL).findall(html)
        match1 = re.compile('<iframe src="http://vk.com/(.+?)" width=".+?" height=".+?"',re.DOTALL).findall(html)
        for movieUrl in match:
                addon.add_directory({'mode': 'GetTitles30c', 'section': section, 'url': 'http://api.video.mail.ru' + movieUrl}, {'title': 'video.mail.ru >>'},img= 'http://www.seo.com/wp-content/uploads/2009/07/one-way-link-building.jpg', fanart=FanartPath + 'fanart.png') 
        for movieUrl in match1:
                addon.add_directory({'mode': 'GetTitles30d', 'section': section, 'url': 'http://vk.com/' + movieUrl}, {'title': 'vk.com >>'},img= 'http://www.seo.com/wp-content/uploads/2009/07/one-way-link-building.jpg', fanart=FanartPath + 'fanart.png') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles30c(section, url, startPage= '1', numOfPages= '1'): #4th
        pageUrl = url
        html = net.http_GET(pageUrl).content
        match = re.compile('videoPresets = {"sd":".+?","md":"(.+?)"}',re.DOTALL).findall(html)
        for movieUrl in match:
                addon.add_directory({'mode': 'PlayVideo1', 'section': section, 'url': movieUrl}, {'title': 'Load video.mail.ru Link >>'},img= 'http://langestore.vn.ua/img/cms/vzlom_my_mail_ru_big.png', fanart=FanartPath + 'fanart.png') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles30d(section, url, startPage= '1', numOfPages= '1'): #5th
        pageUrl = url
        html = net.http_GET(pageUrl).content
        match = re.compile('"url360":"(.+?)?extra=',re.DOTALL).findall(html)
        for movieUrl in match:
                url = url.replace('\/','/')
                addon.add_directory({'mode': 'PlayVideo1', 'section': section, 'url': movieUrl}, {'title': 'Load vk.com Link >>'},img= 'http://www.enkisa.com/wp-content/uploads/2012/05/vk.com_logo1.jpg', fanart=FanartPath + 'fanart.png') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------ TVHQ Categories movies -----------------------------------------------------------------------------------------------------#

def Categoriestvhq(url):  #movie-tags
        url = BASE_URL32 + '/movie-tags/'
        html = net.http_GET(BASE_URL32).content
        match = re.compile('<li><a href=.+?/movie-tags/(.+?)">(.+?)<').findall(html)
        for cat, title in match:
                url = url + cat
                addon.add_directory({'mode': 'GetTitles32', 'url': url, 'startPage': '1', 'numOfPages': '1'}, {'title':  title + '...    (Newest 1st)'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def Categoriestvhq1(url):  #imdb_rating
        url = BASE_URL32 + '/movie-tags/'
        html = net.http_GET(BASE_URL32).content
        match = re.compile('<li><a href=.+?/movie-tags/(.+?)">(.+?)<').findall(html)
        for cat, title in match:
                url = url + cat
                addon.add_directory({'mode': 'GetTitles32', 'url': url + '/imdb_rating/', 'startPage': '1', 'numOfPages': '1'}, {'title':  title + '...    (IMDB)'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Categoriestvhq2(url):  #abc
        url = BASE_URL32 + '/movie-tags/'
        html = net.http_GET(BASE_URL32).content
        match = re.compile('<li><a href=.+?/movie-tags/(.+?)">(.+?)<').findall(html)
        for cat, title in match:
                url = url + cat
                addon.add_directory({'mode': 'GetTitles32', 'url': url + '/abc/', 'startPage': '1', 'numOfPages': '1'}, {'title':  title + '...    (ABC)'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetTitles32(section, url, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + startPage + ''
                        html = net.http_GET(pageUrl).content                   
                match = re.compile('img-preview spec-border.+?src=".+?src=(.+?)&amp;w=130&amp;h=190&amp;zc=1".+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
                for img, movieUrl, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip().replace('(', '').replace(')', ''))
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png') 
                addon.add_directory({'mode': 'GetTitles32', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------- hqtv movies --------------------------------------------------------------------------------------------#

def GetTitles32a(section, url, startPage= '1', numOfPages= '1'): #2nd
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<a class="link" href="(.+?)" title=".+?">(.+?)</a>',re.DOTALL).findall(html)
        for movieUrl, name in match:
                addon.add_directory({'mode': 'GetLinks1', 'section': section, 'url': movieUrl}, {'title':  name.strip()},img=IconPath + 'hqtv.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


def GetTitles32b(section, url, startPage= '1', numOfPages= '1'): #1st
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + '/' + startPage + ''
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + '/' + startPage + ''
                        html = net.http_GET(pageUrl).content
                match = re.compile('img-preview spec-border.+?src=".+?src=(.+?)&amp;w=130&amp;h=190&amp;zc=1".+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
                for img, movieUrl, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip())
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetTitles32a', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')
                addon.add_directory({'mode': 'GetTitles32b', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')  
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))



#------------------------------------------------------------------------------- github iptv -------------------------------------------------------------------------------------#

def GetTitles35a(url):                                           
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<>title="(.+?)" href="(.+?)" />< src="(.+?)"').findall(content)
        for name, url, img in match:
                addon.add_directory({'mode': 'PlayVideo5', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img=img, fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- github help -----------------------------------------------------------------------------------#

def GetTitles37(url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<>title="(.+?)" href="(.+?)" />< src="(.+?)"').findall(content)
        for name, url, img in match:
                addon.add_directory({'mode': 'PlayVideo4', 'url': url, 'listitem': listitem}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def PlayVideo4(url, listitem):
    try:
        print 'in PlayVideo %s' % url
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^^^ Press back ^^^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")


#---------------------------------------------------------------------------------- watchwrestling -----------------------------------------------------------------------------------#

def GetTitles39(section, url, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                       
                match = re.compile('<a class="clip-link" data-id=".+?" title=".+?" href="(.+?)">\s*?<span class="clip">\s*?<img src="(.+?)" alt="Watch (.+?)" /><span', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip().replace('/', ' '))
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetLinks12', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')    
                addon.add_directory({'mode': 'GetTitles', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------- uwatchfree category -----------------------------------------------------------------------------------#

def Categoriesuwf(url):
        url = BASE_URL40a + '/category/'
        html = net.http_GET(BASE_URL40a).content
        match = re.compile('<li class="cat-item cat-item-.+?"><a href="http://www.uwatchfree.net/category/(.+?)/" >(.+?)</a>').findall(html)
        for cat, title in match:
                addon.add_directory({'mode': 'GetTitles40', 'url': 'http://www.uwatchfree.net/category/' + cat + '/', 'startPage': '1', 'numOfPages': '1'}, {'title':  title }, img=IconPath + 'uw3.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetTitles40(section, url, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                       
                match = re.compile('<div class="entry-thumbnails"><a class="entry-thumbnails-link" href="(.+?)" title="(.+?)"><img width="140" height="205" src="(.+?)"', re.DOTALL).findall(html)
                for movieUrl, name, img in match:
                        addon.add_directory({'mode': 'GetLinks', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, img= img, fanart=FanartPath + 'fanart.png')    
                addon.add_directory({'mode': 'GetTitles40', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))


##################################### index ################################ index ############################################### index ############################################


#---------------------------------------------------------------------------- flixanity movie index ---------------------------------------------------------------------------------#

def GetTitles2(query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('<img class="img-preview spec-border"  src=".+?src=(.+?)" alt=" " style=".+?"/>\s*?</a>\s*?<div id=".+?"></div>\s*?</div>\s*?<div class="back">\s*?<h3><a href=".+?">(.+?)</a></h3>"/>',re.DOTALL).findall(html)
        for img, name, query in match:
                addon.add_directory({'mode': 'Search11', 'query': query}, {'title':  query}, img= img, fanart=FanartPath + 'fanart3.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
#---------------------------------------------------------------------------------- flixanity TV index -----------------------------------------------------------------------------------#

def GetTitles2a(query):
    try:
        pageUrl = url
        html = net.http_GET(pageUrl).content                     
        match = re.compile('img-preview spec-border.+?src=".+?src=(.+?)&amp;.+?".+?href="(.+?)".+?>.+?<.+?',re.DOTALL).findall(html)
        for img, query in match:
                addon.add_directory({'mode': 'Search12', 'query': query.replace('http://www.flixanity.is/show/', '').replace('-', ' ') + ' s'}, {'title':  query.replace('http://www.flixanity.is/show/', '').replace('-', ' ')}, img= img, fanart=FanartPath + 'fanart4.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- movierulz movie index ------------------------------------------------------------------------------#

def GetTitles38(section, query, startPage= '1', numOfPages= '1'):
    try:
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                       
                match = re.compile('<div class="entry clearfix">\s*?<a title=".+?" href=".+?"><img width="115" height="170" src="(.+?)" class="attachment-category-thumb wp-post-image" alt="(.+?)" /></a>', re.DOTALL).findall(html)
                for img, query in match:
                        addon.add_directory({'mode': 'Search11', 'section': section, 'query': query}, {'title':  query}, img= img, fanart=FanartPath + 'fanart3.png')    
                addon.add_directory({'mode': 'GetTitles38', 'url': url, 'startPage': str(end), 'numOfPages': numOfPages}, {'title': '[COLOR blue][B][I]Next page...[/B][/I][/COLOR]'}, img=IconPath + 'nextpage1.png', fanart=FanartPath + 'fanart3.png')
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- watchwrestling index ---------------------------------------------------------------------------------#

def GetTitles39a(section, url, startPage= '1', numOfPages= '1'):
    try:
        addon.add_directory({'mode': 'GetTitles2', 'url': BASE_URL12 + '/featuredmovies'}, {'title':  '[COLOR red][B]PLEASE USE CONTEXTMENU TO SEARCH THIS SECTION[/B][/COLOR]'}, img= 'http://img3.wikia.nocookie.net/__cb20120912042430/leagueoflegends/images/f/f1/Warning_UploadText.png', fanart=FanartPath + 'fanart.png')
        pageUrl = url
        if int(startPage)> 1:
                pageUrl = url + 'page/' + startPage + '/'
        print pageUrl
        html = net.http_GET(pageUrl).content
        start = int(startPage)
        end = start + int(numOfPages)
        for page in range( start, end):
                if ( page != start):
                        pageUrl = url + 'page/' + str(page) + '/'
                        html = net.http_GET(pageUrl).content                       
                match = re.compile('<a class="clip-link" data-id=".+?" title=".+?" href="(.+?)">\s*?<span class="clip">\s*?<img src="(.+?)" alt="Watch (.+?)" /><span', re.DOTALL).findall(html)
                for movieUrl, img, name in match:
                        cm  = []
                        runstring = 'XBMC.Container.Update(plugin://plugin.video.allinone/?mode=Search11&query=%s)' %(name.strip().replace('/', ' '))
        		cm.append(('[COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR green]Search[/COLOR]', runstring))
                        addon.add_directory({'mode': 'GetSearchQuery11', 'section': section, 'url': movieUrl}, {'title':  name.strip()}, contextmenu_items= cm, img= img, fanart=FanartPath + 'fanart.png')    
        setView('tvshows', 'tvshows-view')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry site is down [/B][/COLOR],[COLOR blue][B]Please try a different site[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##.replace('/', ' ')## \s*? ##
##################################### Getlinks ################################ Getlinks ############################################### Getlinks ######################################

#--------------------------------------------------------- ocw - wtt - binf - 300mbmovies4u - movies2k.eu --------------------------------------------------------------------------------#
def GetLinks(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('href="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------ primeflicks - hqtv ---------------------------------------------------------------------------------#

def GetLinks1(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('src="(.+?)"').findall(content)
        match1 = re.compile('SRC="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match + match1 :
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        host = host.replace('embed.','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- flixanity --------------------------------------------------------------------------------------------#

def GetLinks1a(section, url): 
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('src="(.+?)"').findall(content)
        match1 = re.compile('<IFRAME SRC="http://www.flixanity.com/jwplayer/gkplugins/player.php?(.+?)" FRAMEBORDER="0" MARGINWIDTH="0" MARGINHEIGHT="0" SCROLLING="NO" WIDTH="870" HEIGHT="505"></IFRAME>').findall(content)
        match2 = re.compile('player.php?(.+?)"').findall(content)
        match3 = re.compile('SRC="(.+?)"').findall(content)
        match4 = re.compile('href="(.+?)"').findall(content)
        match5 = re.compile('onclick="window.open("(.+?)");"><p').findall(content)
        listitem = GetMediaInfo(content)
        for url in match + match1 + match2 + match3 + match4 + match5 :
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        host = host.replace('embed.','')
                        host = host.replace('gdata','')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------ rapgrid ------------------------------------------------------------------------------------#

def GetLinks5(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile("file: '(.+?)'").findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------------- mvl.eu --------------------------------------------------------------------------------------------#

def GetLinks7(section, url): 
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<li><a href="(.+?)">.+?</a></li>').findall(content)
        match1 = re.compile("Watch=window.+?'(.+?)'").findall(content)
        match2 = re.compile("Watch=window.+?'(.+?)'").findall(content)
        listitem = GetMediaInfo(content)
        for url in match1:
                addon.add_directory({'mode': 'GetLinks9', 'url': url, 'listitem': listitem}, {'title':  'V-vids.com'}, img=IconPath + 'vids.png', fanart=FanartPath + 'fanart.png')
        for url in match + match2:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        host = host.replace('youtube.com','[COLOR lime]Movie Trailer[/COLOR]')
                        host = host.replace('youtu.be','[COLOR lime]Movie Trailer[/COLOR]')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def GetLinks9(url):                                            
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('onclick=".+?" href="(.+?)" title=".+?"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                addon.add_directory({'mode': 'PlayVideo1', 'url': url, 'listitem': listitem}, {'title':  'load stream'}, img=IconPath + 'watch.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------- shows4u -------------------------------------------------------------------------------------------#

def GetLinks8(section, url):   
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<IFRAME SRC="(.+?)"').findall(content)
        match1 = re.compile('<iframe src="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match + match1 :
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------------rlssource--------------------------------------------------------------------------------------#

def GetLinks10(section, url): 
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('href=(.+?) target=').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)

                if 'Unknown' in host:
                                continue
                if urlresolver.HostedMediaFile(url= url):
                        print 'in GetLinks if loop'
                        title = url.rpartition('/')
                        title = title[2].replace('.html', '')
                        title = title.replace('.htm', '')
                        title = title.replace('480p','[COLOR coral][B][I]480p[/B][/I][/COLOR]')
                        title = title.replace('720p','[COLOR gold][B][I]720p[/B][/I][/COLOR]')
                        title = title.replace('1080p','[COLOR orange][B][I]1080p[/B][/I][/COLOR]')
                        title = title.replace('mkv','[COLOR gold][B][I]MKV[/B][/I][/COLOR] ')
                        title = title.replace('avi','[COLOR pink][B][I]AVI[/B][/I][/COLOR] ')
                        title = title.replace('mp4','[COLOR purple][B][I]MP4[/B][/I][/COLOR] ')
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host + ' [COLOR gold]:[/COLOR] ' + title }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------------moviezstream------------------------------------------------------------------------------------------------#

def GetLinks11(section, url): 
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<td><a href="(.+?)">Sockshare</a></td>').findall(content)
        match1 = re.compile('<td><a href="(.+?)">Billion</a></td>').findall(content)
        match2 = re.compile('<td><a href="(.+?)">1fichier</a></td>').findall(content)
        match3 = re.compile('<td><a href="(.+?)">Uploaded</a></td>').findall(content)
        match4 = re.compile('<td><a href="(.+?)">FileCloud</a></td>').findall(content)
        match5 = re.compile('<td><a href="(.+?)">Up</a></td>').findall(content)
        match6 = re.compile('<td><a href="(.+?)">MU</a></td>').findall(content)
        match7 = re.compile('<td><a href="(.+?)">Turbo</a></td>').findall(content)
        match8 = re.compile('<td><a href="(.+?)">Putlocker</a></td>').findall(content)
        listitem = GetMediaInfo(content)
        for url in match + match1 + match2 + match3 + match4 + match5 + match6 + match7 + match8:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------ wrestlingrulez ------------------------------------------------------------------------------------#

def GetLinks12(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('<p style=".+?"><a href="(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


#---------------------------------------------------------------------- dlmovies ------------------------------------------------------------------------------------------#

def GetLinks14(section, url):
        html = net.http_GET(url).content
        listitem = GetMediaInfo(html)
        content = html
        match = re.compile('href="http://dlmoviegames.com/download/(.+?)"').findall(content)
        listitem = GetMediaInfo(content)
        for url in match:
                host = GetDomain(url)
                if urlresolver.HostedMediaFile(url= url):
                        addon.add_directory({'mode': 'PlayVideo', 'url': url, 'listitem': listitem}, {'title':  host }, img=IconPath + 'play.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

############################### PlayVideo ######################################## PlayVideo ############################################# PlayVideo ###########################

def PlayVideo(url, listitem):
    try:
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        xbmc.Player().play(stream_url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^ Press back ^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Link may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

#-------livestreams------------#

def PlayVideo2(url, listitem):
    try:
	xbmc.Player().play(url)
        addon.add_directory({'mode': 'help'}, {'title':  '[COLOR slategray][B]^ Press back ^[/B] [/COLOR]'},'','')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry Stream may have been removed ![/B][/COLOR],[COLOR lime][B]Please try a different link/host !![/B][/COLOR],7000,"")")

#-------myvideolinks------------#

def PlayVideo1(url, listitem):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'video')
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]PLAY STREAM[/B][/COLOR]  >> ', iconImage='https://lh5.googleusercontent.com/-p2h0tx7Trgs/Uzu-3kxzKuI/AAAAAAAAOsU/sVJKqxSMY-4/s319/watch2.jpg', thumbnailImage= 'http://s29.postimg.org/8z8jd5x5j/logo1.png')
        li.setProperty('fanart_image', 'http://littletechboy.com/downloads/sins/modding/LoadingSplash.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)

#-------m3u playlists------------#

def PlayVideo5(url, listitem):
        addon_handle = int(sys.argv[1])
        xbmcplugin.setContent(addon_handle, 'video')
        li = xbmcgui.ListItem('[COLOR dodgerblue][B]LOAD STREAM PLAYLIST[/B][/COLOR]  >> ', iconImage='http://www.creation-spip.fr/IMG/arton37.png?1357155686', thumbnailImage= 'http://www.creation-spip.fr/IMG/arton37.png?1357155686')
        li.setProperty('fanart_image', 'http://littletechboy.com/downloads/sins/modding/LoadingSplash.jpg') 
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmcplugin.endOfDirectory(addon_handle)

#--------------------------------------------------------------------------------------------------#

def GetDomain(url):
        tmp = re.compile('//(.+?)/').findall(url)
        domain = 'Unknown'
        if len(tmp) > 0 :
            domain = tmp[0].replace('www.', '')
        return domain

#--------------------------------------------------------------------------------------------------#

def GetMediaInfo(html):
        listitem = xbmcgui.ListItem()
        match = re.search('og:title" content="(.+?) \((.+?)\)', html)
        if match:
                print match.group(1) + ' : '  + match.group(2)
                listitem.setInfo('video', {'Title': match.group(1), 'Year': int(match.group(2)) } )
        return listitem

############################# menus ################################## menus ########################################################### menus ################################

def MainMenu():    #homescreen
        addon.add_directory({'mode': 'MovieMenu'}, {'title':  '[COLOR cornflowerblue][B]Movies >[/B][/COLOR] >'}, img=IconPath + 'films.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'TvMenu'}, {'title':  '[COLOR darkorange][B]Tv Shows >[/B][/COLOR] >'}, img=IconPath + 'tv2.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'SportMenu'}, {'title':  '[COLOR lemonchiffon][B]Sports >[/B][/COLOR] >'}, img=IconPath + 'sport1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles35a', 'url': BASE_URL35 + '/yellow2.txt'}, {'title':  '[COLOR mediumorchid][B]Streams >[/COLOR][/B] >'}, img=IconPath + 'stream.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'MusicMenu'}, {'title':  '[COLOR cadetblue][B]Music >[/B][/COLOR] >'}, img=IconPath + 'music.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'RadioMenu'}, {'title':  '[COLOR lightsteelblue][B]Radio >[/B][/COLOR]>'}, img=IconPath + 'radio.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'SearchMenu'}, {'title':  '[COLOR green][B]Searches >[/B] [/COLOR] >'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[COLOR aquamarine][B]News & Help  >[/B][/COLOR] >'}, img=IconPath + 'helpnew1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-----------------------help---------------------------------------help-----------------------------help--------------------------help-------------------------------help-------#

def HelpMenu(): 
        addon.add_directory({'mode': 'Help'}, {'title':  'Entertainment [COLOR dodgerblue][B]HUB[/B][/COLOR] : [COLOR lime]News >[/COLOR] >'}, img=IconPath + 'helpnew1.png', fanart=FanartPath + 'fanart1.png')
        addon.add_directory({'mode': 'GetTitles37', 'url': BASE_URL35 + '/help.txt'}, {'title':  '[COLOR deeppink]How to videos >[/COLOR] >'}, img=IconPath + 'h2.png', fanart=FanartPath + 'fanart1.png')
        addon.add_directory({'mode': 'ResolverSettings'}, {'title':  '[COLOR red]Resolver Settings >[/COLOR] >'}, img=IconPath + 'resolver.png', fanart=FanartPath + 'fanart1.png')  
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR gold]If you like this addon[/COLOR][/B]'}, img=IconPath + 'twit.png', fanart=FanartPath + 'fanart1.png')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR gold]& you like rave music install Rave player from TheYids REPO[/COLOR][/B]'}, img= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.audio.raveplayer/icon.png', fanart= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.audio.raveplayer/fanart.jpg')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR blue]System/Add-ons/Get Add-ons/TheYids REPO[/COLOR][/B]'}, img= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/repository.TheYid/icon.png', fanart= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.video.allinone/fanart.jpg')
        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR aqua]@TheYid009[/COLOR][/B] - [B][COLOR gold]Add me on twitter for all the latest news & updates..[/COLOR][/B]'}, img=IconPath + 'twit.png', fanart=FanartPath + 'fanart1.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------MusicVideos-----------------------------MusicVideos-------------------------------------MusicVideos---------------------------MusicVideos-----------#

def MusicMenu():   #MusicVideos
        addon.add_directory({'mode': 'GetTitles25', 'section': 'ALL', 'url': BASE_URL25 + '/battles',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cadetblue][B]Rap Battle videos[/B][/COLOR] [COLOR springgreen](Rap Grid) [/COLOR]>>'}, img=IconPath + 'rg.png', fanart=FanartPath + 'fanart.png')

        addon_handle = int(sys.argv[1]) 
        xbmcplugin.setContent(addon_handle, 'audio')

        url = 'rtmp://live.drumandbasslines.com/DnBTV/ch1'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Drum and Bass tv[/B][/COLOR] >>  [COLOR lime](live)[/COLOR]', thumbnailImage= 'http://cdn.desktopwallpapers4.me/wallpapers/music/1366x768/1/6742-drum-and-bass-1366x768-music-wallpaper.jpg')
        li.setProperty('fanart_image', 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.video.allinone/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)


        xbmcplugin.endOfDirectory(addon_handle)

#----------------------------------radio----------------------------radio------------------------------radio-----------------------------radio------------------------------#

def RadioMenu():   #radio
        #setView('radio', 'radio-view')

        addon.add_directory({'mode': 'RadioMenu', '': '', '': '',
                             '': '', '': ''}, {'title':  '[COLOR lime]~~~~~~~[/COLOR][COLOR yellow][B].....WE ARE.....[/B][/COLOR] [COLOR red][I][B](((LIVE)))[/B][/I][/COLOR] [COLOR yellow][B].....TheYids RADIO.....[/B][/COLOR][COLOR lime]~~~~~~~[/COLOR]'}, img=IconPath + 'radioty.png', fanart='http://geewall.com/mmc_uploads/6119-music-notes-wallpaper-37082.jpg')

        addon_handle = int(sys.argv[1])   # thanks to Android TV Boxes a member of xbmchub for this code thanks mate #
        xbmcplugin.setContent(addon_handle, 'audio')

        url = 'http://uk1-pn.webcast-server.net:8698'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Kool London[/B][/COLOR] >>          [COLOR lime](Drum n bass, jungle, oldskool hardcore)[/COLOR]', iconImage='http://s1.postimg.org/fko2kyu9b/icon.png', thumbnailImage= 'http://s1.postimg.org/fko2kyu9b/icon.png')
        li.setProperty('fanart_image', 'http://koollondon.com/images/stories/kool-timetable-september-2014.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://webstreamer.co.uk:41940/;'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Pure Music 247[/B][/COLOR] >>          [COLOR lime](House + much more)[/COLOR]', iconImage='http://puremusic247.com/images/dj-Copyedittest.gif', thumbnailImage= 'http://puremusic247.com/images/dj-Copyedittest.gif')
        li.setProperty('fanart_image', 'http://djautograph.com/wp-content/uploads/2013/10/House_Music_by_Labelrx.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://50.7.184.106:8631/listen.pls'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Central Radio UK[/B][/COLOR] >>          [COLOR lime](Dance + much more)[/COLOR]', iconImage='http://s13.postimg.org/jcdhx5pqf/image.png', thumbnailImage= 'http://s13.postimg.org/jcdhx5pqf/image.png')
        li.setProperty('fanart_image', 'http://www.mrwallpaper.com/wallpapers/Music-equipment.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://213.229.108.96/RTB'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Rough Tempo[/B][/COLOR] >>          [COLOR lime](Drum n bass, jungle, oldskool hardcore)[/COLOR]', iconImage='http://www.roughtempo.com/fbimage.jpg', thumbnailImage= 'http://www.roughtempo.com/fbimage.jpg')
        li.setProperty('fanart_image', 'http://i1.ytimg.com/vi/UwCoz9kGJAs/maxresdefault.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://176.31.239.83:9136/'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Deja Classic [/B][/COLOR] >>         [COLOR lime](oldskool, UK Garage, RnB, HipHop)[/COLOR]', iconImage='http://s2.postimg.org/eg7k51z3t/icon.png', thumbnailImage= 'http://s2.postimg.org/eg7k51z3t/icon.png')
        li.setProperty('fanart_image', 'http://s18.postimg.org/fnbfwgw3d/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://176.31.239.83:9041/'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]DejaVu Live [/B][/COLOR] >>          [COLOR lime](Urban, RnB, HipHop)[/COLOR]', iconImage='http://s2.postimg.org/eg7k51z3t/icon.png', thumbnailImage= 'http://s2.postimg.org/eg7k51z3t/icon.png')
        li.setProperty('fanart_image', 'http://s18.postimg.org/fnbfwgw3d/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://78.129.228.187:8008/;stream/1'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]House fm [/B][/COLOR] >>          [COLOR lime](House)[/COLOR]', iconImage='http://i1.sndcdn.com/artworks-000049756393-x4gokq-crop.jpg?435a760', thumbnailImage= 'http://i1.sndcdn.com/artworks-000049756393-x4gokq-crop.jpg?435a760')
        li.setProperty('fanart_image', 'http://www.strictlyhousefm.co.uk/wp-content/uploads/2012/10/strictly-house-6.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://shine879.internetdomainservices.com:8204/'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Shine879 [/B][/COLOR] >>          [COLOR lime](Drum n Bass, House, UK Garage)[/COLOR]', iconImage='https://lh4.ggpht.com/0rdHZ2GOZYeiDfo1jyuWzbiFa9VIHNulX8qvTgXG3bHWMxO28mrxxUrT2VYWeQgaU4k=w300', thumbnailImage= 'https://lh4.ggpht.com/0rdHZ2GOZYeiDfo1jyuWzbiFa9VIHNulX8qvTgXG3bHWMxO28mrxxUrT2VYWeQgaU4k=w300')
        li.setProperty('fanart_image', 'http://dnbvideo.ru/wp-content/uploads/2013/09/antinox-liquid-drum-n-bass-4-1080p-hq.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://178.32.222.61:8080/'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Flames radio [/B][/COLOR] >>          [COLOR lime](Funk, Reggae, RnB, Soul)[/COLOR]', iconImage='http://i1.sndcdn.com/artworks-000069969699-cvl43d-original.jpg?a0633e8', thumbnailImage= 'http://i1.sndcdn.com/artworks-000069969699-cvl43d-original.jpg?a0633e8')
        li.setProperty('fanart_image', 'http://www.disclosurenewsonline.com/wp-content/uploads/2014/01/burning-flames-yellow-fire1.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://typhoon.exequo.org:8000/rinseradio'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Rinse fm [/B][/COLOR] >>             [COLOR lime](Urban, RnB, HipHop)[/COLOR]', iconImage='http://s16.postimg.org/kdlyi29j9/icon.png', thumbnailImage= 'http://s16.postimg.org/kdlyi29j9/icon.png')
        li.setProperty('fanart_image', 'http://s7.postimg.org/u3877stpn/fanart.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://bbc.co.uk/radio/listen/live/r1x.asx'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]bbc 1xtra[/B][/COLOR] >>             [COLOR lime](Urban, RnB, HipHop)[/COLOR]', iconImage='http://www.madtechrecords.com/wp-content/uploads/2013/08/artworks-000014947132-lbebhn-original.jpg', thumbnailImage= 'http://www.madtechrecords.com/wp-content/uploads/2013/08/artworks-000014947132-lbebhn-original.jpg')
        li.setProperty('fanart_image', 'http://s23.postimg.org/5jq12phff/fanart.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://tx.whatson.com/icecast.php?i=kissnationallow.mp3'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Kiss 100[/B][/COLOR] >>           [COLOR lime](Dance, RnB, HipHop)[/COLOR]', iconImage='http://3.bp.blogspot.com/-x1AWbyHFGug/UGMUaprrDuI/AAAAAAAAAi8/fJrShXB1SrI/s1600/kissfm.gif', thumbnailImage= 'http://3.bp.blogspot.com/-x1AWbyHFGug/UGMUaprrDuI/AAAAAAAAAi8/fJrShXB1SrI/s1600/kissfm.gif')
        li.setProperty('fanart_image', 'http://336fcc281d9fb3480f2a-0af712088f38ef5910226b2ecb408482.r82.cf2.rackcdn.com/img-230-3-1366642376.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://media-ice.musicradio.com/CapitalXTRALondonMP3.m3u'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Capital Xtra[/B][/COLOR] >>           [COLOR lime](Dance, RnB, Urban)[/COLOR]', iconImage='http://www.musicweek.com/cimages/7ec1c3e8cda116edcba97d259933f288.jpg', thumbnailImage= 'http://www.musicweek.com/cimages/7ec1c3e8cda116edcba97d259933f288.jpg')
        li.setProperty('fanart_image', 'http://londonist.com/wp-content/uploads/2013/11/Capital-XTRA.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://193.27.42.226:8192/mosdir.mp3'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Ministry of Sound Radio[/B][/COLOR] >>           [COLOR lime](Dance, House, Drum n Bass)[/COLOR]', iconImage='http://i1.sndcdn.com/artworks-000070064884-tec6ir-original.jpg?f775e59', thumbnailImage= 'http://i1.sndcdn.com/artworks-000070064884-tec6ir-original.jpg?f775e59')
        li.setProperty('fanart_image', 'http://1.bp.blogspot.com/-pXdClkxvZu8/TleccVYC3EI/AAAAAAAAAic/A7aV-CrKcaU/s1600/Ministry-of-Sound.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://50.117.26.26:5448/'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Upper Echelon Radio[/B][/COLOR] >>        [COLOR yellow](US)[/COLOR] [COLOR lime](HipHop)[/COLOR]', iconImage='https://lh4.ggpht.com/TQuDn_5thkjgYupY294UbkBiri4lf8InlIa7_MRj8OVwWhZcVcTxiX0CZV6eF00u9lP1=w300', thumbnailImage= 'https://lh4.ggpht.com/TQuDn_5thkjgYupY294UbkBiri4lf8InlIa7_MRj8OVwWhZcVcTxiX0CZV6eF00u9lP1=w300')
        li.setProperty('fanart_image', 'http://i1.ytimg.com/vi/L8IU9C3xZCk/maxresdefault.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://powerhitz.powerhitz.com:5030'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Power Hitz[/B][/COLOR] >>        [COLOR yellow](US)[/COLOR] [COLOR lime](RnB, HipHop)[/COLOR]', iconImage='http://sfweb3.radioline.fr/covers/39322/logo196.png', thumbnailImage= 'http://sfweb3.radioline.fr/covers/39322/logo196.png')
        li.setProperty('fanart_image', 'http://w8themes.com/wp-content/uploads/2013/08/Musical-Wallpapers.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://209.105.250.73:8206'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Zmix 97[/B][/COLOR] >>        [COLOR yellow](US)[/COLOR] [COLOR lime](old school, HipHop, funk)[/COLOR]', iconImage='http://media-cache-ec0.pinimg.com/236x/d8/be/0b/d8be0ba53a350149e97eb0e643f5fd1f.jpg', thumbnailImage= 'http://media-cache-ec0.pinimg.com/236x/d8/be/0b/d8be0ba53a350149e97eb0e643f5fd1f.jpg')
        li.setProperty('fanart_image', 'http://prettyriveracademy.com/wp-content/uploads/2013/08/hiphop6.jpg.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://s9.myradiostream.com:4418'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Urban hitz radio[/B][/COLOR] >>        [COLOR yellow](US)[/COLOR] [COLOR lime](RnB, HipHop)[/COLOR]', iconImage='https://pbs.twimg.com/profile_images/3424721247/d1111dabf5fd05d86d7fadde2be2e956.png', thumbnailImage= 'https://pbs.twimg.com/profile_images/3424721247/d1111dabf5fd05d86d7fadde2be2e956.png')
        li.setProperty('fanart_image', 'http://upload.wikimedia.org/wikipedia/commons/8/87/The_official_Urban_Hitz_Radio_Logo_for_2013!.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://hot108jamz.hot108.com:4020'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Hot 108 jamz[/B][/COLOR] >>        [COLOR yellow](US)[/COLOR] [COLOR lime](HipHop)[/COLOR]', iconImage='http://i1.ytimg.com/i/DvfgG9q0DPIrVCfy6C-sFA/mq1.jpg?v=dbb2c7', thumbnailImage= 'http://i1.ytimg.com/i/DvfgG9q0DPIrVCfy6C-sFA/mq1.jpg?v=dbb2c7')
        li.setProperty('fanart_image', 'http://i1.sndcdn.com/artworks-000006705654-aw46p2-original.jpg?435a760')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://tuner.defjay.com:80/'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Def jay[/B][/COLOR] >>        [COLOR yellow](US)[/COLOR] [COLOR lime](RnB)[/COLOR]', iconImage='http://www.defjay.com/_img/_layout/boomboom.gif', thumbnailImage= 'http://www.defjay.com/_img/_layout/boomboom.gif')
        li.setProperty('fanart_image', 'http://www.defjay.de/_data/promo/logo_hg_schwarz.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://war.str3am.com:7550/'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Power 106 FM[/B][/COLOR] >>        [COLOR yellow](Jam)[/COLOR] [COLOR lime](Reggae)[/COLOR]', iconImage='http://i.img.co/radio/62/27/2762_290.png', thumbnailImage= 'http://i.img.co/radio/62/27/2762_290.png')
        li.setProperty('fanart_image', 'http://th03.deviantart.net/fs70/PRE/f/2010/344/3/6/rasta_wallpaper_by_ipwnpt-d34luim.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://war.str3am.com:7970'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Ragga Kings[/B][/COLOR] >>        [COLOR yellow](Jam)[/COLOR] [COLOR lime](Reggae, Dancehall)[/COLOR]', iconImage='http://static.rad.io/images/broadcasts/33/32/1922/w175.png', thumbnailImage= 'http://static.rad.io/images/broadcasts/33/32/1922/w175.png')
        li.setProperty('fanart_image', 'http://dubmarine.org/wp-content/uploads/2011/11/RaggakingsPodcast1111-INFRA.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://radio.bigupradio.com:8000/;.mp3'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Big up radio[/B][/COLOR] >>        [COLOR yellow](Jam)[/COLOR] [COLOR lime](Dancehall)[/COLOR]', iconImage='http://static.radio.fr/images/broadcasts/64/3d/3420/w175.png', thumbnailImage= 'http://static.radio.fr/images/broadcasts/64/3d/3420/w175.png')
        li.setProperty('fanart_image', 'http://2.bp.blogspot.com/-G59C17P6Rqo/UHDcmBFcucI/AAAAAAAAAFg/HOtnL0fiaJs/s1600/Jah1.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://radio.bigupradio.com:8013/;.mp3'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Big up radio[/B][/COLOR] >>        [COLOR yellow](Jam)[/COLOR] [COLOR lime](Dub)[/COLOR]', iconImage='http://www.pcwelt.de/images/1/0/7/6/5/3/1/f4735b397dcba707.jpeg', thumbnailImage= 'http://www.pcwelt.de/images/1/0/7/6/5/3/1/f4735b397dcba707.jpeg')
        li.setProperty('fanart_image', 'http://bigupradio.com/reggae/wp-content/uploads/2009/10/Reggae-Flag.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        url = 'http://radio.bigupradio.com:8029/;.mp3'
        li = xbmcgui.ListItem('[COLOR lightsteelblue][B]Big up radio[/B][/COLOR] >>        [COLOR yellow](Jam)[/COLOR] [COLOR lime](Reggaeton)[/COLOR]', iconImage='http://zvlastnistyl.cz/wp-content/uploads/2009/01/BUR_radio_tag.gif', thumbnailImage= 'http://zvlastnistyl.cz/wp-content/uploads/2009/01/BUR_radio_tag.gif')
        li.setProperty('fanart_image', 'http://0.static.wix.com/media/5013e42b6aea16dfd8af90d21b9e4ebb.wix_mp_512')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

        addon.add_directory({'mode': 'HelpMenu'}, {'title':  '[B][COLOR gold]if you like rave music install Rave player from TheYids REPO[/COLOR][/B]'}, img= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.audio.raveplayer/icon.png', fanart= 'https://raw.githubusercontent.com/TheYid/My-Repo/master/plugin.audio.raveplayer/fanart.jpg')
        addon.add_directory({'mode': 'RadioMenu', '': '', '': '',
                             '': '', '': ''}, {'title':  '[COLOR mediumvioletred]~~~~~~~[/COLOR][COLOR aqua][B]Please report any broken links to @TheYid009 on twitter[/B][/COLOR][COLOR mediumvioletred]~~~~~~~[/COLOR]'}, img=IconPath + 'radioty.png', fanart='http://geewall.com/mmc_uploads/6119-music-notes-wallpaper-37082.jpg')

        xbmcplugin.endOfDirectory(addon_handle)

#----------------------------sport------------------------------sport----------------------sport---------------------------sport------------------------------sport--------#

def SportMenu():   #sport
        addon.add_directory({'mode': 'GetTitles39a', 'section': 'ALL', 'url': BASE_URL39 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest Wrestling/MMA[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'wma.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles39', 'section': 'ALL', 'url': BASE_URL39 + 'category/weeklies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest WWE[/B][/COLOR]  [COLOR darkred](Wrestling Rulez) [/COLOR] >>'}, img=IconPath + 'wr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles39', 'section': 'ALL', 'url': BASE_URL39 + '/category/tna-wrestling/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest TNA[/B][/COLOR]  [COLOR darkred](Wrestling Rulez) [/COLOR] >>'}, img=IconPath + 'wr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles39', 'section': 'ALL', 'url': BASE_URL39 + '/category/roh/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest ROH[/B][/COLOR]  [COLOR darkred](Wrestling Rulez) [/COLOR] >>'}, img=IconPath + 'wr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles39', 'section': 'ALL', 'url': BASE_URL39 + '/category/ufcmma/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest MMA[/B][/COLOR]  [COLOR darkred](Wrestling Rulez) [/COLOR] >>'}, img=IconPath + 'wr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles39', 'section': 'ALL', 'url': BASE_URL39 + '/category/wwe-networks/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest WWE shows[/B][/COLOR]  [COLOR darkred](Wrestling Rulez) [/COLOR] >>'}, img=IconPath + 'wr1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles39', 'section': 'ALL', 'url': BASE_URL39 + '/category/pay-per-views/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest PPV[/B][/COLOR]  [COLOR darkred](Wrestling Rulez) [/COLOR] >>'}, img=IconPath + 'wr1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------movies ------------------------movies ---------------------------movies --------------------------movies -------------------------------movies -------#

def MovieMenu():   #movies 
        addon.add_directory({'mode': 'GetTitles38', 'section': 'ALL', 'url': BASE_URL38 + '/category/hollywood-movie-2014/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]New Released[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'reto.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR blue](OCW) [/COLOR]>>'}, img=IconPath + 'ocw.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles41', 'section': 'ALL', 'url': BASE_URL41 + '/Movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR chocolate](undergroundflix) [/COLOR]>>'}, img=IconPath + 'uf.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR khaki](myvideolinks.eu) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/',
                             #'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR salmon](WTT) [/COLOR]>>'}, img=IconPath + 'wtt.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'HqMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR royalblue](TV HQ) [/COLOR]>>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'ZmMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR plum](flixanity) [/COLOR]>>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'PutMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](Prime Flicks) [/COLOR]>>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'MovMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR lightslategray](ViooZ) [/COLOR]>>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'UvMenu'}, {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR floralwhite](Ultra-Vid) [/COLOR]>>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/hollywood-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles20', 'section': 'ALL', 'url': BASE_URL20 + '/category/hollywood/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest Movies[/B][/COLOR][COLOR darkorchid](World4UFree) [/COLOR]>>'}, img=IconPath + 'w4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/hollywood-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'WtMenu'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR lightsteelblue][B]International Movies Zone[/B][/COLOR] >>'}, img=IconPath + 'iz.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'RgMenu'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR mediumturquoise][B]Full HD Zone[/B][/COLOR] >>'}, img=IconPath + 'fhz1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------- flixanity movie-----------------------------------------------------------------------------------------#

def ZmMenu(): #flixanity
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movies/date',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR plum](flixanity) [/COLOR]>>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movies/favorites',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Box Office[/B][/COLOR] >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/featuredmovies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Featured movies[/B][/COLOR] >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movies/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]movies[/B] [/COLOR][COLOR teal](a/z)[/COLOR] >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles12', 'section': 'ALL', 'url': BASE_URL12 + '/movies/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]movies[/B] [/COLOR][COLOR teal](imdb)[/COLOR] >>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Categories' },  {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](Newest) [/COLOR]>>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Categories1' },  {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](IMDB rating) [/COLOR]>>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Categories2' },  {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](ABC) [/COLOR]>>'}, img=IconPath + 'fl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery6'},  {'title':  '[COLOR green][B]Search[/B][/COLOR] [COLOR plum]flixanity[/COLOR] >> '}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#-------------------------------------------------------------------------- tvhq movies ------------------------------------------------------------------------------------------------#

def HqMenu():   #tvhq
        addon.add_directory({'mode': 'GetTitles32', 'section': 'ALL', 'url': BASE_URL32 + '/movies/date/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR royalblue](TV HQ) [/COLOR]>>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32', 'section': 'ALL', 'url': BASE_URL32 + '/movies/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]movies[/B] [/COLOR][COLOR teal](imdb)[/COLOR] >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32', 'section': 'ALL', 'url': BASE_URL32 + '/movies/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]movies[/B] [/COLOR][COLOR teal](abc)[/COLOR] >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Categoriestvhq' },  {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](Newest) [/COLOR]>>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Categoriestvhq1' },  {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](IMDB rating) [/COLOR]>>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Categoriestvhq2' },  {'title':  '[COLOR deepskyblue][B]Movie Genre[/B][/COLOR] [COLOR teal](ABC) [/COLOR]>>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery5'},  {'title':  '[COLOR green][B]Search[/B][/COLOR] [COLOR royalblue](TV HQ) [/COLOR] >> '}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------------- primeflicks movie ------------------------------------------------------------------------------------#

def PutMenu():          # primeflicks
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movies/date/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Added [/B][/COLOR] >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movies/abc/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]ABC [/B][/COLOR] >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15', 'section': 'ALL', 'url': BASE_URL15 + '/movies/imdb_rating/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Top IMDB [/B][/COLOR] >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery9'},  {'title':  '[COLOR green][B]Search[/B][/COLOR] [COLOR royalblue](PrimeFlicks) [/COLOR] >> '}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------- HD zone movies -------------------------------------------------------------------------------------------------#

def RgMenu():  #HD zone
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/yify/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Yify[/B][/COLOR] [COLOR khaki](myvideolinks.eu) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/3-d-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]3D Movies[/B][/COLOR] [COLOR khaki](myvideolinks.eu) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/movies/bluray/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies bluray[/B][/COLOR] [COLOR khaki](myvideolinks.eu) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/hollywood-movie/english-yify-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Movies by Yify[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/hollywood-movie/english-3d-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]3D Movies[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles40', 'section': 'ALL', 'url': BASE_URL40 + '/category/hd/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Latest HD Movies[/B][/COLOR] [COLOR seagreen](uwatchfree) [/COLOR]>>'}, img=IconPath + 'uw3.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles40', 'section': 'ALL', 'url': BASE_URL40 + '/category/featured/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Featured Movies[/B][/COLOR] [COLOR seagreen](uwatchfree) [/COLOR]>>'}, img=IconPath + 'uw3.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#---------------------------------------------------------------------- inter zone movies -------------------------------------------------------------------------------------------------#

def WtMenu():   #world4ufree #m2k
        addon.add_directory({'mode': 'GetTitles30', 'section': 'ALL', 'url': BASE_URL30 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Spanish movies[/B][/COLOR] [COLOR blue](tupeliculashd) [/COLOR]>>'}, img= 'http://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/750px-Flag_of_Spain.svg.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Categoriesuwf' },  {'title':  '[COLOR cornflowerblue][B]Movie Genre[/B][/COLOR] [COLOR seagreen](uwatchfree) [/COLOR]>>'}, img=IconPath + 'uw3.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/bollywood',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Bollywood [/B][/COLOR] [COLOR lightslategray](ViooZ) [/COLOR] >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/hollywood-movie/english-movie-dual-audio/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Dual Audio[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/tamil-movie/tamil-hindi-dubbed-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Tamil hindi Dubbed[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/bollywood-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Bollywood[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles23', 'section': 'ALL', 'url': BASE_URL23 + '/category/tamil-movie/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Tamil[/B][/COLOR] [COLOR crimson](300mb movies4u) [/COLOR] >>'}, img=IconPath + 'm4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles20', 'section': 'ALL', 'url': BASE_URL20 + '/category/bollywood/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Bollywood [/B][/COLOR] [COLOR darkorchid](World4UFree) [/COLOR]>>'}, img=IconPath + 'w4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles20', 'section': 'ALL', 'url': BASE_URL20 + '/category/hindi-dubbed-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Hindi Dubbed [/B][/COLOR] [COLOR darkorchid](World4UFree) [/COLOR]>>'}, img=IconPath + 'w4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles20', 'section': 'ALL', 'url': BASE_URL20 + '/category/songs/indian-videos/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR cornflowerblue][B]Indian Music Videos [/B][/COLOR] [COLOR darkorchid](World4UFree) [/COLOR]>>'}, img=IconPath + 'w4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/hindi-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Hindi [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/hindi-dubbed/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Hindi Dubbed [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/malayalam-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Malayalam [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/tamil-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Tamil [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles21', 'section': 'ALL', 'url': BASE_URL21 + '/category/telugu-movies/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Telugu [/B][/COLOR] [COLOR lawngreen](movies2k.eu) [/COLOR]>>'}, img=IconPath + '2k.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------------ moviesviooz movies ----------------------------------------------------------------------------------#

def MovMenu():   #moviesviooz
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR lightslategray](ViooZ) [/COLOR]>>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hd-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'HD Movies >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/sci-Fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/sport',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/western',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles3', 'section': 'ALL', 'url': BASE_URL3 + '/category/hollywood/war',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 'vu1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#--------------------------------------------------------------------------- moviesUv ----------------------------------------------------------------------------------------#

def UvMenu():   #moviesUv
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Movies[/B][/COLOR] [COLOR floralwhite](Ultra-Vid) [/COLOR]>>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/new-on-bluray',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'HD Movies >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure>>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery drama >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/romance-movies',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/comedy/romantic-comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romantic comedy>>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/sci-fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci-fi >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/movies/family/holiday',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

####################################---tv---####################---tv---####################---tv---###########################---tv---##########################---tv---#####################################################

def TvMenu():       #tv
        addon.add_directory({'mode': 'GetTitles2a', 'url': BASE_URL12 + '/tv-shows/date'}, {'title':  '[COLOR darkorange][B]Latest Episodes[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'intvs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles', 'section': 'ALL', 'url': BASE_URL + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR blue](OCW) [/COLOR]>>'}, img=IconPath + 'ocw.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles41', 'section': 'ALL', 'url': BASE_URL41 + '/TV-Shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR chocolate](undergroundflix) [/COLOR]>>'}, img=IconPath + 'uf.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles1', 'section': 'ALL', 'url': BASE_URL1 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR salmon](ADL) [/COLOR]>>'}, img=IconPath + 'adl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles10', 'section': 'ALL', 'url': BASE_URL10 + '/category/tv-shows/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR goldenrod](HD) [/COLOR][COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR khaki](MyVideoLinks) [/COLOR]>>'}, img=IconPath + 'mvl1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'TsuMenu'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR darkorange](shows4u) [/COLOR]>>'}, img=IconPath + 's4u1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Hq4Menu'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR royalblue](TV HQ) [/COLOR]>>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'PuttvMenu'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR teal](Prime Flicks) [/COLOR]>>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'TzmMenu'}, {'title':  '[COLOR orange][B]Full Seasons[/B][/COLOR] [COLOR plum](flixanity) [/COLOR]>>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles14', 'section': 'ALL', 'url': BASE_URL14 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Episodes list[/B][/COLOR] [COLOR tomato](ChannelCut) [/COLOR]>>'}, img=IconPath + 'cc.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'GetTitles4', 'section': 'ALL', 'url': BASE_URL4 + '/category/tv',
                             #'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR darkorange][B]Latest Episodes[/B][/COLOR] [COLOR floralwhite](Ultra-Vid) [/COLOR]>>'}, img=IconPath + 'uv1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#----------------------------------------------------------------------flixanitytv-------------------------------------------------------------------------------------------#

def TzmMenu():  #flixanitytv
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-shows/date',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Latest added[/B][/COLOR] >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-shows/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Top IMDB[/B][/COLOR] >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-shows/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]ABC[/B][/COLOR] >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tzm1Menu'}, {'title':  '[COLOR orange][B]Tv Show Genre[/B][/COLOR] [COLOR peru](Top IMDB) [/COLOR]>>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tzm3Menu'}, {'title':  '[COLOR orange][B]Tv Show Genre[/B][/COLOR] [COLOR peru](ABC) [/COLOR]>>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tzm2Menu'}, {'title':  '[COLOR orange][B]Tv Show Genre[/B][/COLOR] [COLOR peru](Newest) [/COLOR]>>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tzm1Menu():
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/adventure/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/animation/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/comedy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/crime/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/drama/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/documentary/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/fantasy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/family/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/horror/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/kids/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Kids >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/music/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/mystery/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/romance/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/reality-tv/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality Tv >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/sci-fi/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/sport/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/thriller/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/war/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/talk-show/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Talk Show >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/wwf-wwe/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Wwf - Wwe >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tzm2Menu():
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/family',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/kids',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Kids >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/music',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/mystery',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/reality-tv',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality Tv >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/sci-fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/sport',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/war',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/talk-show',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Talk Show >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/wwf-wwe',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Wwf - Wwe >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tzm3Menu():
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/adventure/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/animation/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/comedy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/crime/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/drama/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/documentary/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/fantasy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/family/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/horror/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/kids/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Kids >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/music/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/mystery/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/romance/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/reality-tv/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality Tv >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/sci-fi/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/sport/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/thriller/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/war/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/talk-show/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Talk Show >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles27a', 'section': 'ALL', 'url': BASE_URL12 + '/tv-tags/wwf-wwe/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Wwf - Wwe >>'}, img=IconPath + 'fl.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

#------------------------------------------------------------------------tvshows4u---------------------------------------------------------------------------------------#

def TsuMenu():  #tvshows4u
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-shows',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Latest added[/B][/COLOR] [COLOR darkorange](shows4u) [/COLOR]>>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-shows/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]Top IMDB[/B][/COLOR] >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-shows/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR orange][B]ABC[/B][/COLOR] >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tsu2Menu'}, {'title':  '[COLOR orange][B]Tv Show Genre[/B][/COLOR] [COLOR peru](Newest 1st) [/COLOR]>>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tsu1Menu'}, {'title':  '[COLOR orange][B]Tv Show Genre[/B][/COLOR] [COLOR peru](Top IMDB 1st) [/COLOR]>>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Tsu3Menu'}, {'title':  '[COLOR orange][B]Tv Show Genre[/B][/COLOR] [COLOR peru](ABC) [/COLOR]>>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tsu1Menu():
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/action/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/adventure/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/animation/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/comedy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/crime/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/drama/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/documentary/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/fantasy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/family/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/horror/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/kids/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Kids >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/music/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/mystery/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/romance/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/reality-tv/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality Tv >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/sci-fi/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/sport/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/thriller/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/war/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/talk-show/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Talk Show >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/western/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tsu2Menu():
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/family',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/kids',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Kids >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/music',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/mystery',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/reality-tv',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality Tv >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/sci-fi',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/sport',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/war',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/talk-show',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Talk Show >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/western',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Tsu3Menu():
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/action/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/adventure/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/animation/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/comedy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/crime/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/drama/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/documentary/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/fantasy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/family/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/horror/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/kids/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Kids >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/music/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Music >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/mystery/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/romance/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/reality-tv/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality Tv >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/sci-fi/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sci Fi >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/sport/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Sport >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/thriller/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/war/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'War >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles28a', 'section': 'ALL', 'url': BASE_URL29 + '/tv-tags/western/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Western >>'}, img=IconPath + 's4u.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

###-------------------------------------------------------------------primeflicks----------------------------------------------------------------------------------------#

def PuttvMenu():          # primeflicks tv
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-shows/date/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Added [/B][/COLOR] >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-shows/abc/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]ABC [/B][/COLOR] >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-shows/imdb_rating/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Top IMDB [/B][/COLOR] >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Put1Menu'}, {'title':  '[COLOR deepskyblue][B]TV Shows Genre[/B][/COLOR] [COLOR teal](Latest added) [/COLOR]>>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'Put2Menu'}, {'title':  '[COLOR deepskyblue][B]TV Shows Genre[/B][/COLOR] [COLOR teal](IMDB rating) [/COLOR]>>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'Put3Menu'}, {'title':  '[COLOR deepskyblue][B]TV Shows Genre[/B][/COLOR] [COLOR teal](A/Z) [/COLOR]>>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Put1Menu():          # primeflicks tv
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/-documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/cooking-food',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Cooking - Food >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/family',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/mystery',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/news',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'News >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/reality-tv',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality-tv >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/thriller-',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Put2Menu():          # primeflicks tv imdb
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/-documentary/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/action/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/adventure/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/animation/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/comedy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/cooking-food/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Cooking - Food >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/crime/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/drama/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/family/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/fantasy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/horror/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/mystery/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/news/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'News >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/reality-tv/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality-tv >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/romance/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/thriller-/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Put3Menu():          # primeflicks tv abc
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/-documentary/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/action/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/adventure/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/animation/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/comedy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/cooking-food/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Cooking - Food >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/crime/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/drama/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/family/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/fantasy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/horror/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/mystery/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/news/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'News >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/reality-tv/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality-tv >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/romance/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles15b', 'section': 'ALL', 'url': BASE_URL15 + '/tv-tags/thriller-/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'fm1.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))


#----------------------------------------------------------------------------TVHQ---------------------------------------------------------------------------------------#

def Hq4Menu():          # tvhq tv
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-shows/date/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Latest Added [/B][/COLOR] >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-shows/abc/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]ABC [/B][/COLOR] >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-shows/imdb_rating/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]Top IMDB [/B][/COLOR] >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'Hq5Menu'}, {'title':  '[COLOR deepskyblue][B]TV Shows Genre[/B][/COLOR] [COLOR teal](Latest added) [/COLOR]>>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'Hq6Menu'}, {'title':  '[COLOR deepskyblue][B]TV Shows Genre[/B][/COLOR] [COLOR teal](IMDB rating) [/COLOR]>>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png') 
        addon.add_directory({'mode': 'Hq7Menu'}, {'title':  '[COLOR deepskyblue][B]TV Shows Genre[/B][/COLOR] [COLOR teal](A/Z) [/COLOR]>>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png') 
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Hq5Menu():          # hqtv tv
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/documentary',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/action',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/adventure',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/animation',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/comedy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/cooking-food',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Cooking - Food >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/crime',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/drama',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/family',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/fantasy',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/horror',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/mystery',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/news',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'News >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/reality-tv',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality-tv >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/romance',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/thriller',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Hq6Menu():          # tvhq tv imdb
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/-documentary/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/action/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/adventure/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/animation/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/comedy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/cooking-food/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Cooking - Food >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/crime/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/drama/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/family/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/fantasy/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/horror/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/mystery/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/news/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'News >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/reality-tv/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality-tv >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/romance/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/thriller/imdb_rating',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

def Hq7Menu():          # tvhq tv abc
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/-documentary/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Documentary >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/action/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Action >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/adventure/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Adventure >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/animation/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Animation >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/comedy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Comedy >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/cooking-food/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Cooking - Food >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/crime/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Crime >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/drama/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Drama >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/family/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Family >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/fantasy/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Fantasy >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/horror/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Horror >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/mystery/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Mystery >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/news/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'News >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/reality-tv/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Reality-tv >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/romance/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Romance >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles32b', 'section': 'ALL', 'url': BASE_URL32 + '/tv-tags/thriller/abc',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  'Thriller >>'}, img=IconPath + 'tvhq.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

################################################################################searchmenu###############################################################################################

def SearchMenu():
        addon.add_directory({'mode': 'GetSearchQuery11'},  {'title':  '[COLOR khaki][B]M[/COLOR][COLOR blue]E[/COLOR][COLOR salmon]G[/COLOR][COLOR darkseagreen]A[/COLOR][/B] [COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR blue][B]HUB[/B][/COLOR] : [COLOR green]Search[/COLOR] (movies)'}, img=IconPath + 'mes.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery12'},  {'title':  '[COLOR khaki][B]M[/COLOR][COLOR blue]E[/COLOR][COLOR salmon]G[/COLOR][COLOR darkseagreen]A[/COLOR][/B] [COLOR blue][B]E[/B][/COLOR]ntertainment [COLOR blue][B]HUB[/B][/COLOR] : [COLOR green]Search[/COLOR] (tv episodes)'}, img=IconPath + 'mes.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2a', 'url': BASE_URL12 + '/tv-shows/date'}, {'title':  '[COLOR darkorange][B]Latest Episodes[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'intvs.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles39a', 'section': 'ALL', 'url': BASE_URL39 + '/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR lemonchiffon][B]Latest Wrestling/MMA[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'wma.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles38', 'section': 'ALL', 'url': BASE_URL38 + '/category/hollywood-movie-2014/',
                             'startPage': '1', 'numOfPages': '1'}, {'title':  '[COLOR cornflowerblue][B]New Released[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'reto.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetTitles2', 'url': BASE_URL12 + '/movies/favorites'}, {'title':  '[COLOR cornflowerblue][B]Featured[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'inf.png', fanart=FanartPath + 'fanart.png')
        #addon.add_directory({'mode': 'GetTitles2', 'url': BASE_URL12 + '/featuredmovies'}, {'title':  '[COLOR cornflowerblue][B]Box office[/B] [/COLOR]: [COLOR greenyellow]Index Search[/COLOR]'}, img=IconPath + 'isbo.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery6'},  {'title':  '[COLOR plum][B]flixanity[/B][/COLOR] : (movie) [COLOR green]Search[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery5'},  {'title':  '[COLOR royalblue][B]TV HQ[/B][/COLOR] : (movie) [COLOR green]Search[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        addon.add_directory({'mode': 'GetSearchQuery9'},  {'title':  '[COLOR royalblue][B]PrimeFlicks[/B][/COLOR] : (movie) [COLOR green]Search[/COLOR]'}, img=IconPath + 'searches.png', fanart=FanartPath + 'fanart.png')
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

########################################################################search#################################################################################################

##------------------------------------------------ tvhq ----------------------------------------------------------------------------------------------------------------##

def GetSearchQuery5():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search5(query)
	else:
                return
def Search5(query):
        url = 'http://www.tvhq.info/index.php?menu=search&query='+query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('img-preview spec-border.+?src=".+?src=(.+?)&amp;.+?".+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
        for img, url, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title}, img=img, fanart=FanartPath + 'fanart.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##--------------------------------------------------------------- flixanity ------------------------------------------------------------------------------------------##

def GetSearchQuery6():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search flixanity[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search6(query)
	else:
                return
def Search6(query):
        url = 'http://www.flixanity.com/index.php?menu=search&query=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="span-24">\s*?<h1>Movie results for:  "(.+?)"</h1>\s*?<div class="clear"></div>\s*?<ul class="span-24">\s*?<div class="span-6 inner-6 tt  view">\s*?<div class="item" style="text-align:center">\s*?<a href="(.+?)" class="spec-border-ie" title="">\s*?<img class="img-preview spec-border show-thumbnail"  src=".+?src=(.+?)&amp;.+?" alt=" " />', re.DOTALL).findall(html)
        for title, url, img in match:
                addon.add_directory({'mode': 'GetLinks1a', 'url': url}, {'title':  title}, img=img, fanart=FanartPath + 'fanart.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##----------------------------------------------------------- primeflicks ------------------------------------------------------------------------------------------##

def GetSearchQuery9():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search [/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search9(query)
	else:
                return
def Search9(query):
        url = 'http://primeflicks.me/index.php?menu=search&query='+query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('img-preview spec-border.+?src=".+?src=(.+?)&amp;.+?".+?href="(.+?)".+?>(.+?)<.+?', re.DOTALL).findall(html)
        for img, url, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title}, img= img, fanart=FanartPath + 'fanart.png')
	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##------------------------------------------------------------- mega movie search-------------------------------------------------------------------------------------------##

def GetSearchQuery11():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search11(query)
	else:
                return
def Search11(query):
    try:
        url = 'http://oneclickwatch.org/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="title"><a href="(.+?)".+?>(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR blue]...(OCW)[/COLOR]'}, img=img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry OneClickWatch is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://myvideolinks.eu/index.php?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="archive">\s*?<a href="(.+?)" rel="bookmark" title=".+?"> <img src="(.+?)" title="(.+?)" class="alignleft" alt=".+?" /></a>', re.DOTALL).findall(html)
        for url, img, title in match:
                addon.add_directory({'mode': 'GetLinks7', 'url': url}, {'title':  title + ' [COLOR gold]...(MVL)[/COLOR]'}, img=img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry myvideolinks is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://300mbmovies4u.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="cover"><a href="(.+?)".+?.+?<img src="(.+?)".+?alt="(.+?)"', re.DOTALL).findall(html)
        for url, img, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR crimson]...(300mb movies4u)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry 300mbmovies4u is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://rlssource.net/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>', re.DOTALL).findall(html)
        for movieUrl, title in match:
                addon.add_directory({'mode': 'GetLinks10', 'url': movieUrl}, {'title':  title + ' [COLOR firebrick]...(rlssource)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry rlssource is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://undergroundflix.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h1 class="entry-title"><a href="(.+?)" rel="bookmark">(.+?)</a></h1>', re.DOTALL).findall(html)
        for movieUrl, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title + ' [COLOR chocolate]...(Undergroundflix)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry rls1click is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://1-linkmovies.com/index.php?s='+query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('video-baslik.+?href="(.+?)".+?>(.+?)<.+?src=.+?', re.DOTALL).findall(html)
        for url, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR aqua]...(1-linkmovies)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry 1-linkmovies is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://moviesall4u.com/?s='+query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>', re.DOTALL).findall(html)
        for url, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR lime]...(moviesall4u)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry moviesall4u is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://www.srmovie.com/?s='+query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="post-box-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>\s*?<p class="post-meta">\s*?<span>.+?</span>\s*?</p>\s*?<div class="post-thumbnail">\s*?<a href=".+?" title=".+?" rel="bookmark">\s*?<img width=".+?" height=".+?" src="(.+?)"', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR yellow]...(srmovie)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry srmovie is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://www.filestube.to/query.html?q='+ query + '&select=mkv'
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('target="_blank" rel="nofollow" href=".+?"><span id="/video/(.+?)">.+?</span></a>', re.DOTALL).findall(html)
        for url in match:
                addon.add_directory({'mode': 'GetLinks', 'url': 'http://www.filestube.to/video/' + url}, {'title': url.replace('-', ' ').replace('.html', ' ') + ' [COLOR lavender](filetube)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry filetube search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##------------------------------------------------------------- mega tv search-------------------------------------------------------------------------------------------##

def GetSearchQuery12():
	last_search = addon.load_data('search')
	if not last_search: last_search = ''
	keyboard = xbmc.Keyboard()
        keyboard.setHeading('[COLOR green]Search[/COLOR]')
	keyboard.setDefault(last_search)
	keyboard.doModal()
	if (keyboard.isConfirmed()):
                query = keyboard.getText()
                addon.save_data('search',query)
                Search11(query)
	else:
                return
def Search12(query):
    try:
        url = 'http://oneclickwatch.org/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="title"><a href="(.+?)".+?>(.+?)<.+?src="(.+?)"', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR blue]...(OCW)[/COLOR]'}, img=img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry OneClickWatch is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://awesomedl.ru/?s=' + query 
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>\s*?<div class="postmeta-primary">\s*?<span class="meta_date">.+?</span> <span class="meta_categories">.+?<a href=".+?" rel="tag">.+?</a></span>\s*?</div>\s*?<img width="280" src="(.+?)" class="alignleft" alt="" />').findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR salmon]...(ADL)[/COLOR]'}, img= img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry watchthetapes is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://myvideolinks.eu/index.php?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="archive">\s*?<a href="(.+?)" rel="bookmark" title=".+?"> <img src="(.+?)" title="(.+?)" class="alignleft" alt=".+?" /></a>', re.DOTALL).findall(html)
        for url, img, title in match:
                addon.add_directory({'mode': 'GetLinks7', 'url': url}, {'title':  title + ' [COLOR gold]...(MVL)[/COLOR]'}, img=img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry myvideolinks is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://rlssource.net/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h2 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h2>', re.DOTALL).findall(html)
        for movieUrl, title in match:
                addon.add_directory({'mode': 'GetLinks10', 'url': movieUrl}, {'title':  title + ' [COLOR firebrick]...(rlssource)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry rlssource is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://undergroundflix.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h1 class="entry-title"><a href="(.+?)" rel="bookmark">(.+?)</a></h1>', re.DOTALL).findall(html)
        for movieUrl, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': movieUrl}, {'title':  title + ' [COLOR chocolate]...(Undergroundflix)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry rls1click is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://www.filestube.to/query.html?q='+ query + '&select=mkv'
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('target="_blank" rel="nofollow" href=".+?"><span id="/video/(.+?)">.+?</span></a>', re.DOTALL).findall(html)
        for url in match:
                addon.add_directory({'mode': 'GetLinks', 'url': 'http://www.filestube.to/video/' + url}, {'title': url.replace('-', ' ').replace('.html', ' ') + ' [COLOR lavender](filetube)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry filetube search is down [/B][/COLOR],[COLOR olive][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://www.channelcut.tv/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<h1 class="entry-title"><a href="(.+?)" title=".+?" rel="bookmark">(.+?)</a></h1>', re.DOTALL).findall(html)
        for url, title in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR orange]...(CC)[/COLOR]'}, img= 'https://raw.githubusercontent.com/TheYid/yidpics/8333f2912d71cc7ddd71a7cee9714dfe263ee543/icons/nopic.png', fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry channelcut is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))
    try:
        url = 'http://watchfullepisode.com/?s=' + query
        url = url.replace(' ', '+')
        print url
        html = net.http_GET(url).content
        match = re.compile('<div class="galleryitem" id=".+?">\s*?<a href="(.+?)" rel="bookmark" title=".+?">\s*?<img alt="(.+?)" src="(.+?)" />', re.DOTALL).findall(html)
        for url, title, img in match:
                addon.add_directory({'mode': 'GetLinks', 'url': url}, {'title':  title + ' [COLOR powderblue]...(watchfullepisode)[/COLOR]'}, img=img, fanart=FanartPath + 'fanart.png')
    except:
        xbmc.executebuiltin("XBMC.Notification([COLOR red][B]Sorry watchfullepisode is down [/B][/COLOR],[COLOR blue][B]Please try later[/B][/COLOR],7000,"")")
       	xbmcplugin.endOfDirectory(int(sys.argv[1]))

##.replace('/', ' ')## \s*? ##
###################################################################################### setViews ##########################################################################

def setView(content, viewType):

	if content:
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if addon.get_setting('auto-view') == 'true':
		xbmc.executebuiltin("Container.SetViewMode(%s)" % addon.get_setting(viewType) )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
	xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )

##############################################################################################################################################################################

if mode == 'main': 
	MainMenu()
elif mode == 'HelpMenu':
        HelpMenu()
elif mode == 'GetTitles': 
	GetTitles(section, url, startPage, numOfPages)
elif mode == 'GetTitles1': 
	GetTitles1(section, url, startPage, numOfPages)
elif mode == 'GetTitles2': 
	GetTitles2(query)
elif mode == 'GetTitles2a': 
	GetTitles2a(query)
elif mode == 'GetTitles3': 
	GetTitles3(section, url, startPage, numOfPages)
elif mode == 'GetTitles4': 
	GetTitles4(section, url, startPage, numOfPages)
elif mode == 'GetTitles10': 
	GetTitles10(section, url, startPage, numOfPages)
elif mode == 'GetTitles12': 
	GetTitles12(section, url, startPage, numOfPages)
elif mode == 'GetTitles12a': 
	GetTitles12a(section, url, startPage, numOfPages)
elif mode == 'GetTitles14': 
	GetTitles14(section, url, startPage, numOfPages)
elif mode == 'GetTitles15': 
	GetTitles15(section, url, startPage, numOfPages)
elif mode == 'GetTitles15a': 
	GetTitles15a(section, url, startPage, numOfPages)
elif mode == 'GetTitles15b': 
	GetTitles15b(section, url, startPage, numOfPages)
elif mode == 'GetTitles16': 
	GetTitles16(section, url, startPage, numOfPages)
elif mode == 'GetTitles20': 
	GetTitles20(section, url, startPage, numOfPages)
elif mode == 'GetTitles21': 
	GetTitles21(section, url, startPage, numOfPages)
elif mode == 'GetTitles23': 
	GetTitles23(section, url, startPage, numOfPages)
elif mode == 'GetTitles25': 
	GetTitles25(section, url, startPage, numOfPages)
elif mode == 'GetTitles27': 
	GetTitles27(section, url, startPage, numOfPages)
elif mode == 'GetTitles27a': 
	GetTitles27a(section, url, startPage, numOfPages)
elif mode == 'GetTitles28': 
	GetTitles28(section, url, startPage, numOfPages)
elif mode == 'GetTitles28a': 
	GetTitles28a(section, url, startPage, numOfPages)
elif mode == 'GetTitles30': 
	GetTitles30(section, url, startPage, numOfPages)
elif mode == 'GetTitles30a': 
	GetTitles30a(section, url, startPage, numOfPages)
elif mode == 'GetTitles30b': 
	GetTitles30b(section, url, startPage, numOfPages)
elif mode == 'GetTitles30c': 
	GetTitles30c(section, url, startPage, numOfPages)
elif mode == 'GetTitles30d': 
	GetTitles30d(section, url, startPage, numOfPages)
elif mode == 'GetTitles31': 
	GetTitles31(section, url, startPage, numOfPages)
elif mode == 'GetTitles31a': 
	GetTitles31a(section, url, startPage, numOfPages)
elif mode == 'GetTitles32': 
	GetTitles32(section, url, startPage, numOfPages)
elif mode == 'GetTitles32a': 
	GetTitles32a(section, url, startPage, numOfPages)
elif mode == 'GetTitles32b': 
	GetTitles32b(section, url, startPage, numOfPages)
elif mode == 'GetTitles34': 
	GetTitles34(section, url, startPage, numOfPages)
elif mode == 'GetTitles35': 
	GetTitles35(url)
elif mode == 'GetTitles35a': 
	GetTitles35a(url)
elif mode == 'GetTitles37': 
	GetTitles37(url)
elif mode == 'GetTitles38': 
	GetTitles38(section, query, startPage, numOfPages)
elif mode == 'GetTitles39': 
	GetTitles39(section, url, startPage, numOfPages)
elif mode == 'GetTitles39a': 
	GetTitles39a(section, url, startPage, numOfPages)
elif mode == 'GetTitles40': 
	GetTitles40(section, url, startPage, numOfPages)
elif mode == 'GetTitles41': 
	GetTitles41(section, url, startPage, numOfPages)
elif mode == 'Categories':
        Categories(url)
elif mode == 'Categories1':
        Categories1(url)
elif mode == 'Categories2':
        Categories2(url)
elif mode == 'Categoriestvhq':
        Categoriestvhq(url)
elif mode == 'Categoriestvhq1':
        Categoriestvhq1(url)
elif mode == 'Categoriestvhq2':
        Categoriestvhq2(url)
elif mode == 'Categoriesuwf':
        Categoriesuwf(url)
elif mode == 'GetLinks':
	GetLinks(section, url)
elif mode == 'GetLinks1':
	GetLinks1(section, url)
elif mode == 'GetLinks1a':
	GetLinks1a(section, url)
elif mode == 'GetLinks5':
	GetLinks5(section, url)
elif mode == 'GetLinks7':
	GetLinks7(section, url)
elif mode == 'GetLinks8':
	GetLinks8(section, url)
elif mode == 'GetLinks9':
	GetLinks9(url)
elif mode == 'GetLinks10':
	GetLinks10(section, url)
elif mode == 'GetLinks11':
	GetLinks11(section, url)
elif mode == 'GetLinks12':
	GetLinks12(section, url)
elif mode == 'GetLinks12a':
	GetLinks12a(section, url)
elif mode == 'GetLinks14':
	GetLinks14(section, url)
elif mode == 'GetSearchQuery9':
	GetSearchQuery9()
elif mode == 'Search9':
	Search9(query)
elif mode == 'GetSearchQuery5':
	GetSearchQuery5()
elif mode == 'Search5':
	Search5(query)
elif mode == 'GetSearchQuery6':
	GetSearchQuery6()
elif mode == 'Search6':
	Search6(query)
elif mode == 'GetSearchQuery11':
	GetSearchQuery11()
elif mode == 'Search11':
	Search11(query)
elif mode == 'GetSearchQuery12':
	GetSearchQuery12()
elif mode == 'Search12':
	Search12(query)
elif mode == 'PlayVideo':
	PlayVideo(url, listitem)
elif mode == 'PlayVideo1':
	PlayVideo1(url, listitem)	
elif mode == 'PlayVideo2':
	PlayVideo2(url, listitem)
elif mode == 'PlayVideo4':
	PlayVideo4(url, listitem)	
elif mode == 'PlayVideo5':
	PlayVideo5(url, listitem)
elif mode == 'ResolverSettings':
        urlresolver.display_settings()
elif mode == 'SearchMenu':
        SearchMenu()
elif mode == 'MovieMenu':
        MovieMenu()
elif mode == 'TvMenu':
        TvMenu()
elif mode == 'MusicMenu':
        MusicMenu()
elif mode == 'MovMenu':
        MovMenu()
elif mode == 'UvMenu':
        UvMenu()
elif mode == 'WtMenu':
        WtMenu()
elif mode == 'ZmMenu':
        ZmMenu()
elif mode == 'RgMenu':
        RgMenu()
elif mode == 'OmpMenu':
        OmpMenu()
elif mode == 'SportMenu':
        SportMenu()
elif mode == 'OmpazMenu':
        OmpazMenu()
elif mode == 'TzmMenu':
        TzmMenu()
elif mode == 'Tzm1Menu':
        Tzm1Menu()
elif mode == 'Tzm2Menu':
        Tzm2Menu()
elif mode == 'Tzm3Menu':
        Tzm3Menu()
elif mode == 'PutMenu':
        PutMenu()
elif mode == 'PuttvMenu':
        PuttvMenu()
elif mode == 'Put1Menu':
        Put1Menu()
elif mode == 'Put2Menu':
        Put2Menu()
elif mode == 'Put3Menu':
        Put3Menu()
elif mode == 'RadioMenu':
        RadioMenu()
elif mode == 'TvsMenu':
        TvsMenu()
elif mode == 'Tvs1Menu':
        Tvs1Menu()
elif mode == 'TsuMenu':
        TsuMenu()
elif mode == 'Tsu1Menu':
        Tsu1Menu()
elif mode == 'Tsu2Menu':
        Tsu2Menu()
elif mode == 'Tsu3Menu':
        Tsu3Menu()
elif mode == 'HqMenu':
        HqMenu()
elif mode == 'Hq4Menu':
        Hq4Menu()
elif mode == 'Hq5Menu':
        Hq5Menu()
elif mode == 'Hq6Menu':
        Hq6Menu()
elif mode == 'Hq7Menu':
        Hq7Menu()
elif mode == 'Help':
    import helpbox
    helpbox.HelpBox()

xbmcplugin.endOfDirectory(int(sys.argv[1]))