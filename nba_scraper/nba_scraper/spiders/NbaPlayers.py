import scrapy
import re

class NbaplayersSpider(scrapy.Spider):
    name = "NbaPlayers"
    allowed_domains = ["www.espn.com"]
    start_urls = ["https://www.espn.com/nba/player/bio/_/id/3155942/domantas-sabonis"]

    def parse(self, response):
        height,weight = response.xpath('//*[@id="fittPageContainer"]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/ul/li[1]/div[2]/div/text()').get().split(",")
        cleaned_height = re.sub(r'\s+|\"', '', height)
        
        birth_year = response.xpath('//*[@id="fittPageContainer"]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/ul/li[2]/div[2]/div/text()').get().split(" ")[0]
        birth_month = birth_year.split("/")[0]
        birth_day = birth_year.split("/")[1]
        birth_year = birth_year.split("/")[2]
        
        college = response.xpath('//*[@id="fittPageContainer"]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/ul/li[3]/div[2]/div/a/text()').get()
        
        draft_info = response.xpath('//*[@id="fittPageContainer"]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/ul/li[4]/div[2]/div/text()').get()
        draft_year = draft_info.split(" ")[0][:-1]
        draft_round = draft_info.split(" ")[2][:-1]
        draft_pick = draft_info.split(" ")[4]
        
        birthplace = response.xpath('//*[@id="fittPageContainer"]/div[2]/div/div[5]/div/div[1]/section/div/div[9]/div/span[2]/text()').get()
        
        position = response.xpath('//*[@id="fittPageContainer"]/div[2]/div/div[5]/div/div[1]/section/div/div[2]/div/span[2]/text()').get()
        
        yield {
            'name': response.xpath('//*[@id="fittPageContainer"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[2]/h1/span[1]/text()').get(),
            'surname': response.xpath('//*[@id="fittPageContainer"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[2]/h1/span[2]/text()').get(),
            'height': cleaned_height,
            'weight': weight.strip()[:-4],
            'position': position,
            'birth_year': birth_year,
            'birth_month':birth_month,
            'birth_day':birth_day,
            'college': college,
            'draft_year': draft_year,
            'draft_round': draft_round,
            'draft_pick': draft_pick,
            'birthplace':birthplace
        }

