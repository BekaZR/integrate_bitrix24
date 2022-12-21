from typing import Any

from selenium.webdriver import Firefox

from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import lxml


class Parse:
    id_list = []
    def __init__(self, responce):
        self.soup = BeautifulSoup(responce, "lxml")
        self.post_list = []
    
    def __call__(self):
        self.posts = self.soup.find_all(
            "div", class_="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum"
            )
        self.category = self.soup.find_all("span", class_="breadcrumbs-linkWrapper-jZP0j")
    
    def get_data_from_post(self):
        for post in range(len(self.posts)):
            id = self.posts[post]["id"]
            
            if id in self.id_list:
                continue
            self.id_list.append(id)
            
            link = self.posts[post].find("a")['href']
            self.post_list.append(
                {
                    "title": self.posts[post].find("a")['title'],
                    "opportunity": self.posts[post].find("meta", itemprop='price')['content'],
                    "comments": self.posts[post].find("div", class_="iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL").text,
                    "additional_info": f"{self.category[-1].text}  {link}",
                    # "comments": self.posts[post].find("a")['href'],
                }
                )
        return self.post_list


class Bot:
    def __init__(self, link):
        self.link = link
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.driver = Firefox()
        self.driver.get(self.link)
        return self.driver.page_source