import scrapy
from fundrzr.items import indv_camapign


class HealthSpider(scrapy.Spider):
    name = "health"
    start_urls = ["https://fundrazr.com/find?search=education"]


    def parse(self, response):
        next_page = response.xpath('//a[text()="Next →"]/@href').get()

        #following next page
        # if next_page is not None:
        #     print("following next page..........")
        #     print(next_page)
        #     yield response.follow(next_page, callback = self.parse)


        #following indv capaign url
        indv_campaign = response.xpath('//a[@class="campaign-link"]/@href').getall()
        for camp in indv_campaign:
            yield response.follow(camp, callback = self.parse_indv_campaign)


    def parse_indv_campaign(self, response):
        item = indv_camapign()

        item['title'] = response.xpath('//div[@id="campaign-title"]/text()').get().strip()
        item['amount_raised'] = response.xpath('//span[@class="amount-raised"]/text()').get().strip()
        item['amount_raised'] = response.xpath('//span[@class="donation-count stat"]/text()').get().strip()
        item['days_running'] = response.xpath('//span[@class="stat"]/text()').get().strip()
        item['author'] = response.xpath('//a[@title="View profile"]/text()').get().strip()
        item['master_story'] = response.xpath('//div[@id="master-story"]/p/text()').getall()

        #getting stories
        total = ""
        # for story in item['master_story']:
        #     total = total+story.strip()

        yield item
