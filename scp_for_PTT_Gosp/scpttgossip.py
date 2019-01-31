# import method
import requests
from requests import Session
from datetime import datetime
from bs4 import BeautifulSoup
import json
import pprint

# set user agent
session = Session()
session.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
print(session.headers['user-agent'])

#set goal site
tar1URL = 'https://www.ptt.cc/bbs/Gossiping/index.html'
tar2URL = 'https://www.ptt.cc/bbs/Gossiping/M.1548660432.A.541.html'

# catch data
def catch (tar1URL):
    response = session.get(tar1URL)
    response = session.get(tar1URL, cookies={'over18':'1'})
    return response

# output
result = catch(tar1URL)

# adjust code
dom = BeautifulSoup(result.text, 'lxml')
print(dom.get_text)
titles = dom.find_all('div.title')
print(titles)

# output
'''
with open ('testtitle.txt', 'w') as f:
    for title in titles:
        message = title.find('r-ent', 'div.title').getText()
        print(message)
        f.write(message + '\n')

print('---finish!---')
'''

