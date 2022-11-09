import scrapy
from ..items import DemoScrapyItem

class LianjiaSpiderSpider(scrapy.Spider):
    name = 'lianjia_spider'
    allowed_domains = ['cd.lianjia.com']
    start_urls = ['https://cd.lianjia.com/ershoufang/']

    def parse(self, response, **kwargs):
        datalist = response.xpath('//ul[@class="sellListContent"]/li[contains(@class,"clear")]')
        for data in datalist:
            item = DemoScrapyItem()
            item['title'] = data.xpath("./div/div/a/text()").extract_first()  # 取第一个字符串
            item['price'] = data.xpath("./div/div[6]/div/span/text()").extract_first()
            # 获取详情url
            href = data.xpath("./div/div/a/@href").extract_first()

            # 将获取的url给到调度器
            yield  scrapy.Request(url=href,callback=self.parse_content,meta={"item":item})

        #next_url = "https://cd.lianjia.com" +response.xpath()
        for num in range(2,5):
            next_url = "https://cd.lianjia.com/ershoufang/pg{}".format(num)
            yield scrapy.Request(url=next_url,callback=self.parse)
    # 再解析详情连接url
    def parse_content(self,reponse):
        item = reponse.meta["item"]
        # 使用join将其【】括号消除
        item["house_info"] = ','.join(reponse.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li/text()').extract())

        print(item)


