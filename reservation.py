### Reseration Webpage info

import fileread
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


# getReservationInfo() from fileread module, returns array [court,time,name,email,mobile]
infoArray = fileread.getReservationInfo('info.txt')

# court and time info
url = "https://booking.naver.com/booking/12/bizes/105398/items/"+ infoArray[0] + "/slots/" + infoArray[1] +"?area=bns"


# begin chrome options
chrome_options = Options()

# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver')
browser.get(url)

# wait until the page is loaded
try:
	element = WebDriverWait(browser, 5).until(
	    lambda x: x.find_element_by_id('tel'))
except Exception as e :
	print e
	pass

# get information(email,name,phonenumber) from reserveInfo
try:
	browser.find_element_by_id('tel').send_keys(infoArray[4])
	browser.find_element_by_id('name').send_keys(infoArray[2])
	browser.find_element_by_name('email').send_keys(infoArray[3])
except Exception as e :
	print e
	pass

# click the agree all button
browser.find_element_by_class_name('chk_txt').click()

# submit the form and return the result
browser.find_element_by_class_name('btn').click()