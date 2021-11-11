# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
from download import DownLoad


download = DownLoad()
path = 'D:\pycharm_workplace\python_pycharm\恶魔之魂.txt'

if __name__ == '__main__':
    book='https://www.douban.com/note/200837090/'
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    _req = requests.get(url=book,headers=headers)
    _html = _req.text
    _bf = BeautifulSoup(_html)
    div = _bf.find_all('div', id='link-report')
    download.down(path,div[0].text.replace('恶魔之魂','\n\n'))