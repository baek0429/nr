# -*- coding: utf-8 -*-
### Reseration Webpage info

import os
import fileread
# import login
# import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


# getReservationInfo() from fileread module, returns array [court,time,name,email,mobile]
infoArray = fileread.getReservationInfo('info.txt')
loginInfoArray = fileread.getLoginInfo('login.txt')

# court and time info
url = "https://booking.naver.com/booking/12/bizes/105398/items/"+ infoArray[0] + "/slots/" + infoArray[1] +"?area=bns"

# get login url
loginUrl = loginInfoArray[0]

# begin chrome options
chrome_options = Options()

# chrome_options.add_argument("--headless"), By OS
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--incognito")

#open browser
if os.name =='nt':
	browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver.exe')
else :
	browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver')

# begin login
browser.get(loginUrl)

browser.implicitly_wait(3)
browser.find_element_by_name('id').send_keys(loginInfoArray[1])
browser.find_element_by_name('pw').send_keys(loginInfoArray[2])
browser.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()


while True:
	try:
		# go to reservation page
		browser.get(url)
		# wait until the page is loaded
		element = WebDriverWait(browser, 5).until(lambda x:
			x.find_element_by_class_name('service_info_dsc').text
			and x.find_element_by_class_name('chk_txt')
			and x.find_element_by_class_name('btn')
			and x.find_element_by_class_name('summary_wrap'))
		serviceInfo = browser.find_element_by_class_name('service_info_dsc').text
		if u'잔여 0' in serviceInfo:
			print serviceInfo.encode('utf-8')
			pass
		if u'잔여 1' in serviceInfo:
			print serviceInfo.encode('utf-8')
			browser.find_element_by_class_name('chk_txt').click()
			# submit the form and return the result
			browser.find_element_by_class_name('btn').click()
			break
		browser.refresh()
	except Exception as e:
		print e
		pass