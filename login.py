#-*-coding:utf8-*-

import os
import json
import time
import fileread

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait



class NaverLogin:
	def getCommonNaverLoginCookie(self, url, USERID, PASSWD, closeIt):
		# begin chrome options
		chrome_options = Options()
		# chrome_options.add_argument("--headless"), By OS
		chrome_options.add_argument("--window-size=1920x1080")
		if os.name =='nt':
			driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver.exe')
		else :
			driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver')
		driver.get(url)
		element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_name('id') and x.find_element_by_name('pw')) 
		driver.find_element_by_name('id').send_keys(USERID)
		driver.find_element_by_name('pw').send_keys(PASSWD)
		driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
		
		cookies = driver.get_cookies()
		if closeIt:
			driver.close()
			driver.quit()
		# print 'result: ' ,  cookies
		return cookies

if __name__ == "__main__":
	infoArray = fileread.getLoginInfo('login.txt')
	login = NaverLogin()
	cookies = login.getCommonNaverLoginCookie(infoArray[0],infoArray[1],infoArray[2], True)
