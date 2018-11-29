# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 10:28:29 2018

@author: mohammed
"""

import logging
from scrapy.utils.log import configure_logging  
from scrapy.contrib.spiders import CrawlSpider, Rule
from webs.items import NewItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors import IGNORED_EXTENSIONS
from scrapy.http import Request
import urllib.parse


class Subpages(CrawlSpider):
    name = "CrawlSubpage"
    
    allowed_domains = ["doercity.com"]
    start_urls = [
       "https://doercity.com/"
    ]
    
    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='log.txt',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )
    #which crawls the all subpages of website and its pages until it does not find <a> tag 
    rules = (
            Rule(LinkExtractor(allow=(r''),restrict_xpaths=('//a'),),follow=True,callback='parse_items_',),
            )
       
    def parse_items_(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
      
        item = NewItem()
        trans_table = {ord(c): None for c in u'\r\n\t'}
        item['page'] = response.url
        item['title'] = ' '.join(s.strip().translate(trans_table) for s in  response.xpath('//title/text()').extract())
        item['content'] =   ' '.join(s.strip().translate(trans_table) for s in  response.xpath('//p/text()').extract())
        yield item
         
         
    custom_settings = {
     'FEED_URI': 'result3.json',
     'FEED_FORMAT': 'json',
     'FEED_EXPORT_ENCODING': 'utf-8'
            } 
   