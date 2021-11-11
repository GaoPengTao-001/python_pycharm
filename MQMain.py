# -*- coding:UTF-8 -*-
import requests,sys
from bs4 import BeautifulSoup
from download import DownLoad


download = DownLoad()
path = 'D:\pycharm_workplace\python_pycharm\天崩地裂.txt'

if __name__ == '__main__':
    book='https://www.23qb.net/book/2816/'
    _req = requests.get(url=book)
    _html = _req.text
    _bf = BeautifulSoup(_html)
    div = _bf.find_all('ul', class_='chaw_c')
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all('a')
    for i in range(len(a)):
        target = 'https://www.23qb.net/' + a[i].get('href')
        print(target)
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', id='TextContent')
        p_bf = BeautifulSoup(str(texts[0]))
        pArr = p_bf.find_all('p')
        download.down(path,a[i].text)
        for pi in range(len(pArr) -1):
            download.down(path, pArr[pi].text)
        download.down(path,'\n\n')