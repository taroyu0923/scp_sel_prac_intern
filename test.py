import re

text = "應該不會這麼多人去買吧，大家都知道salary一直沒有increase可是物價一直increase，我覺得比較是大家concern的東西，如果是吃西餐的話，像三明治加一個burger或什麼都會比這個高價錢，所以我覺得如果它要漲的話，應該會比較受到impact"

result = re.search('[salary]',text)
result.group(0)
print(result)