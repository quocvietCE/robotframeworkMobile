#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python default packages used in this lib.

import sys
import os
import time
import logging

# Get framework base path from environment variable
# which is set in user .basrhrc file.

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
from selenium.webdriver.support.ui import Select
from GUI.Utility import Utility
from GUI.Web.SWC.pom import ConferencePage
import unittest

logger = configure_log(logging.DEBUG, "AlertPage")


class AlertPage(unittest.TestCase):
    def __init__(self):

        # Leave the meeting
        # Are you sure you want to leave this meeting?
        # self.CSS_ALERT_LEAVE_THE_MEETING = "div.db_body.ng-binding"
        self.CSS_ALERT_LEAVE_THE_MEETING = "div[class='confirm-modal ng-scope']"
        self.CSS_BTN_CLOSE = "button.ngdialog-close"
        # self.CSS_BTN_SUBMIT = "button[ng-click='dialogBox.model.submit()']"
        self.CSS_BTN_SUBMIT = "button.db_btn.ng-binding[name='confirmSubmit']"

        # remote control
        self.CSS_LABLE_CAMERA = "div.fecc_camera_name_label.ng-binding"
        self.CSS_BTN_UP = "g[ng-click*='app.swc.feccActionType.up']"
        self.CSS_BTN_DOWN = "g[ng-click*='app.swc.feccActionType.down']"
        self.CSS_BTN_LEFT = "g[ng-click*='app.swc.feccActionType.right']"
        self.CSS_BTN_RIGHT = "g[ng-click*='app.swc.feccActionType.left']"
        self.CSS_BTN_OUT = "div[ng-click*='app.swc.feccActionType.out']"
        self.CSS_BTN_IN = "div[ng-click*='app.swc.feccActionType.in_']"
        self.CSS_BTN_CLOSE_REMOTE_CONTROL = "div.db_close_btn"

        #Enter meeting pin"
        self.CSS_BTN_ENTER                  = "button.db_btn.ng-binding[name='moderatorPinEnter']"
        self.CSS_TF_ENTER_PIN        = "input[type='password']"

        #Knock the door
        self.CSS_ALERT_KNOCK            = "div#tooltipTarget"
        self.CSS_BTN_ADMIT              = "a[ng-click*='core.conferenceWrapper.acceptAll()']"
        self.CSS_BTN_DENY               = "a[ng-click*='core.conferenceWrapper.denyAll()']"
        self.CSS_CLOSE_POPUP_MUTED_DEFAULT  = "div[ng-click='dialogBox.model.cancel()']"
        #sharing system 9.1.9
        self.CSS_ALERT_DISMISS          = "button[ng-click='dialogBox.model.cancel()']"
        self.CSS_BTN_STOP_SHARING_HANDLE    = "button[name=confirmSubmit]"
        self.MUTED_POPUP = "div.muted_popup.ng-scope"

        self.ONE_TIME_PIN_POPUP = "form[class*='assign-pin-form']>label"
        self.ONE_TIME_PIN_INPUT = "form[class*='assign-pin-form']>input"
        self.ENTER_ONE_TIME_PIN_OPTION = "form[class*='assign-pin-form']>button[type='submit']"




    def click_btn_dismiss(self, driver):
        try:
            self.assertTrue(Utility.Utility().click_element_by_css(driver, self.CSS_ALERT_DISMISS), 'CLick on enter button failed')
            logger.info('Clicked on button enter')
            return True
        except:
            logger.error('Exception '+str(sys.exc_info()))
            return False
    
    def handle_alert_dismiss(self, driver):
        try:
            logger.info('Start function handle dismiss')
            self.click_btn_dismiss(driver)
            logger.info('Clicked button dismiss successfully')
            return True
        except:
            logger.error('Exception '+str(sys.exc_info()))
            return False
    