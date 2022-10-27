# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ReviewsAllocineItem(Item):
    title = Field()
    img = Field()
    author = Field()
    time = Field()
    genre = Field()
    score = Field()
    desc = Field()
    release = Field()


class ReviewsBoursItem(Item):
    indice = Field()
    cours = Field()
    var = Field()
    maxVal = Field()
    minVal = Field()
    openVal = Field()
    date = Field()
    page = Field()

