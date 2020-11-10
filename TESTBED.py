#!/usr/bin/python


#Python default packages used in this lib.
import  sys, os, unittest

##Get framework base path from environment variable
##which is set in user .basrhrc file.
base_path	= os.environ['PHOENIX_BASE_PATH']

##Lib PATH SET
sys.path.append(base_path+'MAIN')
sys.path.append(base_path+'MAIN/GUI/Web')
sys.path.append(base_path+'MAIN/GUI/Web/SWC/')
sys.path.append(base_path+'MAIN/GUI/Web/SWC/functions')
sys.path.append(base_path+'MAIN/GUI/Utility')
sys.path.append(base_path+'MAIN/CONFIG')
sys.path.append(base_path+'MAIN/GUI/Clients')
sys.path.append(base_path+'MAIN/GUI/Clients/main_function')
sys.path.append(base_path+'MAIN/GUI/Clients/Utility')
libPath=os.path.join(base_path, 'MAIN/GUI/Clients/')
files	= [f for f in os.listdir(libPath) if f.endswith("y.py")]

for f in files:
	execfile(os.path.join(libPath, f)) 

import logging
from logs import configure_log
#from logs import BackgroundLogger
logger = configure_log(logging.DEBUG, 'SETUP TCs')
#logger = BackgroundLogger()
#logger.configure_log(logging.DEBUG, __name__)

sys_fedramp_mode = {
	'web_portal': 'https://esg172.hcm.com:443/portal',
	'iview_address'		: 'https://10.103.3.20/iview/views/index.jsf',
	'iview_username'	: 'admin',
	'iview_password' 	: 'RAPtor_1234%123456',
	'ext_prefix': '43',
	'auto_config' :'http://10.102.2.58/hfs/auto_conf_fedramp_mode.txt',
}

http_server 		= 'http://10.102.2.58/hfs/'
auto_config_TE		= http_server+'SMGR151/'
screenshot_directory= base_path+'MAIN/LOGS/screenshots/'
subimage			= base_path+'MAIN/GUI/Utility/subimage.png'
user_password 		= 'RAPtor1234'
meeting_pin 		= '123456'
moderator_pin 		= '1234567'
browser_chrome 		= 'chrome'
platform_win 		= 'win'
platform_mac 		= 'mac'
FileShare 			= "000FileShare"
internal_server_address	= "s4b-fe.equinoxsv.com"
external_server_address	= "s4b-fe.equinoxsv.com"
web_title = 'Avaya Equinox'
prefix= sys_mtt_view126['ext_prefix']

###################################### WIN ####################################
win_3 = {	#AEW, SFB
	"host": "10.102.1.117",
	#"host": "10.128.224.204",
	"port": "9999",
	"platform": "win",
	"screenshot_dir" : screenshot_directory,
	"subimage" : subimage
}


###################################### MAC ####################################
mac_1 = {	#AEM, SWC, AEI
	"host": "10.102.1.102",
	"port": "4622",
	"platform": "mac",
	"screenshot_dir" : screenshot_directory,
	"subimage" : subimage
}

###################################### IOS ####################################

ios_1 = {
	"ip": "10.102.1.109",
	"host": "10.102.1.104",
	"port": "4723",
	"platform": "aei",
	"xcodeorgid": 'R4M7A967VG',
	"udid": "e344155913ca64b64e0f3963c1f89817b1eae496",
	"screenshot_dir" : screenshot_directory,
	"subimage" : subimage
}



#################################### ANDROID ###################################
android_1 = {
	"ip": "10.102.1.62",
	"host": "10.102.1.30",
	"port": "4723",
	"platform": "aea",
	"udid": "215d1b04630d7ece",
	"screenshot_dir" : screenshot_directory,
	"subimage" : subimage
}
# user_2006000 = {'username' : 'auto2006000','user_pass':'RAPtor1234','virtual_room':prefix+'2006000'}
# user_2006001 = {'username' : 'auto2006001','user_pass':'RAPtor1234','virtual_room':prefix+'2006001'}






