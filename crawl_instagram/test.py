from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import numpy as np
import cv2
import os
import requests
from threading import Thread
from datetime import datetime
import pickle
import queue




class Instagram:
	def __init__(self):
		self.url_infors = ['https://www.instagram.com/vaan.ilu/','https://www.instagram.com/tayaraujomelo/']
		self.url_album = queue.LifoQueue()
		self.main()
		time.sleep(2)

	def get_information_album_from_url_infor(self, link_infor):
			op = webdriver.ChromeOptions()
			driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)
			driver = self.login(driver)
			dict_album = {}
			driver.get(link_infor)
			
			dem = 0
			last_height = len(dict_album)
			while True:
				main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'main[role="main"]')))
				tabel_abums = main.find_elements(By.CSS_SELECTOR, 'a[tabindex="0"]')
				
				for tabel_abum in tabel_abums:
					try:
						if 'https://www.instagram.com/p/' in tabel_abum.get_attribute('href'):
							dict_album.setdefault(tabel_abum.get_attribute('href'), tabel_abum)	
					except:
						pass
				driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				new_height = len(dict_album)
				if new_height == last_height:
					dem +=1
					if dem == 20:
						break
				else:
					dem = 0
				last_height = new_height
			print('Detected album: ', len(dict_album))
			self.url_album


	def login(self, driver):
		if os.path.exists('cookies.pkl'):
			driver.get('https://www.instagram.com/')
			cookies = pickle.load(open("cookies.pkl", "rb"))
			for cookie in cookies:
				driver.add_cookie(cookie)
			
		else:
			driver.get('https://www.instagram.com/')
			login_fb =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="button"]')))
			login_fb.click()
			username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[name="email"]'))).send_keys("")
			password = driver.find_element(By.CSS_SELECTOR, 'input[name="pass"]').send_keys("")
			login = driver.find_element(By.CSS_SELECTOR, 'button[name="login"]')
			login.click()
			alert = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div[role="dialog"]')))
			pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))
		
		return driver


	def get_url_img_by_album(self):
		self.driver.get('https://www.instagram.com/p/CmhOfqwy5he/')
		dict_url = {}
		
		while True:
			button_next = None
			article = self.waitdriver.until(EC.presence_of_element_located((By.CSS_SELECTOR,'article[role="presentation"]')))
			img_tags = article.find_elements(By.CSS_SELECTOR, 'img[crossorigin="anonymous"]')
			for img_tag in img_tags:
				try:
					url = img_tag.get_property('srcset').split(' ')[0]
					if 'https://instagram' in url:
						dict_url.setdefault(url, 'img')
				except:
					continue
			
			video_tags = self.driver.find_elements(By.CSS_SELECTOR, 'video')
			for video_tag in video_tags:
				try:
					url = video_tag.get_property('src')
					print(url)
					if 'https://instagram' in url:
						dict_url.setdefault(url, 'video')
				except:
					continue
			try:
				button_next = article.find_element(By.CSS_SELECTOR, 'button[aria-label="Next"]')
			except:
				break

			if button_next:
				button_next.click()
			else:
				break
		print('Dict:',len(dict_url))
		dict_url = [(k) for k,v in dict_url.items()]
		print(dict_url)

	def main(self):
		ts = []
		for i in range(2):
			t = Thread(target=self.get_information_album_from_url_infor, args=(self.url_infors[i],))
			t.setDaemon = True
			ts.append(t)
		for t in ts:
			t.start()


m = Instagram()		
	


