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

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
url = f"https://dosi-in.com/ao-khoac-c.31?type_category=male"
driver.get(url)
dem = 1000
while dem!=0:
		# Scroll down to bottom
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(0.6)
		dem-=1
list_product = driver.find_elements(By.XPATH, "//a[@class='product-item_img']")
print(len(list_product))
dict_imgs = {}
for div_item in list_product:
	src_img = div_item.find_elements(By.TAG_NAME, 'img')[0].get_attribute('src')
# 	print(src_img)
	if '320' in src_img:
		dict_imgs.setdefault(src_img.replace('w=320&h=320', 'w=670&h=670'), src_img.replace('w=320&h=320', 'w=670&h=670'))


for link_img, _ in dict_imgs.items():
	s = requests.Session()
	# Set correct user agent
	selenium_user_agent = driver.execute_script("return navigator.userAgent;")
	s.headers.update({"user-agent": selenium_user_agent})

	for cookie in driver.get_cookies():
	    s.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])
	response = s.get(link_img)
	image = np.asarray(bytearray(response.content), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	if image is None:
		print(link_img)
	else:
		cv2.imwrite(f'AOKHOAC/{uuid.uuid4()}.png', image)		







