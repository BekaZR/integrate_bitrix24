from typing import Any

from selenium.webdriver import Firefox

from selenium.webdriver.common.by import By


class Bot:
    id_list = []
    
    def __init__(self, link):
        self.link = link
        self.post_list_for_bitrix = []
        self.post_list = []
    
    def __enter__(self, *args, **kwds):
        self.driver = Firefox()
        self.driver.get(self.link)
        return self
        
    def __exit__(self, *args, **kwargs):
        self.driver.close()
        self.driver.quit()
    
    def get_post_list(self):
        self.post_list = self.driver.find_elements(By.XPATH, '//div[@class="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum"]')
    
    def get_data_for_bitrix(self):
        for i in self.post_list:
            id = i.get_attribute("id")
            if id in self.id_list:
                continue
            self.id_list.append(id)
            data = i.text.split("\n")
            link = i.find_element(By.TAG_NAME, "a").get_attribute("href")
            category = link.split("/")[-2]
            
            self.post_list_for_bitrix.append(
                {
                    "title": data[0],
                    "opportunity": data[1].replace(" ", "").replace("\n", "")[:-1],
                    "comments": data[2],
                    "additional_info": f"{category}  {link}",
                }
            )
        return self.post_list_for_bitrix