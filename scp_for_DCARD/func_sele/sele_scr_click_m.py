from selenium import webdriver
from bs4 import BeautifulSoup
from requests import session
from pprint import pprint
import time
import csv
'''
#input:
search word
scroll times
URL

'''
class dcard_search():

    # init
    def __init__(self, w, t, url):
        self.word = w
        self.times = t
        self.URL = url

    def get_dom(self):
        browser = webdriver.Chrome()
        tar_URL1 = self.URL
        browser.get(tar_URL1)
