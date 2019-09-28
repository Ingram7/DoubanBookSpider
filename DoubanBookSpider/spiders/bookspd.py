# -*- coding: utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import string
import random
import re
from ..items import DoubanbookspiderItem

class BookspdSpider(CrawlSpider):
    name = 'bookspd'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/subject/1040771/']

    rules = (
        Rule(LinkExtractor(allow=r'/subject/\d+/$'), callback='parse_item', follow=True,
             process_request='get_cookie'),
        #process_request 是一个callable或string(该spider中同名的函数将会被调用)。 该规则提取到每个request时都会调用该函数。该函数必须返回一个request或者None。 (用来过滤request)
    )

    def get_cookie(self, request):
        bid = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(11))
        request.cookies['bid'] = bid
        return request

    def parse_item(self, response):

        item = DoubanbookspiderItem()
        item['id'] = re.findall(r'/subject/(\d+)/', response.url)[0]
        item['cover'] = ''.join(response.xpath('//div[@id="mainpic"]/a[@class="nbg"]/@href').extract())
        item['name'] = ''.join(response.xpath('//span[@property="v:itemreviewed"]/text()').extract())
        item['Originalname'] = ''.join(response.xpath('//div[@id="info"]').re('原作名:</span>\s(.*)<br>'))
        item['author'] = ''.join(response.xpath('//div[@id="info"]//span[contains(text(), "作者")]/../a[1]/text()').extract()).replace(' ','').replace('\n','')
        item['publisher'] = ''.join(response.xpath('//div[@id="info"]').re('出版社:</span>\s(.*)<br>'))
        item['publishdate'] = ''.join(response.xpath('//div[@id="info"]').re('出版年:</span>\s(.*)<br>'))
        item['pages'] = ''.join(response.xpath('//div[@id="info"]').re('页数:</span>\s(.*)<br>'))
        item['price'] = ''.join(response.xpath('//div[@id="info"]').re('定价:</span>\s(.*)<br>'))
        item['rating_num'] = response.xpath('//strong[@property="v:average"]/text()').extract_first()
        item['rating_people'] = response.xpath('//span[@property="v:votes"]/text()').extract_first()

        yield item

