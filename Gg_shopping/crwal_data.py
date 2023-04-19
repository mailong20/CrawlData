from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import numpy as np
import cv2
import requests
import urllib
import uuid
from threading import Thread
from selenium.webdriver.common.by import By
import requests 
import bs4 
  
driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
# Generating the url  
number_page = 10
i = 0
while i<5:
	url = f"https://shopping.google.com/search?tbm=shop&q=hoodie&start={i*60}"
	print(url)
	i +=1
	driver.get(url)
	list_product = driver.find_elements(By.XPATH, "//div[@role='listitem']")
	for list_pt in list_product:
		div_a = list_pt.find_elements(By.TAG_NAME, 'a')
		try:
			div_click = div_a[1].click()
		except:
			pass
		time.sleep(1)
	tag_imgs = driver.find_elements(By.TAG_NAME, "img")
	print(len(tag_imgs))
	for tag_img in tag_imgs:
		class_img = tag_img.find_element(By.XPATH, "..").get_attribute('class').split('  ')
		print(tag_img.find_element(By.XPATH, "..").get_attribute('class'))
		# print(class_img)
		if len(class_img) == 2:
			url = tag_img.get_attribute('src')

			if 's512' in url:
				print(url)
				s = requests.Session()
				# Set correct user agent
				selenium_user_agent = driver.execute_script("return navigator.userAgent;")
				s.headers.update({"user-agent": selenium_user_agent})

				for cookie in driver.get_cookies():
				    s.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])
				response = s.get(url)
				image = np.asarray(bytearray(response.content), dtype="uint8")
				image = cv2.imdecode(image, cv2.IMREAD_COLOR)
				cv2.imwrite(f'hoodie/{uuid.uuid4()}.png', image)







