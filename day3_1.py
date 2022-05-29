from datetime import datetime
import requests

def url_caller(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is OK")

for my_url in ["https://api.github.com/",
            "https://google.com",
            "https://moshe.com"]:
    url_caller(my_url)


print(datetime.now())

