import scrapy


class ProjectPipeline(object):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def process_item(self, item, spider):
        return item
        
    def close_spider(self, spider):
        pass
