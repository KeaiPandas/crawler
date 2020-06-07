import requests
from bs4 import BeautifulSoup

# 使用requests.get 方法发送请求,获取响应对象
r = requests.get('https://www.shiyanlou.com/courses')
# 使用 BeautifulSoup类的实力解析源码
soup = BeautifulSoup(r.text, features='lxml')

# 创建空字典对象存储课程名字和图片地址
courses_dict = {}

# 将课程名字作为key，图片地址作为value添加键值对
for div in soup.find_all('div', class_='col-sm-12 col-md-3'):
    courses_dict[div.img['alt']] = div.img['src']

# 爬取图片并存储到指定目录下，文件名即课程名
for name, url in courses_dict.items():
    r = requests.get(url)
    with open('存储目录地址' + name, 'wb') as f:
        f.write(r.content)
