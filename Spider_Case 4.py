from bs4 import BeautifulSoup
import requests
import re
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
for link in soup.find_all('a'): #打印所有超链接
    print(link.get('href'))
for tag in soup.find_all(True):
    print(tag.name) #打印所有标签名
for tag in soup.find_all(re.compile('b')):
    print(tag.name)
print(soup.find_all('p','course')) #打印包含某属性的标签
print(soup.find_all(id='link1')) #打印id域的标签元素
print(soup.find_all(string="Basic Python")) #打印含有该字符串的信息