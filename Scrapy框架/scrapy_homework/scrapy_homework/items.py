# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyHomeworkItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    recipe = scrapy.Field()
    score = scrapy.Field()
    brief = scrapy.Field()
    cooking = scrapy.Field()



