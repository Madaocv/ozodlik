import scrapy
from ozodlikorg.items import OzodlikorgItem

class OzodlikSpider(scrapy.Spider):
    name = 'ozodlik_1'

    def __init__(self, *args, **kwargs):
        super(OzodlikSpider, self).__init__(*args, **kwargs)
        self.name2 = kwargs.get('name2')
        self.start_urls = ['https://www.rferl.org/s?k=%s' % self.name2]

    def parse(self, response):

        items = OzodlikorgItem()

        all_div = response.css('.fui-grid__inner')

        for media in all_div:
            title = media.css('.media-block__title--size-3::text').get()
            content = media.css('.perex--mb::text').get()
            author = media.css('.links__item-link::text').get()

            items['title'] = title
            items['content'] = content
            items['author'] = author

            yield items

        # next_page = response.css('li.pagination__item--next a::attr(href)').get()
        # print(next_page)
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
