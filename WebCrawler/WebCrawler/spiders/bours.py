import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsBoursItem
import time


class BoursSpider(scrapy.Spider):
    name = 'boursorama'
    allowed_domains = ['finance.yahoo.com']
    start_urls =  []

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_boursorama)

    def parse_boursorama(self, response):
        liste_indices = response.css('tr.c-table__row')[1:]

        for indices in liste_indices:
            # item =  # importer la class Items du projet provenant du fichier items.py

            # #indice boursier
            # try:
            #   item['indice'] =  # à compléter
            # except:
            #   item['indice'] = 'None'

            # #indice cours de l'action
            # try:
            #   item['cours'] =  # à compléter
            # except:
            #     item['cours'] = 'None'

            # #Variation de l'action
            # try:
            #   item['var'] =  # à compléter
            # except:
            #   item['var'] = 'None'

            # #Valeur la plus haute
            # try:
            #   item['hight'] =  # à compléter
            # except:
            #   item['hight'] = 'None'

            # #Valeur la plus basse
            # try:
            #   item['low'] =  # à compléter
            # except:
            #   item['low'] = 'None'

            # #Valeur d'ouverture
            # try:
            #   item['open_'] =  # à compléter
            # except:
            #   item['open_'] = 'None'

            # #Date de la collecte
            # try:
            #   item['time'] =  # à compléter
            # except:
            #   item['time'] = 'None'

            # yield item
