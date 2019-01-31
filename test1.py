import unicodedata
import re
import jieba
from datetime import datetime
from collections import Counter

# input text
with open ('demo1.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    f.close

# normalize
newData = unicodedata.normalize('NFKC', data)

# search
title_pat = re.compile(r'^(.+?)\n')
time_pat = re.compile(r'出版時間:(\d\d\d\d/\d\d/\d\d \d\d:\d\d)')
author_pat = re.compile(r'\(([一-龥]+)/[一-龥]+\)')


# group data
title = title_pat.search(data).group(1)
#createdTime = time_pat.search(data)
#createdTime = datetime.strptime(createdTime, '%Y/%m/%d %H:%M')
#author = author_pat.search(data).group(1)

# context
data = re.sub(r'\(.+?\)', '', data)
text = data
for pat in (title_pat, time_pat, author_pat):
    text = pat.sub('', text)
text = text.strip('\n')
tokens = jieba.lcut(text)

#analysis
types = list(set(tokens))
vocabularyRichness = len(types) / len(tokens)
freqdict = Counter(tokens)
highFreqVoc = freqdict.most_common(20)

print(title)
print(types)
print(vocabularyRichness)
print(highFreqVoc)
print('end of task')