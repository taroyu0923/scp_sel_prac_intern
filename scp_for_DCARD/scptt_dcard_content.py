from requests import Session
from bs4 import BeautifulSoup
import json
from pprint import pprint

# set user agent
session = Session()
session.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
print(session.headers['user-agent'])

# set goal site
tar1_URL = 'https://www.dcard.tw/f?latest=true'

# target tag
tar_css = '[class^=PostEntry_title]'
tar_tag = 'h3'

# catch data
resp = session.get(tar1_URL)
dom = BeautifulSoup(resp.text)
print(dom.select(tar_css))
titles = dom.select(tar_css)
print('-----------------')
print(titles)


