from general import *
import requests
from threading import Thread
class Snipstock(Model):
    def __init__(self):
        self.driver = None
        self.category = ['free-weapons-pngs']
        self.sub(incognito=True)
        self.get_image('c', 'pulleys')
    
    def get_image(self, search_alias, key_word):
        for category in self.category:
            url =f'https://www.cossyimages.com/{category}'
            self.driver.get(url)
            time.sleep(5)
            source = self.driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/main/div/div/div/div[2]/div/div/div/section[1]/div[2]/div/div[2]/div/div[1]/h1/span/span/span')
            
            path_name = source.text.replace('PNG images: ', '')

            path_foder = Path(f'E:/Share/data/cossyimages/{path_name}')
            path_foder.mkdir(parents=True, exist_ok=True)
            count = 0
            while True:
                pictures = []
                try:
                    pictures = WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'picture[id="multi_picture_undefined"]')))
                except Exception:
                    pass
                if len(pictures) ==0:
                    print(count)
                    count +=1
                else:
                    count = 0
                if count >10:
                    count = 0
                    break
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # Lăn chuột lên 5 pixel
                self.driver.execute_script("window.scrollBy(0, -40);")

                # Lăn chuột xuống 5 pixel
                self.driver.execute_script("window.scrollBy(0, 50);")
                data_image = []
                for picture in pictures:
                    source = picture.find_element(By.XPATH, 'source[2]')
                    name_image = source.get_attribute('srcset').split('/')[4]
                    data_image.append((f'https://static.wixstatic.com/media/{name_image}', f"{path_foder}/{name_image}"))
                    self.driver.execute_script("arguments[0].setAttribute('id','multi_picture_undefineds')", picture)
                self.download_image_thread(data_image)
      

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

