from typing import Any

from selenium.webdriver import Firefox

from bs4 import BeautifulSoup

import lxml


class Parse:
    id_list = []
    def __init__(self, responce):
        self.soup = BeautifulSoup(responce, "lxml")
        self.post_list = []
    
    def __call__(self):
        self.posts = self.soup.find_all("div", class_="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum")
        self.category = self.soup.find_all("span", class_="breadcrumbs-linkWrapper-jZP0j")
    
    def get_data_from_post(self):
        for post in range(len(self.posts)):
            id = self.posts[post]["id"]
            
            if id in self.id_list:
                continue
            self.id_list.append(id)
            self.post_list.append(
                {post: {
                    "link": self.posts[post].find("a")['href'],
                    "name": self.posts[post].find("a")['title'],
                    "description": self.posts[post].find("div", class_="iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL").text,
                    "price": self.posts[post].find("meta", itemprop='price')['content'],
                    "category": self.category[-1].text
                }}
                )
        return self.post_list


class Bot:
    def __init__(self, link):
        self.link = link
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.driver = Firefox()
        self.driver.get(self.link)
        return self.driver.page_source