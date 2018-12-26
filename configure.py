# -*- coding: utf-8 -*-
# @File  : configure.py
# @Author: Arhur
# @Date  : 2018/12/22
# @Desc  :

import configparser
import os

cf = configparser.ConfigParser()
path = os.path.dirname(os.path.abspath(__file__))
print(path)
cf.read(f'{path}/db.conf')


class es_db():
    url = cf.get('es', 'url')

if __name__ == '__main__':
    es_db = es_db()
    print(es_db.url)