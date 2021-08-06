import scrapy
from tutorial.items import QuoteItem 

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    def parse(self, response):
        quoteItem=QuoteItem()

        for quote in response.css('div.quote'):
            quoteItem['text']=quote.css('span.text::text').get()
            quoteItem['author']=quote.css('small.author::text').get()
            yield quoteItem
            # yield {
                # 'text': quote.css('span.text::text').get(),
                # 'author': quote.css('small.author::text').get(),
                # 'tags': quote.css('div.tags a.tag::text').getall(),
                # }
