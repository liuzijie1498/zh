# -*- coding utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in
# https//docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhItem(scrapy.Item):
    id = scrapy.Field()
    url_token = scrapy.Field()
    name = scrapy.Field()
    use_default_avatar = scrapy.Field()
    avatar_url = scrapy.Field()
    avatar_url_template = scrapy.Field()
    is_org = scrapy.Field()
    type = scrapy.Field()
    url = scrapy.Field()
    user_type = scrapy.Field()
    headline = scrapy.Field()
    gender = scrapy.Field()
    is_advertiser = scrapy.Field()
    vip_info = scrapy.Field()
    badge = scrapy.Field()
    badge_v2 = scrapy.Field()
    allow_message = scrapy.Field()
    is_following = scrapy.Field()
    is_followed = scrapy.Field()
    is_blocking = scrapy.Field()
    follower_count = scrapy.Field()
    answer_count = scrapy.Field()
    articles_count = scrapy.Field()
    employments = scrapy.Field()
    is_realname = scrapy.Field()
