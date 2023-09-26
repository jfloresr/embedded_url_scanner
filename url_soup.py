#!/opt/automation-artifacts/projects/url_soup/url_soup_venv/bin/python3

import requests
import re
import sys
import json
import validators
from bs4 import BeautifulSoup
from requests.packages import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = sys.argv[1]

if not validators.url(url):
    e = {}
    e["Error"] = "URL provided is not valid"
    print(json.dumps(e, indent=3))
    sys.exit()

reqs = requests.get(url, verify=False)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
reg = re.compile("^http.*", re.IGNORECASE)
for link in soup.find_all('a'):
    if reg.match(str(link.get('href'))):
        urls.append(link.get('href'))
    else:
        continue

urlObj = {}
urlObj["urlList"] = urls
urlObj["urlCount"] = len(urls)
print(json.dumps(urlObj, indent=3))
