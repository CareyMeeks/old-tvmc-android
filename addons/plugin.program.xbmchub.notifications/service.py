import xbmc,string,logging,array
import common as Common #from common import * #import common
## ################################################## ##
## ################################################## ##
## Start of program
TypeOfMessage="t"; (NewImage,NewMessage)=Common.FetchNews(); 
Common.CheckNews(TypeOfMessage,NewImage,NewMessage,True); 
## ################################################## ##
## ################################################## ##