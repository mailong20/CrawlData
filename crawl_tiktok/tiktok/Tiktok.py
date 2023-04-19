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
from __init__ import *
from model import *
import process
class Tiktok:
    def __init__(self):
        self.sub()
        
        self.run()
    def sub(self):
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)
        self.driver.get('https://www.tiktok.com/live')
        DivLive = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "DivExploreButton")]')))
        DivLive.click()
        auto_play = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div[data-e2e="auto-play-icon"]')))
        auto_play.click()
        volume = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div[data-e2e="volume-icon-id"]')))
        volume.click()
     
    def value_to_float(self, x):
        if type(x) == float or type(x) == int:
            return x
        if 'K' in x:
            if len(x) > 1:
                return float(x.replace('K', '')) * 1000
            return 1000.0
        if 'M' in x:
            if len(x) > 1:
                return float(x.replace('M', '')) * 1000000
            return 1000000.0
        if 'B' in x:
            return float(x.replace('B', '')) * 1000000000
        return int(x)

    def run(self):
        while True:
            try:
                SpanNickName = self.driver.find_elements(By.XPATH, '//span[contains(@class, "SpanPersonCount")]')
                for e in SpanNickName:
                    try:
                        e = e.find_element(By.XPATH, '..')
                        all_chill = e.find_elements(By.CSS_SELECTOR, '*')
                        count_live = self.value_to_float(all_chill[4].text)
                        if all_chill[0].text != '' and count_live >=50:
                            if process.add_account(url_tiktok=all_chill[0].text, count_live=count_live):
                                print(all_chill[0].text, count_live)

                        time.sleep(1)

                        DivPageDownButton = self.driver.find_element(By.XPATH, '//div[contains(@class, "DivPageDownButton")]')
                        DivPageDownButton.click()

                    except Exception as e:
                        pass
            except Exception:
                try:
                    self.driver.refresh()
                except Exception:
                    self.sub()
tik = Tiktok()