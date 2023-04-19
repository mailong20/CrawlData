import re
import string
import json
import unicodedata

class Alphabet:
    def __init__(self):
        self.pat_phones = [r'0[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}', r'84[\D]{0,}[\d][\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}',r'02[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d']
        self.pat_links = [r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+']
  
    def convert(self, text: str):
        normal_text = ''
        for char in text:
            if unicodedata.category(char) != "So":
                normal_text += unicodedata.normalize("NFKD", char).encode("ascii", "ignore").decode("utf-8")
            else:
                normal_text += char
        return normal_text


    def get_number(self, text):
        test = ''
        for l in text:
            if l.isnumeric():
                test += l
            else:
                test += ''
        return test
    def filter(self, text):
        links = []
        for pat_link in self.pat_links:
            for link in re.findall(pat_link, text):
                if len(link) <=60:
                    links.append(link)
                text = text.replace(link, '')
        phones = []
        
        for pat_phone in self.pat_phones:
            text_p = text
            for phone in re.findall(pat_phone, text_p):
                    # text = text.replace(phone, '')
                    phone = self.get_number(phone)
                    
                    tmp = 1 if phone[0] == '0' else 2  
                    if (phone[tmp] not in '01246' and 9<len(phone)<12) or phone[:2] == '02' and len(phone) == 11:       
                        phones.append(phone)
                    else:
                        print('Sai:', phone)

        return links, phones


 
    def get_link_and_phone(self, texts):
        links, phones = [], []
        for text in texts:
            text_fs = text.split('\n') if text else []
            for text_f in text_fs:
                text_f = self.convert(text_f)
                linkf, phonef = self.filter(text_f)
                links += linkf
                phones += phonef
        return links, phones



# al = Alphabet()
# text = '028 6653 8882'
# pat = r'02[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d[\D]{0,}\d'
# # print(re.findall(pat, text))
# print(al.get_link_and_phone([text]))

