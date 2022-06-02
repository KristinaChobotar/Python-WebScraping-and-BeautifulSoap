import requests
import re
from bs4 import BeautifulSoup

r = requests.get(url='https://python.org/')
soup = BeautifulSoup(r.text, "html.parser")

# 1
print(soup.title)
# 2
tag_p = soup.find_all('p')
print(tag_p)
# 3
print(len(tag_p))
# 4
print(tag_p[0].string)
#5
tag_h2 = soup.find_all('h2')
print(len(tag_h2[0]))
#6
tag_a = soup.find_all('a')
print(tag_a[0].string)
#7
tag_ahref = soup.find_all('a')
print(tag_ahref[0]['href'])
# 8
for tag_li in soup.find_all('li'):
    print(tag_li.find_next('a')['href'])
# 9
print(len(tag_h2[0:4]))
#10
print(tag_a[0:11])
# 11
tag_h1 = list(soup.find_all('h1'))
tag_h2 = list(soup.find_all('h2'))
tag_h3 = list(soup.find_all('h3'))
tag_h1h2h3 = tag_h1 + tag_h3 + tag_h2
print(tag_h1h2h3)
# 12
print(soup.get_text())
# 13
for tag_name in soup.find_all():
    print(tag_name.name)
# 14
print(soup.find_all('html'))
# 15
for child in soup.find('body').children:
    print(child)
# 16
tag_h_1 = soup.find_all('h1')[1]
print(tag_h_1.string)
print(tag_h_1.parent)
# 17
tag_li_ = soup.find_all('li')
print(tag_li_)
# 18
str1 = soup.find_all(string=re.compile('Python'))
for txt in str1:
    print(" ".join(txt.split()))
print(soup.get_text())
# 19
print(soup.select("#python-network"))
# 20
print(soup.find(href='//docs.python.org/3/tutorial/controlflow.html#defining-functions'))
# 21
print(soup.select('p > a'))
# 22
print(soup.find_all(class_='menu'))
# 23
tag_change = soup.find('h1')["class"] = 'changed'
print(tag_change)
# 24
soup.a.append(' CSS')
print(soup.a)
# 25
tag_url = soup.find('a')
tag_url.insert(0, 'Url ')
print(tag_url)
# 26
tag_new = soup.new_tag("i")
tag_new.string = "Before"
soup.li.insert_before(tag_new)
print(soup.li.parent)
# 27
tag_new = soup.new_tag("i")
tag_new.string = "After"
soup.li.insert_after(tag_new)
# print(soup.li.parent)
# 28
tagg = soup.a
tagg.clear()
print(tagg)
# 29
a_tag = soup.find_all('a')[1]
span_tag = soup.span.extract()
print(span_tag)
print(a_tag)
# 30
a__tag = soup.find_all('a')[1]
span__tag = soup.span.decompose()
print(span__tag)
print(a__tag)
# 31
a___tag = soup.find_all('a')[1]
new_tag = soup.new_tag('span')
new_tag.string = 'new text'
a___tag.span.replace_with(new_tag)
print(a___tag)
# 32
new_tag = soup.new_tag('span')
print(soup.a.string.wrap(soup.new_tag('b')))
# 33
a_tag_ = soup.find_all('a')[1]
a_tag_.unwrap()
print(a_tag_)