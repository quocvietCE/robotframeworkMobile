#!/usr/bin/python

# ********************************************************************
# This library mainly focused on Equinox Client with help of
# selenium remote webdriver.
# Author Dong Nguyen <nmdong@tma.com.vn>
# Date 30 Dec 2018
# *******************************************************************
# Get framework base path from environment variable
# which is set in user .basrhrc file.

import sys,os,time,logging,datetime,inspect
import clipboard

##Get framework base path from environment variable
##which is set in user .basrhrc file.

base_path = os.environ['PHOENIX_BASE_PATH']
##Lib PATH SET
sys.path.append(base_path+'MAIN/GUI/')
sys.path.append(base_path+'MAIN/CLI/logger/1.0.0.478_0.crx')

# from itertools import izip
# from urllib2 import URLError
from itertools import zip_longest as zip
from logs import configure_log
from appium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import Select
from threading import Thread
import unittest
from GUI.IX_Workplace.pom import AccountPage
from GUI.IX_Workplace.Utility import Utility, AXPath

from robotbackgroundlogger import BackgroundLogger
logger_main = configure_log(logging.DEBUG, __name__)
logger = configure_log(logging.DEBUG, __name__)
logger_bg = BackgroundLogger()
log_info = Utility.Utility().log_infor

class Clients(unittest.TestCase, object):
    def __init__(self, platform=None):
        self.driver         = None
        self.client_ip      = platform.get("host")
        self.client_port    = platform.get("port")
        self.client         = platform.get("platform")
        self.udid           = platform.get("udid")
        self.xcodeorgid     = platform.get("xcodeorgid")
        self.profile        = None
        self.screenshot_dir = platform.get('screenshot_dir')
        self.sharing_mode   = None
        self.powerpoint_instance = False
        self.outlook_instance = False
        self.driverapp      = None                              #pptx driver
        self.conference_window = None
        self.main_window    = "Avaya IX Workplace"
        self.subimage       = platform.get('subimage')
        self.point          = None
        self.result_parallel_execute = None
    try:
        driver_keeper
    except:
        driver_keeper = None

    def get_desired_capabilities(self):

        desired_capabilities_sfbw = {
            "debugConnectToRunningApp": True,
            "app": r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Namefile.exe",
            "--url-base":"wd/hub"
        }
        desired_capabilities_win = {
            "debugConnectToRunningApp": False,
            "app": r"C:\Program Files (x86)\Namefile.exe"
        }
        desired_capabilities_mac = {
            'platformName':'mac', 
            'deviceName':'ThoPham', 
            'browserName':'Chrome',  
            'commandDelay':500, 
            'loopDelay':1000, 
            'implicitTimeout':3000, 
            'mouseMoveSpeed':50, 
            "screenShotOnError":1,
            "--url-base":"wd/hub"
        }
        desired_capabilities_aea = {
            "browserName": "",
			"udid": self.udid,
            "platformVersion": "9",
			"deviceName":"Samsung devices",
			"platformName":"Android",
            "noReset":False,
            "automationName":"UiAutomator2",
			"appPackage": "nameApp",
			"appActivity":"nameAppActivity",
            "newCommandTimeout":"200000",
            #"newCommandTimeout":"300",
			"autoGrantPermissions":True,
            "systemPort":8220,
            "--url-base":"wd/hub"
        }
        desired_capabilities_aei = {
            "platformName": "iOS",
            "platformVersion": "10.1.1",
            "deviceName":"iPad",
            "xcodeOrgId": self.xcodeorgid,
            "xcodeSigningId": "iPhone Developer",
            "automationName": "XCUITest",
            "bundleId": "bundleApp",
            "udid": self.udid,
            "newCommandTimeout":"10000"
        }
        desired_capabilities_list= {
            "win": desired_capabilities_win,
            "mac": desired_capabilities_mac,
            "aea": desired_capabilities_aea,
            "aei": desired_capabilities_aei,
            "sfbw":desired_capabilities_sfbw
        }
        return desired_capabilities_list.get(self.client)

    def get_command_url(self):
        command_url ={
            "win":      'http://'+self.client_ip+':'+self.client_port,
            "mac":      'http://'+self.client_ip+':'+self.client_port,
            "aea":      'http://'+self.client_ip+':'+self.client_port+'/wd/hub',
            "aei":      'http://'+self.client_ip+':'+self.client_port+'/wd/hub',
            "sfbw":     'http://'+self.client_ip+':'+self.client_port
        }
        return command_url.get(self.client)


    def launch_app(self):
        try:
            log_info(self.client_ip, self.client_port, inspect.stack()[0][3])
            if self.point != None and self.point.is_alive():
                logger = logger_bg
                logger.info('Status is sub thread so log background will be write after back to main thread')
            else:
                logger = logger_main
            logger.info('Start function launch_app')
            desired_capabilities = self.get_desired_capabilities()
            logger.info('Desired_capabilities: %s'%(desired_capabilities))
            logger.info('Client_port: %s' %self.client_port)
            logger.info('Client: %s' %self.client)
            if self.client in "mac aei aea":
                self.driver = webdriver.Remote(command_executor=self.get_command_url(), desired_capabilities=desired_capabilities)
            else:
                if not InitPage.InitPage().check_driver_win_is_existed(self.driver_keeper): 
                    self.driver = webdriver.Remote(command_executor=self.get_command_url(), desired_capabilities=desired_capabilities)  
                    self.driver_keeper = self.driver
                    if Utility.Utility().wait_to_element_is_displayed(self.driver, *AlertPage.AlertPage().NO_BTN.get(self.client),15):
                        Utility.Utility().click_element(self.driver,1,*AlertPage.AlertPage().NO_BTN.get(self.client))
                else:
                    self.driver = self.driver_keeper
                    logger.info('Avaya Equinox already opened')
            if self.client in "win mac": 
                if self.client == "mac":
                    self.driver.get(self.main_window)
                logger.info('Verify launch_app desktop')
                logger.info(('Waiting to open equinox client on host: %s.') %(self.client_ip))
                current_window = self.driver.current_window_handle
                logger.info('current_window_handle: %s' %current_window)
                window_handles = self.driver.window_handles
                logger.info('window_handles: %s' %window_handles)
                if current_window != None and self.check_is_existed_ix_app():
                    logger.info(('Open window : %s') % (current_window))
                    return True
                else:
                    self.fail("AVAYA IX WORKPLACE is opened unsuccessfully")
            else:
                logger.info('Verify launch_app mobile')
                if self.client == 'aei' and Utility.Utility().wait_for_exists_not_except(self.driver, 10, *(AlertPage.AlertPage().ACCEPT_BTN.get(self.client))):
                    self.driver.find_element(*(AlertPage.AlertPage().ACCEPT_BTN.get(self.client))).click()
                    logger.info('clicked ACCEPT button')
                return True
        except:
            raise RuntimeError('Function exception: '+str(sys.exc_info()))


    def quit_app(self):
        log_info(self.client_ip, self.client_port, inspect.stack()[0][3])
        logger.info('Start function quit_app')
        try:
            self.driver.quit()
        except:
            logger.info('Function exception: '+str(sys.exc_info()))


