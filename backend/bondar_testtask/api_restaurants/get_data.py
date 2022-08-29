import requests
import json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


response = requests.get("https://www.kfc.ru/restaurants")
print(response.status_code)
print("response.json():\n{}\n\n".format(response.json()))
