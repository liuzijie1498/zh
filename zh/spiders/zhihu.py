# -*- coding: utf-8 -*-
import json
from pprint import pprint
from zh.items import ZhItem
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    # start_urls = ['https://www.zhihu.com']

    start_user = 'xunzhaohailan'

    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}offset={offset}&limit=20'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    def start_requests(self):

        # 解析用户，获得轮子哥所有粉丝的用户信息
        yield scrapy.Request(url=self.user_url.format(user=self.start_user, include=self.user_query),
                             callback=self.parse_user)

        # 解析轮子哥的粉丝列表
        yield scrapy.Request(
            url=self.followers_url.format(user=self.start_user, include=self.followers_query, offset=0),
            callback=self.parse_followers)

    def parse_user(self, response):
        result = json.loads(response.text)
        pprint(result)
        item = ZhItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        print(response.text)
        yield item
        yield scrapy.Request(self.user_url.format(user=result.get('url_token'), include=self.followers_query, offset=0),
                             self.parse_followers)

    def parse_followers(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield scrapy.Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                                     callback=self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            print(next_page)
            yield scrapy.Request(next_page, self.parse_followers)
