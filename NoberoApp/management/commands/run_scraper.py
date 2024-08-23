# from django.core.management.base import BaseCommand
# import subprocess

# class Command(BaseCommand):
#     help = 'Run Scrapy spider'

#     def handle(self, *args, **kwargs):
#         command = 'scrapy crawl men'
#         result = subprocess.run(command, shell=True, capture_output=True, text=True)

#         if result.returncode == 0:
#             self.stdout.write(self.style.SUCCESS('Spider started successfully'))
#             self.stdout.write(result.stdout)
#         else:
#             self.stdout.write(self.style.ERROR('Failed to start spider'))
#             self.stdout.write(result.stderr)

from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Command(BaseCommand):
    help = 'Run the Scrapy spider'

    def handle(self, *args, **kwargs):
        # Ensure Django settings are not mixed with Scrapy settings
        process = CrawlerProcess(get_project_settings())
        process.crawl('men')  # Replace 'men' with your spider name
        process.start()
        self.stdout.write(self.style.SUCCESS('Successfully ran the scraper'))
