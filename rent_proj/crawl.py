#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import csv
import time
import lxml
# 抓取网址
url = "https://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"

# 初始化页面
page = 0
# 打开rent.csv文件，如果没有就创建一个，并设置写入模式
csv_file = open("rent.csv","w") 
# 创建writer对象
csv_writer = csv.writer(csv_file, delimiter=',')
# 循环所有页面
while True:
    page += 1
    print("fetch: ", url.format(page=page))
    time.sleep(1)
    # 抓取目标页面
    response = requests.get(url.format(page=page))
    # 创建一个BeautifulSoup对象，获取页面正文
    html = BeautifulSoup(response.text,features="lxml")
    # 获取当前页面的房子信息
    house_list = html.select(".list > li")

    # 循环在读不到新的房源时结束
    if not house_list:
        break
    # 房子信息
    for house in house_list:
        house_title = house.select("h2")[0].string
        house_url = house.select("a")[0]["href"]
        house_info_list = house_title.split()

        # 如果第二列是公寓名则取第一列作为地址
        if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]

        house_money = house.select(".money")[0].select("b")[0].string
        # 写入一行数据
        csv_writer.writerow([house_title, house_location, house_money, house_url])

csv_file.close()
