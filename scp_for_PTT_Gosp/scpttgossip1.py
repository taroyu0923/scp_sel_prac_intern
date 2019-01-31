# import method
from requests_html import HTML
from requests import Session
from bs4 import BeautifulSoup
import json

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
def parseArticle(doc):
    html = HTML(html=doc)
    post_entries = html.find('div.r-ent')
    return post_entries
def parseArticleMeta(entry):

    return{
        'title':entry.find('div.title', first=True).text,
        'author':entry.find('div.author', first=True).text
    }
# output
result = catch(tar1URL)
post_entries = parseArticle(result.text)
print(post_entries)

with open("titlemessage.json", 'w') as f:
    for entry in post_entries:
        meta = parseArticleMeta(entry)
        print(meta)
        json.dump(meta, f)

print('-----finish!------')