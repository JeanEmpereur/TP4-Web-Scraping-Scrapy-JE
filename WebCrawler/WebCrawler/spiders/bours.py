import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsBoursItem
from datetime import datetime
from WebCrawler.pipelines import Databases


class BoursSpider(scrapy.Spider):
    
    Databases.connectDb()
    Databases.createTable()

    name = 'bours'
    allowed_domains = ['finance.yahoo.com']
    start_urls =  [f'https://www.boursorama.com/bourse/actions/palmares/france/page-{n}?france_filter%5Bmarket%5D=1rPCAC' for n in range(1, 3)]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_boursorama)

    def parse_boursorama(self, response):
        liste_indices = response.css('tbody.c-table__body tr.c-table__row')

        for indice in liste_indices:
            item = ReviewsBoursItem()

            #indice boursier
            try:
                item['indice'] = indice.css('a.c-link::text').extract()[0]
            except:
                item['indice'] = None

            #indice cours de l'action
            try:
                item['cours'] = float(indice.css('span.c-instrument--last::text').extract()[0])
            except:
                item['cours'] = None

            #Variation de l'action
            try:
                item['var'] = float(indice.css('span.c-instrument--instant-variation::text').extract()[0].split('%')[0])
            except:
                item['var'] = None

            #Valeur la plus haute
            try:
                item['maxVal'] = float(indice.css('span.c-instrument--high::text').extract()[0])
            except:
                item['maxVal'] = None

            #Valeur la plus basse
            try:
                item['minVal'] = float(indice.css('span.c-instrument--low::text').extract()[0])
            except:
                item['minVal'] = None

            #Valeur d'ouverture
            try:
                item['openVal'] = float(indice.css('span.c-instrument--open::text').extract()[0])
            except:
                item['openVal'] = None

            #Date de la collecte
            try:
                item['date'] = datetime.today()
            except:
                item['date'] = None

            item['page'] = int(response.url.split('page-')[1].split('?')[0])

            Databases.addRowBoursorama(item)
            yield item
