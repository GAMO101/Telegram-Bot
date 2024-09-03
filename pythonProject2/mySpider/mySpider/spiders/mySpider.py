import scrapy


class FreyTagSpider(scrapy.Spider):
    name = 'freytagspider'
    start_urls = ['https://frey-tag.at/']

    # Custom settings for the spider
    custom_settings = {
        'FEEDS': {
            'frey_tag.json': {
                'format': 'json',
                'overwrite': True,  # If the file already exists, it will overwrite it
            },
        },
    }

    def parse(self, response):
        # Log the visited URL and the status code
        self.log(f"Visited {response.url} with status code {response.status}")

        # Adjust the selectors based on the site's HTML structure
        events = response.css('div.event-container')  # Assuming each event is in a div with class 'event-container'

        for event in events:
            title = event.css('h2.event-title::text').get()
            date = event.css('div.event-date::text').get()

            # Yield each event's data
            yield {
                'Title': title.strip() if title else None,
                'Date': date.strip() if date else None,
            }
