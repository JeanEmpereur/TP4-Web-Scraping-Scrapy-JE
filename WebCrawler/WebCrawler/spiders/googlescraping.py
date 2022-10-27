import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsAllocineItem
from WebCrawler.pipelines import Databases

class GooglescrapingSpider(scrapy.Spider):
    name = 'googlescraping'
    allowed_domains = ['www.google.be']
    start_urls = ['http://www.google.be/']

    Databases.connectDb()
    Databases.createTable()

    name = 'allocine'
    allowed_domains = ['www.allocine.fr']

    #page a collecter
    yes = f'https://www.google.be/search?q={recherche}&tbm=isch'

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_manga)

    def parse_google(self, response):
        liste_film = response.css('li.mdl')

        # Boucle qui parcours l'ensemble des éléments de la liste des films
        for film in liste_film:
            item = ReviewsAllocineItem()

            # Nom du film
            try:
                item['title'] = film.css(
                    'a.meta-title-link::text')[0].extract()
            except:
                item['title'] = None

            # Lien de l'image du film
            try:
                item['img'] = film.css('img').attrib['src']
            except:
                item['img'] = None

            # Auteur du film
            try:
                item['author'] = film.css(
                    'div.meta-body-direction').css('a::text')[0].extract()
            except:
                item['author'] = None

            # Durée du film
            try:
                item['time'] = film.css(
                    'div.meta-body-info::text')[0].extract().strip()
            except:
                item['time'] = None

            # Genre cinématographique
            try:
                item['genre'] = '' .join(
                    film.css('div.meta-body-info')[0].css('span::text').extract()[1:])
            except:
                item['genre'] = None

            # Score du film
            try:
                # test = {}
                # for score in film.css('div.rating-item-content')[:2] :
                #     test[score.css('rating-title::text').extract()] = score.css('.stareval-note::text').extract()
                # item['score'] = test
                item['score'] = film.css(
                    'div.rating-item-content .stareval-note::text')[0].extract()
            except:
                item['score'] = None

            # Description du film
            try:
                item['desc'] = film.css('div.synopsis').css(
                    '.content-txt::text').extract()[0]
            except:
                item['desc'] = None

            # Date de sortie
            try:
                item['release'] = film.css('span.date::text').extract()[0]
            except:
                item['release'] = None

            Databases.addRowAllocine(item)
            yield item
