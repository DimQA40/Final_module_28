import os
from Pages.base import WebPage
from Pages.elements import WebElement


class Pages(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    field_search = WebElement(id='search-field')
    button_search = WebElement(xpath='//button[@type="submit"]')
    message_search = WebElement(xpath='//h1[@class="index-top-title"]')
    message_result = WebElement(xpath='//*[contains(text(),"Мы ничего не нашли по вашему запросу! Что делать?")]')
    button_book = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[1]/span/a')
    button_best = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[2]/span/a')
    button_school = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[3]/span/a')
    button_games = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[4]/span/a')
    button_office = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[5]/span/a')
    button_still = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[10]/span')
    button_multimedia = WebElement(xpath='//*[@id="header-more"]/div/ul/li[5]/a')
    button_souvenir = WebElement(xpath='//*[@id="header-more"]/div/ul/li[6]/a')
    button_journals = WebElement(xpath='//*[@id="header-more"]/div/ul/li[7]/a')
    button_household = WebElement(xpath='//*[@id="header-more"]/div/ul/li[8]/a')
    button_club = WebElement(xpath='//*[@id="minwidth"]/div[7]/div[1]/div[1]/div[4]/div/div[1]/ul/li[11]/span/a')
    button_region = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[12]/span[1]/'
                                     'span/span[3]/span')
    field_button_region = WebElement(xpath='//*[@id="region-post"]')
    click_region = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/h2[1]')
    message_region = WebElement(xpath='//span[@title="Санкт-Петербург"]')
    button_maps = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[4]/div/div[1]/ul/li[12]/span[2]'
                                   '/span[2]/a')
    button_message = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[2]/div/ul/li[3]/a/span[1]/span')
    button_my_lab = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[2]/div/ul/li[4]/a/span[1]'
                                     '/span[1]/span')
    button_postponed = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[2]/div/ul/li[5]/a/span[1]/span[1]'
                                        '/span[1]')
    button_cart = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[2]/div/ul/li[6]/a/span[1]'
                                   '/span[1]/span[3]')
    button_help = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[1]/a')
    button_top = WebElement(xpath='//*[@id="minwidth"]/div[6]/div[1]/div[2]/div/ul/li[2]/a')
    button_rating = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[3]/a')
    button_novelty = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[4]/a')
    button_sale = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[5]/a')
    button_contact = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[6]/a')
    button_all_contact = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[9]/a')
    button_support = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[10]/a')
    button_all_maps = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[11]/a')
    link_VK = WebElement(xpath='//a[@data-event-content="ВКонтакте"]')
    link_VK_kids = WebElement(xpath='//a[@data-event-content="ВКонтакте. Дети"]')
    link_youtube = WebElement(xpath='//a[@data-event-content="Ютьюб"]')
    link_instagram = WebElement(xpath='//a[@data-event-content="Инстаграм"]')
    link_instagram_kids = WebElement(xpath='//a[@data-event-content="Инстаграм. Дети"]')
    link_facebook = WebElement(xpath='//a[@data-event-content="Фейсбук"]')
    link_classmates = WebElement(xpath='//a[@data-event-content="Одноклассники"]')
    link_twitter = WebElement(xpath='//a[@data-event-content="Твиттер"]')
    link_zen = WebElement(xpath='//a[@data-event-content="Дзен"]')
    link_t_me = WebElement(xpath='//a[@data-event-content="Телеграм"]')
    link_tiktok = WebElement(xpath='//a[@data-event-content="ТикТок"]')
    buy = WebElement(xpath='//*[@class="btn buy-link btn-primary"]')
    message_book_buy = WebElement(xpath='//*[@class="popup-window top-block-popup basket-popup dropdown-block js-change'
                                        '-popup-position"]')
