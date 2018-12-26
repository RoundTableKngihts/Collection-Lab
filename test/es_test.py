# -*- coding: utf-8 -*-
# @File  : es_test.py
# @Author: Arhur
# @Date  : 2018/12/22
# @Desc  :

import unittest
import db.es
import common.utils as utils
import json
es_conn = db.es.es_connector()


class es_test(unittest.TestCase):
    def test_get(self):
        utils.print_f('test es get function')
        # self.assertTrue('foo'.upper(), 'FOO')
        result = json.loads(es_conn.get('test/_doc/a'))
        self.assertTrue(result['_source']['a'], 1)

    def test_post(self):
        result = es_conn.post('test/_doc/a',{
            'a':1,
            'b':2,
            'c':3
        })
        self.assertTrue(result.status_code,200)


if __name__ == '__main__':
    es_test.main()
