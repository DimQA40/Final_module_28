import os
from Pages.base import WebPage
from Pages.elements import WebElement
from selenium.webdriver.common.by import By


class Pages(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/books/'

        super().__init__(web_driver, url)

    button_genres = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[1]/a')
    button_kids = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[2]/a')
    comic_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[3]/a')
    youth_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[4]/a')
    fiction_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[5]/a')
    periodic_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[6]/a')
    religion_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[7]/a')
    dict_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[8]/a')
    art_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[9]/a')
    exc_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/div[5]/div/div[3]/ul/li[10]/a')
    trans_2 = WebElement(xpath='//*[@id="catalog"]/div/div[3]/div/div[6]/div[2]/div[1]/div[2]/div[2]/a')
    trans_10 = WebElement(xpath='//*[@id="catalog"]/div/div[3]/div/div[6]/div[2]/div[1]/div[2]/div[10]/a')