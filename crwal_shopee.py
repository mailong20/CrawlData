import json
import uuid
import requests

from requests import request
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem  

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
# Get Random User Agent String.
user_agent = user_agent_rotator.get_random_user_agent()

# api_request = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&keyword=dao%20b%E1%BA%BFp&limit=60&newest={0}&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2"
# api_request = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&keyword=k%C3%A9o&limit=60&newest={0}&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2"

api_request = f"https://shopee.vn/api/v4/search/search_items?by=relevancy&keyword=qu%E1%BA%A7n%5C&limit=60&newest={0}&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2"
# api_request = f"&newest={0}&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2"

for i in range(0, 10):
    user_agent = user_agent_rotator.get_random_user_agent()
    skip = 60 * i
    print(skip)
    headers = {
        "user-agent": user_agent
    }
    api_request.format(skip)
    response = requests.get(api_request, headers=headers)
    data_json = json.loads(response.text)
    # print(response.text)
    items = data_json["items"]
    for item in items:
        item_basic = item["item_basic"]
        images = item_basic["images"]

        for img in images:
            full_url = f"https://cf.shopee.vn/file/{img}"
            response_img = requests.get(full_url)
            open(f'E:/test/{uuid.uuid4()}.png', 'wb').write(response_img.content)
    # page += 120