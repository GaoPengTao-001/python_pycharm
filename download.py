# -*- coding:UTF-8 -*-
import requests,sys

class DownLoad:
    def down(self,path,text):
        with open(path, 'a', encoding='utf-8') as f:
            f.writelines(text)
            f.writelines('\n')