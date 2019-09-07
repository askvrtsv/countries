import re

import scrapy

from scrapyproject.items import CountryItem


class CountrySpider(scrapy.Spider):
    """"""

    name = 'country'
    custom_settings = {}

    def start_requests(self):
        yield scrapy.Request(
            url="https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes",
            callback=self.parse_code
        )

    def parse_code(self, response):
        for row in response.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr'):
            code2 = row.xpath("./td[4]/a/span/text()").get()
            if not code2:
                continue

            item = CountryItem()
            item['name'] = row.xpath("./td[1]/a/text()").get()
            item["code2"] = code2
            item["code3"] = row.xpath("./td[5]/a/span/text()").get()

            yield response.follow(
                row.xpath("./td[1]/a/@href").get(),
                callback=self.parse_currency_code,
                meta={"item": item},
            )

    def parse_currency_code(self, response):
        item = response.meta['item']

        codes = []
        queries = (
            "//th[text()='Currency']/following-sibling::td[1]//a[@title='ISO 4217']/text()",
            "//th[text()='Currency']/following-sibling::td[1]//text()",
        )
        for query in queries:
            codes += response.xpath(query).getall()

        for code in codes:
            code = re.sub(r'[^A-Z]', "", code)
            if len(code) == 3:
                item['currency_code'] = code
                break

        yield item
