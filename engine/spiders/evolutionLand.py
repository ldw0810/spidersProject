# -*- coding: utf-8 -*-
import scrapy
import re


class EvolutionLandSpider(scrapy.Spider):
    name = 'evolutionLand'
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'engine.middlewares.EvolutionlandMiddleware': 543,
        }
    }
    allowed_domains = ['www.evolution.land/']
    start_urls = ['https://www.evolution.land/']

    def parse(self, response):
        print response.body
        response_body = re.findall(r'(?<=<body>).*?(?=</body>)', response.body)
        print(response_body)
