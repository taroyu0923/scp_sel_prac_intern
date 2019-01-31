import requests
from bs4 import BeautifulSoup
from pprint import pprint
from tabulate import tabulate

# setting
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
url = 'http://www.forex.ntu.edu.tw/members/teacher.php' 
response = requests.get(url, headers = headers)
response.encoding = 'utf-8'
html = response.text

# process
dom = BeautifulSoup(html, 'html.parser')
teachers = dom.find_all('div', class_ = 'teacher_list')

# teachers' data
teacher_list = []
for teacher in teachers:
    name = teacher.find_all('li')[1].find('a').text
    
    job_title = teacher.find_all('li')[0]
    job_title = job_title.text.replace('職稱:', '').strip()

    sub_dom = teacher.find('li', class_ = 'mail')
    if sub_dom:
        email = sub_dom.find('a').attrs['href']
        email = email.replace('mailto:','')
    else:
        email = ''
    teacher_list.append((name, job_title, email))

# output
pprint(teacher_list)
print(tabulate(teacher_list, headers=['姓名','職稱','email']))
print('end of task')