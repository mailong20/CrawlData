from general import *
import requests
class Amazon(Model):
    def __init__(self):
        self.driver = None
        self.sub(incognito=True)
        self.get_image('c', 'pulleys')
    
    def get_image(self, search_alias, key_word):
        count = 1
        self.product_image = {}
        while True:  
            url = f"https://www.amazon.com/s?k={key_word.replace(' ', '+')}&page={count}&i=tools-intl-ship"
            self.driver.get(url)
            product_images = self.driver.find_elements(By.CSS_SELECTOR, 'img[data-image-latency="s-product-image"]')
            for product_image in product_images:
                self.product_image.setdefault(product_image.get_attribute('src'), '')
            count +=1
            try:
                next_span = self.driver.find_element(By.XPATH, '//span[contains(@class, "s-pagination-next s-pagination-disabled")]')
                break
            except:
                pass
        key_word_name = Path(f'data/{key_word}')
        key_word_name.mkdir(parents=True, exist_ok=True)    
        for url_image, _ in  self.product_image.items():
            image_name =url_image.split('/')[-1].split('.')[0]
            url_image = f'https://m.media-amazon.com/images/I/{image_name}._SL1500_.jpg'
            response = requests.get(url_image)
            open(f"data/{key_word}/{image_name}.png", "wb").write(response.content)

amazon = Amazon()

