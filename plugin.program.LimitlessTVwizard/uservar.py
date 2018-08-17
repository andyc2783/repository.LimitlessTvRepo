import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'Limitless Tv Wizard'
EXCLUDES       = [ADDON_ID]
# Text File with build info in it.
BUILDFILE      = 'https://www.dropbox.com/s/y7x22zbs90hpavq/build.zip'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'http://www.limitlesstv.xyz/v2/new-android-tvapp/Limitless%20CCTV(1.4)_to_publish.apk/'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = ''
YOUTUBEFILE    = 'http://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://www.limitlesstv.xyz/v2/mobile-androidapp/limitless-tv.apk'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'https://www.dropbox.com/s/mrus6ndaeqb4kq3/icon.png'
ICONMAINT      = 'https://www.dropbox.com/s/mrus6ndaeqb4kq3/icon.png'
ICONAPK        = 'https://www.dropbox.com/s/mrus6ndaeqb4kq3/icon.png'
ICONADDONS     = 'https://www.dropbox.com/s/mrus6ndaeqb4kq3/icon.png'
ICONYOUTUBE    = 'http://'
ICONSAVE       = 'https://www.dropbox.com/s/mrus6ndaeqb4kq3/icon.png'
ICONTRAKT      = 'http://'
ICONREAL       = 'http://'
ICONLOGIN      = 'https://www.dropbox.com/s/mrus6ndaeqb4kq3/icon.png'
ICONCONTACT    = 'https://www.dropbox.com/s/mrus6ndaeqb4kq3/icon.png'
ICONSETTINGS   = 'https://www.dropbox.com/s/mrus6ndaeqb4kq3/icon.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'Yes'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'dodgerblue'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I]([COLOR '+COLOR2+']LimitlessTV[/COLOR])[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing LimitlessTV Wizard.\r\n\r\nContact us on facebook at http://facebook.com'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'https://www.dropbox.com/s/mrus6ndaeqb4kq3/icon.png'
CONTACTFANART  = 'https://www.dropbox.com/s/z5vlcsn8rq3qgjx/fanart.jpg'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = ''
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = ''
# Url to folder zip is located in
REPOZIPURL     = ''
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'No'
# Url to notification file
NOTIFICATION   = ''
# Use either 'Text' or 'Image'
HEADERTYPE     = ''
HEADERMESSAGE  = ''
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = ''
#########################################################