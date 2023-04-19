from general import *
import requests
from threading import Thread
class Snipstock(Model):
    def __init__(self):
        self.category = [('3', 'Animals'), ('4', 'Architecture/Buildings'), ('5', 'Backgrounds/Textures'), ('6', 'Beauty/Fashion'), ('7', 'Business/Finance'), ('8', 'Computer/Communication'), ('9', 'Education'), ('10', 'Emotions'), ('11', 'Food/Drink'), ('12', 'Health/Medical'), ('13', 'Industry/Craft'), ('14', 'Music'), ('15', 'Nature/Landscapes'), ('16', 'People'), ('17', 'Places/Monuments'), ('18', 'Religion'), ('19', 'Science/Technology'), ('20', 'Sports'), ('21', 'Transportation/Traffic'), ('22', 'Travel/Vacation')]
        self.driver = None
        self.sub(incognito=True)
        self.get_image('c', 'pulleys')
    
    def get_image(self, search_alias, key_word):
        count = 1
        self.product_image = {}
        for key, category_name in self.category:
            path_foder = Path(f'E:/Share/data/snipstock/{category_name}')
            path_foder.mkdir(parents=True, exist_ok=True) 
            self.driver.get(f'https://snipstock.com/search?q=&order=&imgType=png&category={key}')
            number_page = self.driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[6]/div[1]/p/span/strong[2]')
            number_page = int(number_page.text)
            sta = 0
            if key == '3':
                sta = 1128
            for i in range(sta, number_page):
                self.driver.get(f'https://snipstock.com/search?q=&order=&imgType=png&category={key}&page={i+1}')
                searchResultDiv = self.driver.find_element(By.CSS_SELECTOR, 'div[id="searchResults"]')
                images = WebDriverWait(searchResultDiv, 2).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))
                # print(len(images))
                data_image = []
                for image in images: 
                    url_image = image.get_attribute('href')
                    name_image = url_image.split('/')[-1]+ '.png'
                    if '.png' in name_image:
                        data_image.append((f'{url_image}?download=medium', f"{path_foder}/{name_image}"))
                # print(len(data_image))
                self.download_image_thread(data_image)
                with open("log.txt", "a", encoding="utf-8") as file:
                        file.write(f'{key, category_name, i}\n')

    def download_image(self, data):
        for url, path_image in data:
            response = requests.get(url)
            open(path_image, "wb").write(response.content)


    def download_image_thread(self, data_image):
        datas = []
        len_data =len(data_image)//5
        for i in range(0,5):
            if i == 4:
                datas.append(data_image[len_data*4:])
            else:
                datas.append(data_image[len_data*i:len_data*(i+1)])   
        ts = []
        for data in datas:
            t = Thread(target=self.download_image, args=(data,))
            t.setDaemon = True
            ts.append(t)
        for t in ts:
            t.start()

amazon = Snipstock()

