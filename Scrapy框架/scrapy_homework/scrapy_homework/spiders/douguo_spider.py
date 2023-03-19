import scrapy
from ..items import ScrapyHomeworkItem

class DouguoSpiderSpider(scrapy.Spider):
    name = 'douguo_spider'
    allowed_domains = ['www.douguo.com']
    start_urls = ['https://www.douguo.com/caipu/%E5%AE%B6%E5%B8%B8%E8%8F%9C/0/0']

    def parse(self, response, **kwargs):
        data_set = response.xpath('//li[@class="clearfix"]')
        for data in data_set:
            item = ScrapyHomeworkItem()
            item['name'] = data.xpath('./div/a/text()').extract_first()
            item['recipe'] = data.xpath('./div/p/text()').extract_first()
            item['score'] = data.xpath('./div/div[1]/span[2]/text()').extract_first()
            href = 'https://www.douguo.com/' + data.xpath('./div/a/@href').extract_first()

            yield scrapy.Request(url=href, callback=self.parse_hrefData, meta={"item": item})

    def parse_hrefData(self,response):
        item = response.meta["item"]
        item["brief"] = ''.join(response.xpath('//*[@id="left"]/div[2]/p/text()').extract_first().split())
        item["cooking"] = ''.join(response.xpath('//*[@id="left"]/div[5]/p/text()').extract_first().split())
        print(item)
