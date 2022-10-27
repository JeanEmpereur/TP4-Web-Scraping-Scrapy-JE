# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class WebcrawlerPipeline:
    def process_item(self, item, spider):
        return item


class Databases:
    def connectDb():
        mydb = mysql.connector.connect(
            host="localhost",
            user="redpanda",
            password="redpanda",
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS allocine")
        mycursor.execute("CREATE DATABASE IF NOT EXISTS bours")
        mycursor.execute("CREATE DATABASE IF NOT EXISTS google_scraping")

    def createTable():
        mydb = mysql.connector.connect(
            host="localhost",
            user="redpanda",
            password="redpanda",
            database="allocine"
        )
        mycursor = mydb.cursor()
        mycursor.execute(
            "CREATE TABLE IF NOT EXISTS movie ("
            "title VARCHAR(255), "
            "img VARCHAR(255), "
            "author VARCHAR(255), "
            "time VARCHAR(255), "
            "genre VARCHAR(255), "
            "score VARCHAR(255), "
            "description TEXT(50000), "
            "releaseDate VARCHAR(255))"
        )
        mydb = mysql.connector.connect(
            host="localhost",
            user="redpanda",
            password="redpanda",
            database="bours"
        )
        mycursor = mydb.cursor()
        mycursor.execute(
            "CREATE TABLE IF NOT EXISTS bours ("
            "indice VARCHAR(255), "
            "cours VARCHAR(255), "
            "var FLOAT, "
            "maxVal FLOAT, "
            "minVal FLOAT, "
            "openVal FLOAT, "
            "date DATETIME)"
        )

    def addRowAllocine(item):
        mydb = mysql.connector.connect(
            host="localhost",
            user="redpanda",
            password="redpanda",
            database="allocine"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO movie (title, img, author, time, genre, score, description, releaseDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (item['title'], item['img'], item['author'], item['time'], item['genre'], item['score'], item['desc'], item['release'])
        mycursor.execute(sql, val)
        mydb.commit()

    def addRowBoursorama(item):
        mydb = mysql.connector.connect(
            host="localhost",
            user="redpanda",
            password="redpanda",
            database="bours"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO bours (indice, cours, var, maxVal, minVal, openVal, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (item['indice'], item['cours'], item['var'], item['maxVal'], item['minVal'], item['openVal'], item['date'])
        mycursor.execute(sql, val)
        mydb.commit()

    def createTableGoogle():
        mydb = mysql.connector.connect(
            host="localhost",
            user="redpanda",
            password="redpanda",
            database="google_scraping"
        )
        mycursor = mydb.cursor()
        mycursor.execute(
            "CREATE TABLE IF NOT EXISTS google_scraping ("
            "title VARCHAR(255), "
            "img VARCHAR(255), "
            "author VARCHAR(255), "
            "time VARCHAR(255), "
            "genre VARCHAR(255), "
            "score VARCHAR(255), "
            "description TEXT(50000), "
            "releaseDate VARCHAR(255))"
        )
    
    def addRowGoogleScraping(item):
        mydb = mysql.connector.connect(
            host="localhost",
            user="redpanda",
            password="redpanda",
            database="google_scraping"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO google_scraping (indice, cours, var, maxVal, minVal, openVal, date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (item['indice'], item['cours'], item['var'], item['maxVal'], item['minVal'], item['openVal'], item['date'])
        mycursor.execute(sql, val)
        mydb.commit()
