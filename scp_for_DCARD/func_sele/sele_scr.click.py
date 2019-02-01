from selenium import webdriver
from bs4 import BeautifulSoup
from requests import session
from pprint import pprint
import time
import csv

timer_start = time.time()

# method
# method to correct page number
def count_finder (text_data):
    count = 0
    for text_data in text_data:
        count = count + 1
    print('Total data is:', count)
    return count
# method to set scroll
def mouse_scroll (count):
    for scroll_count in range(0,count):
        browser.execute_script("window.scrollTo(0,100000)")
        time.sleep(2)
        scroll_count = scroll_count+1
        print('process...', int((scroll_count / input_scroll_count) * 100), '%')

browser = webdriver.Chrome()
tar_URL1 = 'https://www.dcard.tw/f?latest=true'
browser.get(tar_URL1)

result_li = [] # set the result area

try:
    browser.find_element_by_name('query').send_keys("韓國瑜")
    time.sleep(2)
    browser.find_element_by_css_selector('button[class^= "HeaderSearchForm"]').click()
    time.sleep(5)

    print("Please input scroll count:", end='')
    input_scroll_count = int(input())
    mouse_scroll(input_scroll_count)
    
    search_dom = browser.find_elements_by_css_selector('a[class^= "PostEntry_root"]')
    pprint(search_dom)
    
    for i in range(len(search_dom)):
        dic = {}
        dic['title']= search_dom[i].find_element_by_css_selector('h3[class^= "PostEntry_title"]').text
        dic['time_stamp'] = search_dom[i].find_element_by_css_selector('span[class^= "PostEntry_published"]').text
        dic['author'] = search_dom[i].find_element_by_css_selector('span[class^= "PostAuthor_root"]').text
        dic['likecount'] = search_dom[i].find_element_by_css_selector('div[class^= "PostEntry__LikeCount"]').text
        result_li.append(dic)
        # print process
        print('collect data...', int((i / len(search_dom)) * 100), '%')
    pprint(result_li)
    
except Exception as e:
    print('exception type is:')
    print(type(e), str(e))
    print('exception happened')

print('-------------Close Browser---------------')
browser.close()
timer_end = time.time()
count_finder(search_dom)
print('It cost %f sec' %(timer_end - timer_start))