from scrapy import Field, Item


class CountryItem(Item):

    name = Field()
    code2 = Field()
    code3 = Field()
    currency_code = Field()

