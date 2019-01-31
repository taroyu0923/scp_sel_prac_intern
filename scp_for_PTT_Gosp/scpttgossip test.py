# import method
from requests import Session
from bs4 import BeautifulSoup
from pprint import pprint

# set user agent
session = Session()
session.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
print(session.headers['user-agent'])

#set goal site
tar1URL = 'https://www.ptt.cc/bbs/Gossiping/index.html'
tar2URL = 'https://www.ptt.cc/bbs/Gossiping/M.1548660432.A.541.html'

# catch data
def catch (tar2URL):
    response = session.get(tar2URL)
    response = session.get(tar2URL, cookies={'over18':'1'})
    return response
result = catch(tar2URL)

# adjust code
dom = BeautifulSoup(result.text, 'lxml')
print(dom.get_text)
print('--------------------')
articles = dom.find_all('div', 'push')
print(articles)

# output
with open('testMessages.txt', 'w') as f:
    for article in articles:
        messages = article.find('span', 'f3 push-content').getText().replace(':','').strip()
        pprint (messages)
        f.write(messages + "\n")

print('---finish!---')