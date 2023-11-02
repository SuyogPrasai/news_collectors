import scrapy


class KathmandpostSpider(scrapy.Spider):
    name = "kathmandpost"
    allowed_domains = ["kathmandupost.com"]
    start_urls = ["https://kathmandupost.com"]

    def parse(self, response):
        url = 'https://kathmandupost.com/'
        categories = ['national', 'politics', 'valley', 'money', 'sports']
        for category in categories:
            main_url = url + category
            yield response.follow(main_url, callback=self.parse_news)
    
    def parse_news(self, response): 
        posts = response.css('.block--morenews article')
        for post in posts:
            post_title = post.css('a h3::text').get()
            post_url = 'https://kathmandupost.com/' + post.css('a').attrib['href']

            yield {
                'Title': post_title,
                'url': post_url
            } 