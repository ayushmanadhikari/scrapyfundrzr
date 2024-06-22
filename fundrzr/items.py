# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FundrzrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class capaign_list(scrapy.Item):
    pass


class indv_camapign(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    donation_count = scrapy.Field()
    days_running = scrapy.Field()
    master_story = scrapy.Field()
    amount_raised = scrapy.Field()
