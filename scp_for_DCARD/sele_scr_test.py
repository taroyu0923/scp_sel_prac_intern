# import
from selenium import webdriver
from bs4 import BeautifulSoup
from requests import session
from pprint import pprint
from collections import defaultdict
import time
import random
import csv

# set other item
timer_start = time.time()

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

for scroll_count in range(1,20):
    browser.execute_script("window.scrollTo(0,100000)")
    time.sleep(2)
    scroll_count = scroll_count+1

# get web data
dom = BeautifulSoup(browser.page_source, 'html.parser')
dom_title = browser.find_elements_by_css_selector('h3[class^= "PostEntry_title"]')
dom_desp = browser.find_elements_by_css_selector('div[class^= "PostEntry_excerpt"]')
dom_time_stamp = browser.find_elements_by_css_selector('span[class^= "PostEntry_published"]')
dom_author = browser.find_elements_by_css_selector('span[class^= "PostAuthor_root"]')
dom_likecount = browser.find_elements_by_css_selector('div[class^= "PostEntry__LikeCount"]')
dom_entry = browser.find_elements_by_css_selector('span[class^= "PostEntry_forum"]')

result_li = []
# adjust catch data
for i in range(len(dom_title)):
    dic = {}
    dic['title'] = dom_title[i].text
    dic['entry'] = dom_entry[i].text
    dic['time_stamp'] = dom_time_stamp[i].text
    dic['author'] = dom_author[i].text
    dic['likecount'] = dom_likecount[i].text
   #  dic['desp'] = dom_desp[i].text
    result_li.append(dic)

pprint(result_li)
'''
title = data_adjust(dom_title)
desp = data_adjust(dom_desp)
time_stamp = data_adjust(dom_time_stamp)
author = data_adjust(dom_author)
likecount = data_adjust(dom_likecount)
entry = data_adjust(dom_entry)
'''

# close broswer
print('-------------Close Browser---------------')
browser.close()

# output
'''
with open('output_dataset.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for input_num in range(len(result_li)):
        writer.writerow(result_li)
'''
counter = count_finder(dom_title)
timer_end = time.time()
print('It cost %f sec' %(timer_end - timer_start))