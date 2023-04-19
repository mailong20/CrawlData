from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait as Wait
from pathlib import Path
import time
import numpy as np
import pickle
import os
import random
import time
class Model:
    def __init__(self):
        self.driver = None
    def sub(self, incognito=False, headless=False):
        if self.driver is not None:
            self.driver.quit()
        self.driver, self.wait, self.action = self.create_chrome(incognito=incognito, headless=headless)
        
    def sleep(self, fast=False):
        if isinstance(fast, list):
            time.sleep(random.uniform(*fast))
        else:
            time.sleep(random.uniform(0.1, 0.3) if fast else random.uniform(1, 3))

    def human_type(self, text, element):
        self.action.move_to_element(element).perform()
        self.sleep(True)
        self.action.click().perform()
        self.sleep(True)
        for char in text:
            self.sleep(True)
            self.action.send_keys(char).perform()
            
    def human_click(self, element):
        self.action.move_to_element(element).perform()
        self.sleep(True)
        self.action.click().perform()

    def create_chrome(self, profile_name='', wait_timeout=30,
                  options: uc.ChromeOptions = None, headless=False, incognito=False, proxy=None):
        if options is None:
            options = uc.ChromeOptions()

        if proxy is not None:
            options.add_argument(f'--proxy-server={proxy}')
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--mute-audio")
        options.add_argument("--start-maximized")
        options.add_argument("--deny-permission-prompts")
        options.add_argument("--disable-popup-blocking")
        prefs = {"credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.default_content_settings.geolocation": 2}
        options.add_experimental_option("prefs", prefs)
        data_dir = None
        if not incognito:
            profile_name = Path('profile/unknown')
            profile_name.mkdir(parents=True, exist_ok=True)
            data_dir = profile_name.absolute()
            options.add_argument(f"--user-data-dir={data_dir}")
        else:
            options.add_argument("--incognito")
        driver = uc.Chrome(

            options=options,
            user_data_dir=data_dir,
            headless=headless,
            )
        wait = Wait(driver, wait_timeout)
        action = ActionChains(driver)
        return driver, wait, action


# fb = Proton()

