#!/usr/bin/python

#Python default packages used in this lib.
import socket
import sys,os,time,logging,datetime

##Get framework base path from environment variable
##which is set in user .basrhrc file.

base_path = os.environ['PHOENIX_BASE_PATH']
##Lib PATH SET
sys.path.append(base_path+'MAIN/GUI/')
sys.path.append(base_path+'MAIN/CLI/logger/')

# from itertools import izip
# from urllib2 import URLError
from itertools import zip_longest as zip
from logs import configure_log
#from logs import BackgroundLogger
from robotbackgroundlogger import BackgroundLogger
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
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import Select
import random
import cv2
import numpy as np
import unittest
from GUI.Utility.MySocketConnection import MySocketConnection


# conenction timeout after 20 seconds
connect_timeout = 20

# receive data from client socket will timeout after 300 seconds
receive_timeout = 300


logger_main = configure_log(logging.DEBUG, __name__)
logger = configure_log(logging.DEBUG, __name__)
logger_bg = BackgroundLogger()


class Utility(unittest.TestCase):
	'''
		This class will help to support for client.
	'''
	def __init__(self):
		self.defaultImplicitTimeout_sec = 5
		#super.__init__()
		# logger.info("------------------Ultility Class")
	# def __del__(self):
	# 	logger.info("------------------Release Ultility Class")

	def send_key_enter(self, driver=None):
		try:
			ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
			logger.info("Pressed enter")
			return True
		except:
			logger.error('Exception '+str(sys.exc_info()))
			return False

	def send_key_control_a(self, driver=None):
		# not work with win 
		try:
			ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
			logger.info("Pressed control+a")
			return True
		except:
			logger.error('Exception '+str(sys.exc_info()))
			return False

	def send_key_backspace(self, driver=None):
		try:
			ActionChains(driver).send_keys(20 * Keys.DELETE).perform()
			logger.info('Press backspace')
			return True
		except:
			logger.error('Exception '+str(sys.exc_info()))
			return False

	def send_key_escape(self, driver=None):
		try:
			#ActionChains(driver).send_keys(20 * Keys.ESCAPE).perform()
			ActionChains(driver).send_keys(Keys.ESCAPE).perform()
			logger.info('Press espace')
			return True
		except:
			logger.error('Exception '+str(sys.exc_info()))
			return False

	def send_keys(self, driver=None, key_message=None, byselenium=1):
		try:
			logger.info('send_keys %s' %str(key_message))
			if byselenium==1:
				logger.info('Use method ActionChains-MoveAndClick')
				ActionChains(driver).send_keys(str(key_message)).perform()
			else:
				# For AEM client
				message = str(key_message)
				data = message.split(':')
				a = 0
				while(a < len(data)):
					ActionChains(driver).send_keys(data[a]).perform()
					a = a + 1
					if a < len(data):
						ActionChains(driver).key_down(Keys.SHIFT).send_keys(";").key_up(Keys.SHIFT).perform()
			logger.info('send_keys Succesfully')
			return True
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False

	def send_keys_v2(self, driver, by_framework,locator, element,key_message):
		try:
			logger.info('Send_keys %s' %str(key_message))
			if by_framework==1:
				logger.info('Use method click Selenium-Appium')
				url_textfield = driver.find_element(locator, element)
				url_textfield.click()
				url_textfield.clear()
				url_textfield.send_keys(key_message)
			elif by_framework==2:
				logger.info('Use method ActionChains-MoveAndClick')
				ActionChains(driver).send_keys(str(key_message)).perform()
			else:
				logger.info('Use method For AEM client')
				message = str(key_message)
				data = message.split(':')
				a = 0
				while(a < len(data)):
					ActionChains(driver).send_keys(data[a]).perform()
					a = a + 1
					if a < len(data):
						ActionChains(driver).key_down(Keys.SHIFT).send_keys(";").key_up(Keys.SHIFT).perform()
			logger.info('Send_keys Succesfully')
			return True
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False

	def click_element(self, driver=None, by_framework=1, locator=None, element=None):
		try:
			logger.info('Clicking element: %s' %element)
			if by_framework==1:
				logger.info('Use method click Selenium-Appium')
				driver.find_element(locator, element).click()
			elif by_framework == 2:
				logger.info('Use method ActionChains-MoveAndClick')
				found_element = driver.find_element(locator, element)
				time.sleep(1)
				actions = ActionChains(driver)
				actions.move_to_element(found_element)
				actions.click()
				actions.perform()
				actions.reset_actions()
			elif by_framework == 0:
				logger.info('Use method ActionChains-Click')
				found_element = driver.find_element(locator, element)
				time.sleep(1)
				actions = ActionChains(driver)
				actions.click(found_element)
				actions.perform()
				actions.reset_actions()
			else:
				#mobile unusal case
				logger.info('Use method click TouchAction')
				TouchAction(driver).tap(driver.find_element(locator, element)).perform()
			logger.info('Clicked on element')
			return True
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False
	
	def click_element1(self, driver=None, by_framework=1, element=None):
		try:
			logger.info('Clicking element')
			if by_framework==1:
				logger.info('Use method click Selenium-Appium')
				element.click()
			elif by_framework == 2:
				# move and click the mouse like a user
				logger.info('Use method ActionChains-MoveAndClick')
				actions = ActionChains(driver)
				actions.move_to_element(element)
				actions.click()
				actions.perform()
				actions.reset_actions()
			elif by_framework == 0:
				logger.info('Use method ActionChains-Click')
				actions = ActionChains(driver)
				actions.click(element)
				actions.perform()
				actions.reset_actions()
			else:
				#mobile unusal case
				logger.info('Use method click TouchAction')
				TouchAction(driver).tap(element).perform()
			logger.info('Clicked on element')
			return True
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False

	def double_click_element(self, driver=None, by_framework=1, locator=None, element=None):
		try:
			logger.info('Double Clicking element: %s' %element)
			if by_framework==1:
				logger.info('Use method click Selenium-Appium')
				driver.find_element(locator, element).click()
				driver.find_element(locator, element).click()
			elif by_framework == 0:
				logger.info('Use method ActionChains-Click')
				actions = ActionChains(driver)
				actions.double_click(driver.find_element(locator, element))
				actions.perform()
			elif by_framework == 2:
				# move and click the mouse like a user
				logger.info('Use method ActionChains-MoveAndClick')
				actions = ActionChains(driver)
				actions.move_to_element(driver.find_element(locator, element))
				actions.double_click()
				actions.perform()
			logger.info('Double Clicked on element')
			return True
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False

	def click_element_with_offset(self, driver=None, byselenium=2, xoffset=0, yoffset=0, locator=None, element=None):
		try:
			logger.info('Clicking element: %s' %element)
			if byselenium==1:
				driver.find_element(locator, element).click()
			else:
				# move and click the mouse like a user
				actions = ActionChains(driver)
				actions.move_to_element_with_offset(driver.find_element(locator, element), xoffset, yoffset).perform()
				actions.click()
				actions.perform()
			logger.info('Clicked on element')
			return True
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False
	
	def click_element_with_offset1(self, driver=None, byselenium=2, xoffset=0, yoffset=0, element=None):
		try:
			logger.info('Clicking element: %s' %element)
			if byselenium==1:
				element.click()
			else:
				# move and click the mouse like a user
				actions = ActionChains(driver)
				actions.move_to_element_with_offset(element, xoffset, yoffset).perform()
				actions.click()
				actions.perform()
			logger.info('Clicked on element')
			return True
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False

	def click_and_hold_element_move_to_offset(self, driver=None, byselenium=2, xoffset=0, yoffset=0, element=None):
		try:
			logger.info('Clicking element: %s' %element)
			if byselenium==1:
				element.click()
			else:
				# move and click the mouse like a user
				actions = ActionChains(driver)
				actions.move_to_element_with_offset(element, 0, 0).perform()
				actions.click_and_hold()
				actions.perform()
				actions.move_to_element_with_offset(element, xoffset, yoffset).perform()
			logger.info('Clicked on element')
			return True
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False

	def drag_and_drop_element_by_offset(self, driver=None, xoffset=0, yoffset=0, element=None):
		try:
			logger.info('Drag and drop element: %s' %element)
			# move and click the mouse like a user
			actions = ActionChains(driver)
			actions.drag_and_drop_by_offset(element, xoffset, yoffset).perform()
			logger.info('Did it base on element')
			return True
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False


	def check_exists_by_name(self, driver, name):
		try:
			logger.info('Start function check_exists_by_name')
			elements = driver.find_elements(By.NAME,name)
			if len(elements) > 0:
				#logger.info('Found element with name %s' %(name))
				return True
			#logger.info('Not found element with name %s' %(name))
			return False
		except:
			logger.error('There is an exception while performing check_exists_by_name')
			return False
			
	##### NOT WORK WITH MAC ######
	def check_exists(self, driver=None, locator=None, element=None):
		try:
			logger.info('Start function ')
			elements = driver.find_elements(locator ,element)
			if len(elements) > 0:
				logger.info('Found element %s' %(element))
				return True
			logger.info('Not found element %s' %(element))
			return False
		except WebDriverException as Ex:
			logger.info('Exception '+str(Ex))
			return False

	def wait_for_exists(self, driver=None, implicit_timeout_sec1=0, locator=None, element=None):
		try:
			logger.info('Checking element...%s' %element)
			wait = WebDriverWait(driver, implicit_timeout_sec1)
			wait.until(EC.visibility_of_element_located((locator, element)))
			logger.info('Found element %s' %(element))
			return True
		except:
			logger.info('Not found element %s' %(element))
			return False

	#   Convenience method to check existence immediately without using implicit timeout.
	#   returns: found element, or None
	def wait_for_exists_not_except(self, driver=None, implicit_timeout_sec1=0, locator=None, element=None):
		try:
			logger.info('Checking element...%s' %element)
			wait = WebDriverWait(driver, implicit_timeout_sec1)
			wait.until(EC.visibility_of_element_located((locator, element)))
			logger.info('Found element %s' %(element))
			elements = driver.find_elements(locator, element)
			if len(elements) > 0:
				return True
			logger.info('Not found element %s' %element)
			return False
		except:
			logger.info('Not found locator')
			return False


	#MAC prefer to use this function
	def check_exists_not_except(self, driver=None, locator=None, element=None):
		try:
			logger.info('Start function check_exists_not_except')
			elements = driver.find_elements(locator, element)
			if len(elements) > 0:
				logger.info('Found element %s' %(element))
				return True
			logger.info('Not found element %s' %(element))
			return False
		except :
			logger.info('Not found element %s' %(element))
			return False

	def wait_for_vanish(self, driver=None, implicit_timeout_sec1=10, locator=None, element=None):
		try:
			logger.info('Checking element...%s'%element)
			wait = WebDriverWait(driver, implicit_timeout_sec1)
			wait.until_not(EC.visibility_of_element_located((locator, element)))
			logger.info('element %s is vanish' %element)
			return True
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False

	def wait_for_presence(self, driver=None, implicit_timeout_sec1=20, locator=None, element=None):
		try:
			logger.info('Checking element...%s'%element)
			wait = WebDriverWait(driver, implicit_timeout_sec1)
			wait.until(EC.presence_of_element_located((locator, element)))
			logger.info('element %s is presentative' %element)
			return True
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False

	def wait_for_clickable(self, driver=None, implicit_timeout_sec1=20, locator=None, element=None):
		try:
			logger.info('Checking element...')
			wait = WebDriverWait(driver, implicit_timeout_sec1)
			wait.until(EC.element_to_be_clickable((locator, element)))
			logger.info('element %s is clickable' %element)
			return True
		except:
			logger.info('element %s is not clickable' %element)
			return False

	def wait_until_not_clickable(self, driver=None, implicit_timeout_sec1=20, locator=None, element=None):
		try:
			logger.info('Checking element...')
			wait = WebDriverWait(driver, implicit_timeout_sec1)
			wait.until_not(EC.element_to_be_clickable((locator, element)))
			logger.info('element %s is not clickable' %element)
			return True
		except WebDriverException as Ex:
			# logger.error('Exception '+str(Ex))
			return False

	def wait_for_text_of_element_is(self, driver=None, implicit_timeout_sec1=20, value=None, locator=None, element=None):
		try:
			logger.info('Checking value of element...')
			wait = WebDriverWait(driver, implicit_timeout_sec1)
			wait.until(EC.text_to_be_present_in_element((locator, element), value))
			logger.info('value %s is presentative' %value)
			return True
		except WebDriverException as Ex:
			# logger.error('Exception '+str(Ex))
			return False

	def wait_for_title_of_url_is(self, driver=None, implicit_timeout_sec1=20, value=None):
		try:
			logger.info('Checking value of element...')
			wait = WebDriverWait(driver, implicit_timeout_sec1)
			wait.until(EC.title_is(value))
			logger.info('title is %s' %value)
			return True
		except WebDriverException as Ex:
			# logger.error('Exception '+str(Ex))
			return False

	def wait_and_click_element(self, driver=None, implicit_timeout_sec1=20, locator=None, element=None):
		try:
			logger.info('wait and click to element... %s' %(element))
			wait = WebDriverWait(driver, implicit_timeout_sec1)
			wait.until(EC.element_to_be_clickable((locator, element))).click()
			return True
		except:
			logger.error('Exception '+str(sys.exc_info()))
			return False


	def move_to_element_with_offset(self, driver=None, xoffset=0, yoffset=0, locator=None, element=None):
		try:
			logger.info('checking_by_xpath %s' %(locator))
			# if self.check_exists(driver, locator, element):
			# 	logger.info('Found element')
			# else:
			# 	logger.info('Not found element')
			# 	return False
			logger.info('Hover element')
			element = driver.find_element(locator, element)
			ActionChains(driver).move_to_element_with_offset(element, xoffset, yoffset).perform()
			return True
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False
	
	def move_to_element_with_offset1(self, driver=None, xoffset=0, yoffset=0, element=None):
		try:
			logger.info('Hover element')
			ActionChains(driver).move_to_element_with_offset(element, xoffset, yoffset).perform()
			return True
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False

	def swipe_element(self, driver, xoffset=0, yoffset=0,  duration=800, locator=None, element=None):
		try:
			if self.check_exists(driver, locator, element):
					logger.info('Found element')
					elemnet = driver.find_elements(locator, element)
					elemnet_x = elemnet.location.x
					elemnet_y = elemnet.location.y
					logger.info('elemnet_x: %s' %elemnet_x)
					logger.info('elemnet_y: %s' %elemnet_y)
					driver.swipe(elemnet_x, elemnet_y, elemnet_x + xoffset, elemnet_y+ yoffset, duration)
					return True
			logger.info('Not found element')
			return True
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False

	def clear_text(self, driver=None, byselenium=1, locator=None, element=None):
		try:
			if byselenium == 1:
				driver.find_element(locator, element).clear()
			else:
				actions = ActionChains(driver)
				element = driver.find_element(locator, element)
				# actions.move_to_element_with_offset(element, 10, 10).perform()
				actions.double_click(element).perform()
				actions.send_keys(Keys.DELETE).perform()
			logger.info('Clear all text')
			return True
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False

	def get_text_by_element(self, driver=None, locator=None, element=None):
		try:
			if self.check_exists(driver, locator, element):
				return driver.find_element(locator, element).text
			else:
				logger.info('Not found element')
				return False
		except WebDriverException as Ex:
			logger.error('Exception '+str(Ex))
			return False



	def take_screenshot(self,driver=None, screenshot_directory=None, client_name=None, client_ip=None):
		try:
			logger.info('Taking screenshot...')
			screenshot_name = screenshot_directory+client_name+'-'+client_ip+'-'+str(datetime.datetime.now())+'.png'
			screenshot_name = screenshot_name.replace(" ","-").replace(":","-")
			logger.info('screenshot_name: '+str(screenshot_name))
			if driver.save_screenshot(screenshot_name):
				logger.info('Take screenshot successfully with path: '+screenshot_name)
				# Oct 30, 2019 - Tho add this line to support ADA
				logger.info('<'+ str(screenshot_name)+'>')
				return screenshot_name
			else:
				logger.info('Failed to take screenshot')
				return 'error'
		except WebDriverException as ex:
			logger.error('There is an exception while performing clean_up')
			logger.error('Exception '+str(ex))
			return False

	def log_infor(self, client_ip=None, client_port=None, function_name=None):
		try:
			logger.info('\n\n****************************** CONNECTION ******************************' )
			logger.info('====> Connected to %s on port %s' %(client_ip, client_port))
			logger.info('====> Command is sent : %s' %function_name)
			return True
		except:
			logger.error('Exception '+str(sys.exc_info()))
			return False

	def right_click_element(self, driver=None, locator=None, element=None):
		self.assertTrue(self.wait_for_exists(driver, locator, element, 2), 'Not found element')
		ActionChains(driver).context_click((locator, element)).perform()
		logger.info('Right click %s' %element)
		return True

	#   Convenience method to wait and click on xpath with configurable timeout (default = 10 seconds).
	#   return: True if click ok. False otherwise
	def wait_and_click_not_except(self, driver=None, time_out=10, locator=None, element=None):
		try:
			logger.info('wait_and_click_by_xpath ')
			logger.info('wait_and_click_by_xpath %s' %(element))
			wait = WebDriverWait(driver, time_out)
			wait.until(EC.visibility_of_element_located((locator, element))).click()
			return True
		except:
			logger.info('not found %s' %element)
			return False

