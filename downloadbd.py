# -*- coding:UTF-8 -*-
import requests,sys
from bs4 import BeautifulSoup
from download import DownLoad


download = DownLoad()
path = 'D:\pycharm_workplace\python_pycharm\天崩地裂.txt'

if __name__ == '__main__':
    book='https://wenku.baidu.com/ndPureView/8637905d81eb6294dd88d0d233d4b14e85243ee5?foldPageNums=2&visibleFoldPage=1'
    _req = requests.get(url=book)
    _html = _req.text
    _bf = BeautifulSoup(_html)
    # print(_bf)
    p = _bf.find_all('p')
    for t in p:
        print(t.text,end='')
    # a_bf = BeautifulSoup(str(div[0]))
    # a = a_bf.find_all('a')
    # for i in range(len(a)):
    #     target = 'https://www.23qb.net/' + a[i].get('href')
    #     print(target)
    #     req = requests.get(url=target)
    #     html = req.text
    #     bf = BeautifulSoup(html)
    #     texts = bf.find_all('div', id='TextContent')
    #     p_bf = BeautifulSoup(str(texts[0]))
    #     pArr = p_bf.find_all('p')
    #     download.down(path,a[i].text)
    #     for pi in range(len(pArr) -1):
    #         download.down(path, pArr[pi].text)
    #     download.down(path,'\n\n')