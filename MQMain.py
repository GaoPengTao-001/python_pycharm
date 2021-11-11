# -*- coding:UTF-8 -*-
import requests
from MQUtil import MQUtil
from bs4 import BeautifulSoup


if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/'
    req = requests.get(url=target)
    html = req.text
    print(html)
    bf = BeautifulSoup(html)
    div = bf.find_all('div', class_='listmain')
    print(div[0])

x = MQUtil()
x.put_data({"333":"高鹏涛"})