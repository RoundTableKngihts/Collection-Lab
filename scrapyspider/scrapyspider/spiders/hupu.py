# -*- coding: utf-8 -*-
import scrapy
import db.es


def gen_start_urls():
    c = 156378
    start_urls = []
    for i in range(1, 10):
        start_urls.append(f'https://nba.hupu.com/games/boxscore/{c+i}')
    print(start_urls)
    return start_urls

class HupuSpider(scrapy.Spider):
    name = 'hupu'
    allowed_domains = ['hupu.com']
    start_urls = gen_start_urls()

    def parse(self, response):
        id = response.url.split('/')[-1]
        print('id is '+id)
        away_player_datas = []
        home_player_datas = []
        away_team = response.xpath('//div[@class="team_a"]/div[@class="message"]/p/a/text()').extract_first()
        away_score = response.xpath('//div[@class="team_a"]/div[@class="message"]/h2/text()').extract_first()
        home_team = response.xpath('//div[@class="team_b"]/div[@class="message"]/p/a/text()').extract_first()
        home_score = response.xpath('//div[@class="team_b"]/div[@class="message"]/h2/text()').extract_first()
        time = response.xpath('//div[@class="about_fonts clearfix"]/p[@class="time_f"]/text()').extract_first()
        for node in response.xpath(
                '//table[@id="J_away_content"]/tbody/tr[@style="background-color: rgb(255, 255, 255);"]'):
            player_data = []
            player_id = ''
            for item in node.xpath('td'):
                if item.xpath('a/text()'):
                    player_id = item.xpath('a/@href').extract_first().split('/')[-1].split('.')[0];
                    player_data.append(item.xpath('a/text()').extract()[0].replace('\n', ''))
                    player_data.append(item.xpath('a/@href').extract_first().split('/')[-1].split('.')[0])
                elif item.xpath('span/text()'):
                    player_data.append(item.xpath('span/text()').extract()[0].replace('\n', ''))
                else:
                    # print(item.xpath('text()').extract())
                    player_data.append(item.xpath('text()').extract()[0].replace('\n', ''))
            away_player_datas.append({player_id: player_data})
        for node in response.xpath(
                '//table[@id="J_home_content"]/tbody/tr[@style="background-color: rgb(255, 255, 255);"]'):
            player_data = []
            player_id = ''
            for item in node.xpath('td'):
                if item.xpath('a/text()'):
                    player_id = item.xpath('a/@href').extract_first().split('/')[-1].split('.')[0];
                    player_data.append(item.xpath('a/text()').extract()[0].replace('\n', ''))
                    # print(item.xpath('a/@href').extract_first())
                    player_data.append(item.xpath('a/@href').extract_first().split('/')[-1].split('.')[0])
                elif item.xpath('span/text()'):
                    player_data.append(item.xpath('span/text()').extract()[0].replace('\n', ''))
                else:
                    # print(item.xpath('text()').extract())
                    player_data.append(item.xpath('text()').extract()[0].replace('\n', ''))
            home_player_datas.append({player_id: player_data})
        print(f'away team is {away_team}')
        print(f'home team is {home_team}')
        print(f'away score is {away_score}')
        print(f'home score is {home_score}')
        print(f'time is {time}')
        print(away_player_datas)
        print(home_player_datas)
        data = {
            "time": time,
            "away_team": away_team,
            "home_team": home_team,
            "away_score": away_score,
            "home_score": home_score,
            "away_player_datas": away_player_datas,
            "home_player_datas": home_player_datas
        }
        es_conn = db.es.es_connector
        results = es_conn.post(es_conn, f'nba_games/_doc/{id}', data)
        print(results.content)