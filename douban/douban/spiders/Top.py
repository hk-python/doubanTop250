# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class TopSpider(scrapy.Spider):
    name = 'Top'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    def parse(self, response):
        a=response.xpath("//div[@id='content']/div/div[@class='article']/ol/li")
        for sel in a:
            item = DoubanItem()
            item["moviename"]="".join(sel.xpath(".//div[@class='hd']/a/span[1]/text()").extract())
            item["moviebd"]="".join(sel.xpath(".//div[@class='info']/div[@class='bd']/p[1]/text()").extract())
            item["moviestar"]="".join(sel.xpath(".//div[@class='star']/span[2]/text()").extract())
            item["movieimg"]="".join(sel.xpath(".//div/div[1]/a/img/@src").extract())
            yield item
        next_page=response.xpath("//div[@id='content']/div/div[1]/div[2]/span[3]/a/@href")
        # print(next_page)
        if next_page:
            url=response.urljoin(next_page[0].extract())
            print(url)
            yield scrapy.Request(url,self.parse)
