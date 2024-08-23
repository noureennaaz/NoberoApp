from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from NoberuScraper.spiders.my_spider import MySpider  # Import your spider

class Command(BaseCommand):
    help = 'Run the Scrapy spider to fetch data and store it in MongoDB'

    def handle(self, *args, **kwargs):
        process = CrawlerProcess(get_project_settings())
        process.crawl(MySpider)
        process.start()
        self.stdout.write(self.style.SUCCESS('Scraping completed successfully!'))
