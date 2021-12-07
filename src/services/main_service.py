"""Modules"""
import sys
import requests
from bs4 import BeautifulSoup
from repositories import db_init
sys.path.insert(0, '../src')

class MainClass:
    """Methods for collecting, storing and printing data"""
    def get_topics(self):
        """Scrapes website and returns a list of topics"""
        topics_lst = []
        url = "https://www.economist.com/espresso"
        site = requests.get(url)
        parsed_site = BeautifulSoup(site.content, "html.parser")

        class_t = parsed_site.find_all("div", class_="_gobbet")

        for i in class_t:
            esim = i.get_text()
            topics_lst.append(esim)

        return topics_lst

    def store_topics(self, items):
        """Stores scraped topics into a database"""
        j = 0
        for i in items:
            db_init.insert_to_table(j, i)
            j += 1

    def print_topics():
        """Retrieves topics from database and prints them"""
        data = db_init.get_all_from_table()
        for i in data:
            print(i[-1])

    def db_operations(self, topics):
        """Operations from creating a table, scraping data, check duplicates, storing n printing"""
        db_init.create_table()

        duplicates = db_init.check_duplicates()
        count = db_init.row_count()

        if count <= 0:
            MainClass.store_topics(MainClass, topics)
        elif len(duplicates) < 1:
            MainClass.store_topics(MainClass, topics)
