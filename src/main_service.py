import requests
from bs4 import BeautifulSoup

class Main_class():
    def __init__(self, input):
        self.input = input

    def get_topics():
        url = "https://www.economist.com/espresso"
        site = requests.get(url)
        parsed_site = BeautifulSoup(site.content, "html.parser")

        for i in parsed_site(["style"]):
            i.decompose()

        items = parsed_site.find_all("div", class_="_gobbet")

        for i in items:
            print(i.text, end="\n")