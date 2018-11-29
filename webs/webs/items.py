# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:35:58 2018

@author: mohammed
"""

from scrapy.item import Item, Field

class NewItem(Item):
    page =  Field()
    title = Field()
    content = Field()
    