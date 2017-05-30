import xbmcaddon
import xbmcgui
from provider import *

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

provider = Provider()
kb = xbmc.Keyboard('Any link here')
kb.doModal()

url = provider.provide(kb.getText())
xbmc.Player().play(url)
	
