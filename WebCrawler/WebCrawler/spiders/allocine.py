import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsAllocineItem

class AllocineSpider(scrapy.Spider):
    name = 'allocine'
    allowed_domains = ['www.allocine.fr']

    #Liste des pages à collecter
    start_urls = [f'https://www.allocine.fr/film/meilleurs/?page={n}' for n in range(1, 30)]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_manga)

    def parse_manga(self, response):
        liste_film = response.css('li.mdl')

        # Boucle qui parcours l'ensemble des éléments de la liste des films
        for film in liste_film:
            item = ReviewsAllocineItem()

            # Nom du film
            try:
                item['title'] = film.css('a.meta-title-link::text')[0].extract()
            except:
                item['title'] = 'None'

            # Lien de l'image du film
            try:
                item['img'] = film.css('img').attrib['src']
            except:
                item['img'] = 'None'

            # Auteur du film
            try:
                item['author'] = film.css('div.meta-body-direction').css('a::text')[0].extract()
            except:
                item['author'] = 'None'

            # Durée du film
            try:
                item['time'] = film.css('div.meta-body-info::text')[0].extract().strip()
            except:
                item['time'] = 'None'

            # Genre cinématographique
            try:
                item['genre'] = film.css('div.meta-body-info')[0].css('span::text').extract()[1:]
            except:
                item['genre'] = 'None'

            # Score du film
            try:
                test = {}
                for score in film.css('div.rating-item-content')[:2] :
                    test[score.css('rating-title::text').extract()] = score.css('.stareval-note::text').extract()
                item['score'] = test
            except:
                item['score'] = 'None'

            # Description du film
            try:
                item['desc'] = film.css('div.synopsis').css('.content-txt::text').extract()[0]
            except:
                item['desc'] = 'None'

            # Date de sortie
            try:
                item['release'] = film.css('span.date::text').extract()[0]
            except:
                item['release'] = 'None'

            yield item
