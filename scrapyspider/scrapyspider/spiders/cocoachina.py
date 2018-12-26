# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import scrapy
import json
import common.utils
import db.es
import time

class CocoachinaSpider(scrapy.Spider):
    name = 'cocoachina'
    allowed_domains = ['cocoachina.com']
    start_urls = ['http://cocoachina.com/']

    def parse(self, response):
        infos = []
        es_conn = db.es.es_connector
        info_titles = response.xpath('//div[@class="yyinfoblock"]/a/div[@class="yyinfoblockinfo fr"]/h3/text()').extract()
        info_link = response.xpath('//div[@class="yyinfoblock"]/a/@href').extract()
        cur_time = int(time.time())
        for index, title in enumerate(info_titles):
            infos.append({
                "create": {
                    "_index": "cocoachina",
                    "_type": "_doc",
                    "_id": cur_time + index
                }
            })
            infos.append({
                'title': title,
                'link': info_link[index],
                'date': time.strftime('%Y-%m-%d')
            })
        es_conn.bulk(es_conn, infos)
        print()
        print()
        # common.utils.print_f(json.dumps(infos))
        print()
        print()
        # print(infos)
        print()
        print()
        # print('djfkljsdklfjakldfjaklfjadslkfjalkfd')
