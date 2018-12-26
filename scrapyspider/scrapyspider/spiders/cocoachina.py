# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import scrapy
import json
import common.utils


class CocoachinaSpider(scrapy.Spider):
    name = 'cocoachina'
    allowed_domains = ['cocoachina.com']
    start_urls = ['http://cocoachina.com/']

    def parse(self, response):
        infos = []
        info_titles = response.xpath('//div[@class="yyinfoblock"]/a/div[@class="yyinfoblockinfo fr"]/h3/text()').extract()
        info_link = response.xpath('//div[@class="yyinfoblock"]/a/@href').extract()
        for index, title in enumerate(info_titles):
            infos.append({
                'title':title,
                'link': info_link[index]
            })
        print()
        print()
        common.utils.print_f(json.dumps(infos))
        print()
        print()
        print(infos)
        print()
        print()
        print('djfkljsdklfjakldfjaklfjadslkfjalkfd')
