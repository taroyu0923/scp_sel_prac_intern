# import

from selenium import webdriver
from bs4 import BeautifulSoup
from requests import session
from pprint import pprint
import time
import csv

# set other item

timer_start = time.time()
print("Please input scroll count:")
input_scroll_count = int(input())

# method to correct page number
def count_finder (text_data):
    count = 0
    for text_data in text_data:
        count = count + 1
    print('Total data is:', count)
    return count
# method to adjust dom
def data_adjust (dom_text):
    result = []
    for dom_text in dom_text:
        message = dom_text.text
        print(message)
        result.append(message)
    return result
# method to find element by css celector
def find_elements_by_css (item ,path):
    dom = item.find_elements_by_css_selector(path)
    return dom
# set webdriver & target site
browser = webdriver.Chrome()
tar_URL1 = 'https://www.dcard.tw/f?latest=true'
browser.get(tar_URL1)

for scroll_count in range(1,input_scroll_count):
    browser.execute_script("window.scrollTo(0,100000)")
    time.sleep(2)
    scroll_count = scroll_count+1

# get web data

result_li = [] # set the result area
dom = BeautifulSoup(browser.page_source, 'html.parser')
total_dom = browser.find_elements_by_css_selector('a[class^= "PostEntry_root"]')
try:
    for i in range(len(total_dom)):
        dic = {}
        dic['title']= total_dom[i].find_element_by_css_selector('h3[class^= "PostEntry_title"]').text
        dic['time_stamp'] = total_dom[i].find_element_by_css_selector('span[class^= "PostEntry_published"]').text
        dic['author'] = total_dom[i].find_element_by_css_selector('span[class^= "PostAuthor_root"]').text
        dic['likecount'] = total_dom[i].find_element_by_css_selector('div[class^= "PostEntry__LikeCount"]').text
        dic['entry'] = total_dom[i].find_element_by_css_selector('span[class^= "PostEntry_forum"]').text
        # dic['desp'] = total_dom[i].find_element_by_css_selector('div[class^= "PostEntry_excerpt"]').text
        result_li.append(dic)
    pprint(result_li)
except Exception as e:
    print('exception type is:')
    print(type(e), str(e))
    print('exception happened')

# close broswer

print('-------------Close Browser---------------')
browser.close()

# output

'''
with open('output_dataset.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for i in result_li:
        writer.writerow(result_li)
'''
#counter = count_finder(dom_title)

timer_end = time.time()
count_finder(total_dom)
print('It cost %f sec' %(timer_end - timer_start))