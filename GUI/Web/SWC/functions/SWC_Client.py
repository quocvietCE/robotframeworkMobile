#!/usr/bin/python
# Python default packages used in this lib.

import unittest
import sys
import os
import time,datetime,inspect
import logging
import PyPDF2
import subprocess
from GUI.Web.SWC.pom import MeetNowPage
from GUI.Clients.main_function import Clients
from GUI.Utility import Utility
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium.webdriver.common.touch_action import TouchAction
from logs import configure_log
from threading import Thread
# from urllib2 import URLError
# from itertools import izip
from itertools import zip_longest as zip
from robotbackgroundlogger import BackgroundLogger
import os.path
from os import path
from pathlib import Path
# Get framework base path from environment variable
# which is set in user .basrhrc file.

base_path = os.environ['PHOENIX_BASE_PATH']
# Lib PATH SET
sys.path.append(base_path+'MAIN/GUI/')
sys.path.append(base_path+'MAIN/CLI/logger/1.0.0.478_0.crx')
sys.path.append(base_path+'MAIN/GUI/')

log_info = Utility.Utility().log_infor
logger_main = configure_log(logging.DEBUG, __name__)
logger = configure_log(logging.DEBUG, __name__)
logger_bg = BackgroundLogger()

class SWC(unittest.TestCase):
    def __init__(self, client, browser):
        self.client_ip = client.get('host')
        self.client_port = '4444'
        self.browser = browser
        self.main_window = "null"
        self.detach_window = "null"
        self.conference_window = "null"
        self.platform = client.get('platform')
        self.meeting_id = ""
        self.screenshot_dir = client.get('screenshot_dir') 
        self.subimage = client.get('subimage') 
        self.subimage_branding = base_path+'MAIN/GUI/Utility/BRANDING_IMAGE/'
        self.appInstance = False
        self.powerpoint_instance = False
        self.point          = None
        self.result_parallel_execute = None
        self.driver_platform = Clients.Clients(client)
        self.file_download = None
        self.time_start_schedule_meeting = None

    def prepare_webdriver(self):
        '''
            * Function name: prepare_webdriver 
            * Description: This function is used to create web driver
            * Parameters:  None    
            * Author: Hao Nguyen
            * Date: Sep, 2019
            * Ex: prepare_webdriver  
            * Modify by: 
        '''
        if self.browser in 'chrome':       
            logger.info('Select chrome browser %s' %self.client_ip)
            profile_temp = webdriver.ChromeOptions()
            profile_temp.accept_untrusted_cert = True
            self.cap = profile_temp.to_capabilities()
            self.cap['goog:loggingPrefs'] = { 'browser':'ALL' }
            self.driver = webdriver.Remote(command_executor='http://'+self.client_ip+':'+self.client_port+'/wd/hub',desired_capabilities=self.cap)                
            logger.info('Webdriver is ready')
            return True
        elif self.browser == 'firefox':
            logger.info('Select Firefox browser %s' %self.client_ip)
            profile_dir = self.get_profile()
            profile_temp = webdriver.FirefoxProfile(profile_dir)
            profile_temp.set_preference("media.navigator.permission.disabled", 1)
            profile_temp.native_events_enabled = True
            profile_temp.assume_untrusted_cert_issuer=False
            profile_temp.set_preference("browser.helperApps.neverAsk.openFile","text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml")
            self.cap = DesiredCapabilities.FIREFOX
            self.cap["firefox_profile"] = profile_temp.encoded
            self.cap['acceptSslCerts'] = True
            self.cap['loggingPrefs'] = { 'browser':'ALL' }
            self.driver = webdriver.Remote(command_executor='http://'+self.client_ip+':'+self.client_port+'/wd/hub',desired_capabilities=self.cap)
            logger.info('Handle open tab firefox browser')
            self.driver.get("about:preferences") 
            time.sleep(2)
            if Utility.Utility().click_element_by_css(self.driver, "checkbox#linkTargeting",0):
                logger.info('Webdriver is ready')
                return True
            else:
                self.fail('Fail to click on checkbox open on tab')
        elif self.browser == 'edge':
            logger.info('Select Chromium Edge browser %s' %self.client_ip)
            self.cap = DesiredCapabilities.EDGE
            self.cap["version"] = "10"
            self.cap['platform'] = "WINDOWS"
            self.driver = webdriver.Remote(command_executor='http://'+self.client_ip+':'+self.client_port+'/wd/hub',desired_capabilities=self.cap)
            return True
        elif self.browser == 'ie':
            logger.info('Select Internet Explorer browser')
            self.cap = DesiredCapabilities.INTERNETEXPLORER
            self.driver = webdriver.Remote(command_executor='http://'+self.client_ip+':'+self.client_port+'/wd/hub',desired_capabilities=self.cap)
            return True
        elif self.browser == "safari":
            logger.info('Select Safari browser')
            self.cap=DesiredCapabilities.SAFARI
            self.driver = webdriver.Remote(command_executor='http://'+self.client_ip+':'+self.client_port+'/wd/hub',desired_capabilities=self.cap)
            return True
        else:
            self.fail('invalid browser')   


    def get_profile(self):
        if self.platform in 'win':
            if self.browser in 'chrome':        
                logger.info('Select Profile chrome browser %s' %self.client_ip)
                profile_path = ''
            elif self.browser == 'firefox':
                logger.info('Select Profile Firefox browser  %s' %self.client_ip)
                profile_path = base_path+"MAIN/GUI/Utility/HaoNVA_WIN_FF"
                logger.info('Profile path :%s' %profile_path)
            elif self.browser == 'edge':
                logger.info('Select Edge browser')
                profile_path = ''
            else:
                self.fail('invalid browser')
        elif self.platform in 'mac':
            if self.browser in 'chrome':
                logger.info('Select chrome browser %s' %self.client_ip)
                profile_path = ''
            elif self.browser in 'firefox':
                logger.info('Select Profile Firefox browser  %s' %self.client_ip)
                profile_path = base_path+"MAIN/GUI/Utility/HaoNVA_MAC_FF"
                logger.info('Profile path :%s' %profile_path)            
            elif self.browser in 'edge':
                logger.info('Select Edge browser')
                profile_path = ''
            else:
                self.fail('invalid browser')
        else:
            self.fail('invalid platform')
        return profile_path

    def launch_browser(self, url=None, title_web=None):
        try:
            log_info(self.client_ip, self.client_port, inspect.stack()[0][3])
            if self.point != None and self.point.is_alive():
                logger = logger_bg
                logger.info('Status is sub thread so log background will be write after back to main thread')
            else:
                logger = logger_main
            logger.info('Web Address:   %s' % url)
            self.driver_platform.launch_app()
            self.prepare_webdriver()
            self.driver.get(url)
            self.driver.set_page_load_timeout(30)
            self.driver.switch_to.default_content()
            self.driver.maximize_window()
            self.main_window = self.driver.current_window_handle
            logger.info('%s' % self.main_window)
            WebDriverWait(self.driver, 10).until(EC.title_contains(title_web))
            title_current = self.driver.title
            logger.info('Title: %s' % title_current)
            if not title_web:
                logger.info('Launch_browser susccessfuly')
                return True
            if title_web.lower() in title_current.lower():         
                self.driver_platform.active_screen(self.browser)
                logger.info('Launch_browser susccessfuly')
                return True
            self.fail('Goto %s failed, please check network' % url)
        except:
            raise RuntimeError('Function exception: '+str(sys.exc_info()))

    def close_browser(self):
        try:
            log_info(self.client_ip, self.client_port, inspect.stack()[0][3])
            logger.info('Start function close_browser')
            self.driver.quit()
            return True
        except:
            raise RuntimeError('Function exception: '+str(sys.exc_info()))

