import process
import pandas as pd

accounts = process.get_all_account(phone_number = True)
list = []
for i in accounts:
    if i.phone_number !='':
        list.append(i.toString())
print(len(list))

df = pd.DataFrame(list)

df = pd.DataFrame(list, columns =['url_tiktok', 'count_live', 'count_flower', 'user_subtitle', 'user_bio','spanlink','phone_number', 'url_facebook'])
df.to_excel("output.xlsx",
             sheet_name='TIKTOK')  
