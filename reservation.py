### Reseration Webpage info

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from urlparse import urlparse


# Court Number Array
courtNumbers = {
	'3' : '2633373',
	'4' : '2652587',
	'5' : '2652589',
	'6' : '2652590',
	'7' : '2652591',
	'8' : '2652592',}

# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver')
browser.get(site)
delay = 3 # seconds

browser.implicitly_wait(delay)

# wait until the page is loaded
element = WebDriverWait(browser, 1).until(
    lambda x: x.find_element_by_id('tel'))

# get information(email,name,phonenumber) from reserveInfo
email = browser.find_element_by_id('tel').send_keys(reserveInfo['phoneNumber'])
email = browser.find_element_by_id('name').send_keys(reserveInfo['name'])
username = browser.find_element_by_name('email').send_keys(reserveInfo['email'])

# click the agree all button
browser.find_element_by_class_name('chk_txt').click()

# submit the form and return the result
browser.find_element_by_class_name('btn').click()

#Changes Monthly, hard to get it, serverside app.
slotNumbers = '1234567'

# court and time info
site = "https://booking.naver.com/booking/12/bizes/105398/items/"+ courtNumbers['4'] + "/slots/" + slotNumber +"?area=bns"

print "proceed reservation for" + site

## info class needed for reservation

reserveInfo = {
	'name' : 'test',
	'email' : 'test@gmail.com',
	'phoneNumber' : '010-3222-2223',
	}

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver')
browser.get(site)
delay = 3 # seconds

browser.implicitly_wait(delay)

# wait until the page is loaded
element = WebDriverWait(browser, 1).until(
    lambda x: x.find_element_by_id('tel'))

# get information(email,name,phonenumber) from reserveInfo
email = browser.find_element_by_id('tel').send_keys(reserveInfo['phoneNumber'])
email = browser.find_element_by_id('name').send_keys(reserveInfo['name'])
username = browser.find_element_by_name('email').send_keys(reserveInfo['email'])

# click the agree all button
browser.find_element_by_class_name('chk_txt').click()

# submit the form and return the result
browser.find_element_by_class_name('btn').click()


# Get Confirmation Number (if Success) or Reservation Fail Code