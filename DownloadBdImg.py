# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import uuid

from download import DownLoad

download = DownLoad()

def download_img(img_url):
    r = requests.get(img_url, stream=True)
    if r.status_code == 200:
        open('D:\\img\\pitaya\\'+ str(uuid.uuid1()) +'.jpg', 'wb').write(r.content) # 将内容写入图片
        print("保存成功")
    del r

if __name__ == '__main__':
    book='https://image.baidu.com/search/acjson?tn=resultjson_com&logid=12586463282466808439&ipn=rj&ct=201326592&is=&fp=result&fr=&word={keyword}&queryWord={keyword}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={num}&rn=60&gsm=1c&1644805280512='
    # 设置headers，值为浏览器request headers
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cache - Control': 'max - age = 0',
               'Connection': 'keep - alive',
               'Cookie': 'BIDUPSID=2BB669D681EE0014C747FC74D4DD461B; PSTM=1642579195; BAIDUID=2BB669D681EE001491D57A506E9E9512:FG=1; __yjs_duid=1_ffb8001941347eeb9b17c83db90879361642656563191; BDSFRCVID_BFESS=tn_OJeC62uxd-U5HPWz7ukrX0gKK_mcTH6aoJAE6VJw8Wlc5XyjBEG0PEx8g0Kub6m8JogKKL2OTHm_F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tbuDVI8MfI_3HnRY-PR5bJDBbeTb5RjJ-KTKQJOSHJrqfKvmhlncy4LdjG5thP0LQRT7bU3LJ-5OqxPxbURvBPuS3-Aq54RZ0mIq-qc5fU3SHI5y2t6IQfbQ0-oOqP-jW5Ta_JCyWJ7JOpvsDxnxy-umQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ht6T2-DA__I_bfIOP; BAIDUID_BFESS=2BB669D681EE001491D57A506E9E9512:FG=1; MCITY=-315%3A; BDRCVFR[Ke8kQFs3CYT]=OjjlczwSj8nXy4Grjf8mvqV; H_PS_PSSID=31254_26350; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; cleanHistoryStatus=0; indexPageSugList=%5B%22%E8%8B%B9%E6%9E%9C%22%5D; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; delPer=0; PSINO=5; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BA_HECTOR=05al252ga52l0g0k6f1h0jdlg0r; userFrom=null; ab_sr=1.0.1_NzI4NjI5MTUxOGEzMTZkYWY3MjM1NWZiNzA5ZWYzZDJiZTg3ZGQxZTM4NDMzYTIwYTZjZGU3MjdlOTQ1Y2I5MmIxODE4MTk2NTI3NTYwY2QzMWFkNzA4OGU0NjQxZDg3MzE4MDE5NjQyYzg3MWZiNzQ2ZjY2M2U3NTczZjc1MTFhMjI2OTRiODc1ODQzODJmNDU3YzU5ODg4ZDU5YjlmOQ==',
               'Host': 'image.baidu.com',
               'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
               'sec-ch-ua-mobile': '?0',
               'sec-ch-ua-platform': '"Windows"',
               'Sec-Fetch-Dest': 'document',
               'Sec-Fetch-Mode': 'navigate',
               'Sec-Fetch-Site': 'same-origin',
               'Sec-Fetch-User': '?1',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
               }

    for i in range(1,20):
        _req = requests.get(url=book.format(keyword='火龙果', num=str(i*60)),headers=headers)
        # 处理中文乱码的问题
        _req.encoding = _req.apparent_encoding
        text = json.loads(_req.text)
        for i in text['data']:
            if ('thumbURL' in i):
                print(i['thumbURL'])
                download_img(i['thumbURL'])

