from requests import Session
from bs4 import BeautifulSoup
import json
from pprint import pprint
# set user agent
session = Session()
session.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
print(session.headers['user-agent'])

# set goal site
tar1_URL = 'https://www.dcard.tw/f'

# target tag
tar_css = '[class^=ForumEntryGroup_listContainer]'
tar_tag = 'li'

# catch data
resp = session.get(tar1_URL)
dom = BeautifulSoup(resp.text)
print(dom.select(tar_css))
boards = dom.select(tar_css)[0].select(tar_tag)
sch_boards = dom.select(tar_css)[1].select(tar_tag)
print (sch_boards)

result_1 = {}
result_2 = {}

for board in boards:
    key = board.select_one('a').text   
    value = board.select_one('a').attrs['href']
    result_1[key] = value

for sch_board in sch_boards:
    key = sch_board.select_one('a').text
    value = sch_board.select_one('a').attrs['href']
    result_2[key] = value

pprint(result_1)
pprint(result_2)