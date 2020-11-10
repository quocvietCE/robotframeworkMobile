#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Python default packages used in this lib.
import sys,os,time,logging
base_path = os.environ['PHOENIX_BASE_PATH']
##Lib PATH SET
sys.path.append(base_path+'MAIN/GUI/')
sys.path.append(base_path+'MAIN/CLI/logger/')

##Get framework base path from environment variable
##which is set in user .basrhrc file.

# from itertools import izip
# from urllib2 import URLError
from itertools import zip_longest as zip
from logs import configure_log
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from GUI.IX_Workplace.Utility import AXPath ,Utility

logger = configure_log(logging.DEBUG, __name__)

class AccountPage():
    '''
        This class defines all elements in Top Of Mind page
    '''
    def __init__(self):
        self.REMEMBER_PASSWORD_SW   = {
            "aea":  (By.ID, 'com.avaya.android.flare:id/remember_password_switch'),
            "aei":  (By.XPATH, '//XCUIElementTypeSwitch[@name="Remember Passwords"]')
        }
        self.SIGN_OUT_BTN   = {
            "aea":  (By.ID, 'com.avaya.android.flare:id/signout_button'),
            "aei":  (By.ID, 'Sign Out')
        }

        self.WORKPLACE_USERNAME_TF = {
            "win":  (By.ID, 'CommunicatorUsernameAutomationIdTextSettingTextBox')
        }

        self.WORKPLACE_PASSWORD_TF = {
            "win":  (By.ID, 'CommunicatorPasswordAutomationId')
        }


    def enter_workplace_username(self,driver,client,message):
        logger.info('Start enter_workplace_username')
        if Utility.Utility().wait_to_element_is_displayed(driver,*(self.WORKPLACE_USERNAME_TF.get(client)),6):
            Utility.Utility().send_keys_v2(driver,1,*(self.WORKPLACE_USERNAME_TF.get(client)),message)


    def enter_workplace_password(self,driver,client,message):
        logger.info('Start enter_workplace_password')
        Utility.Utility().send_keys_v2(driver,1,*(self.WORKPLACE_PASSWORD_TF.get(client)),message)

    def setting_workplace_account(self,driver,client,username,password):
        logger.info('Start setting_workplace_account')
        self.enter_workplace_username(driver,client,username)
        self.enter_workplace_password(driver,client,password)
        return True