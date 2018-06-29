# -*- coding: utf-8 -*-
### Reseration Webpage info

import os
import fileread
# import login
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


# getReservationInfo() from fileread module, returns array [court,time,name,email,mobile]
infoArray = fileread.getReservationInfo('info.txt')
# loginInfoArray = fileread.getLoginInfo('login.txt')

# court and time info
url = "https://booking.naver.com/booking/12/bizes/105398/items/"+ infoArray[0] + "/slots/" + infoArray[1] +"?area=bns"

# begin chrome options
chrome_options = Options()

# chrome_options.add_argument("--headless"), By OS
chrome_options.add_argument("--window-size=1920x1080")

if os.name =='nt':
	browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver.exe')
else :
	browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver')

browser.get(url)

# get information(email,name,phonenumber) from reserveInfo
while True:
	try:
		# wait until the page is loaded
		element = WebDriverWait(browser, 5).until(lambda x: x.find_element_by_id('tel') 
			and x.find_element_by_class_name('service_info_dsc')
			and x.find_element_by_id('name')
			and x.find_element_by_name('email'))
		# element = WebDriverWait(browser, 5).until(lambda y: y.find_element_by_class_name('service_info_dsc'))
		serviceInfo = browser.find_element_by_class_name('service_info_dsc').text
		if u'잔여 1' in serviceInfo:
			break
		# if not available, refresh()
		browser.refresh()
	except Exception as e:
		print e
		break

# complete the form
browser.find_element_by_id('tel').send_keys(infoArray[4])
browser.find_element_by_id('name').send_keys(infoArray[2])
browser.find_element_by_name('email').send_keys(infoArray[3])
# click the agree all button
browser.find_element_by_class_name('chk_txt').click()
# submit the form and return the result
browser.find_element_by_class_name('btn').click()

input("press enter to close")