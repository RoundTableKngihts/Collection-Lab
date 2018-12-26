# -*- coding: utf-8 -*-
# @File  : es.py
# @Author: Arhur
# @Date  : 2018/12/22
# @Desc  :
# import sys
# sys.path.append('..')
# import configparser

# cf = configparser.ConfigParser()
# cf.read('/Users/arthur/git-project/trk/Collection-Lab/db.conf')
# print(cf.get('es','url'))
import configure
import os
# print(configure.es_db.url)
import http
base_url = configure.es_db.url
import requests
import json
header = {
    "content-type": "application/json"
}
class es_connector():
    def __init__(self):
        self.url = configure.es_db.url

    # def conn(self):

    def join_url(self, suffix):
        urls = [base_url, suffix]
        return '/'.join(urls)

    def get(self, suffix):
        urls = [base_url, suffix]
        get_url = '/'.join(urls)
        res = requests.get(get_url, headers=header)
        results = res.text
        return results

    def post(self, suffix, data):
        get_url = self.join_url(suffix)
        results = requests.post(get_url, json.dumps(data), headers=header)
        return results


if __name__ == '__main__':
    es = es_connector()
    # print(es.post('test/_doc/a',{
    #         'a':1,
    #         'b':2,
    #         'c':3
    #     }))





