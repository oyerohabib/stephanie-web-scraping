# import scrapy
# import json

# class ExampleSpider(scrapy.Spider):
# 	name = "example"

# 	start_urls = [
# 		'http://quotes.toscrape.com/page/1/',
# 	]

# 	def parse(self, response):
# 		results = []
# 		for quote in response.css('div.quote'):

# 			result = {
# 				'text': quote.css('span.text::text').get().encode("ascii", "ignore").decode('utf-8'),
# 				'author': quote.css('small.author::text').get().encode("ascii", "ignore").decode('utf-8'),
# 				'link': quote.css("span a::attr(href)").get().encode("ascii", "ignore").decode('utf-8'),
# 				'tags': quote.css('div.tags a.tag::text').getall()
# 			}
# 			for tag in result['tags']:
# 				tag.encode("ascii", "ignore").decode('utf-8')

# 			results.append(result)
# 			yield result

# 		next_page = response.css("li.next a::attr(href)").get()
# 		if next_page is not None:
# 			yield response.follow(next_page, callback=self.parse)

# 		page = response.url.split("/")[-2]
# 		filename = f'quotes-{page}.json'
# 		with open(filename, 'w') as f:
# 			f.write(json.dumps(results, indent=2))
# 			f.close()
# 		self.log(f'Saved file {filename}')


# import scrapy

# class AuthorSpider(scrapy.Spider):
#     name = 'author'

#     start_urls = ['http://quotes.toscrape.com/']

#     def parse(self, response):
#         author_page_links = response.css('.author + a')
#         yield from response.follow_all(author_page_links, self.parse_author)

#         pagination_links = response.css('li.next a')
#         yield from response.follow_all(pagination_links, self.parse)

#     def parse_author(self, response):
#         def extract_with_css(query):
#             return response.css(query).get(default='').strip()

#         yield {
#             'name': extract_with_css('h3.author-title::text'),
#             'birthdate': extract_with_css('.author-born-date::text'),
#             'bio': extract_with_css('.author-description::text'),
#         }

# import scrapy

# class QuotesSpider(scrapy.Spider):
#     name = "quotes"

#     def start_requests(self):
#         url = 'http://quotes.toscrape.com/'
#         tag = getattr(self, 'tag', None)
#         if tag is not None:
#             url = url + 'tag/' + tag
#         yield scrapy.Request(url, self.parse)

#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').get(),
#                 'author': quote.css('small.author::text').get(),
#             }

#         next_page = response.css('li.next a::attr(href)').get()
#         if next_page is not None:
#             yield response.follow(next_page, self.parse)