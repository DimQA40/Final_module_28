import time
from Pages.main_page import Pages


def test_button_mess(web_browser):
    """15.Тестируем кнопку 'Сообщения'.Ожидаем открытие всплывающего окна 'Полный доступ к Лабиринту'.
     Делаем скриншот и сохраняем в файл"""
    page = Pages(web_browser)
    page.button_message.click()
    time.sleep(2)
    web_browser.save_screenshot('images/result.png')


def test_button_mlab(web_browser):
    """16.Тестируем кнопку 'Мой Лаб'.Ожидаем открытие всплывающего окна 'Полный доступ к Лабиринту'.
     Делаем скриншот и сохраняем в файл"""
    page = Pages(web_browser)
    page.button_my_lab.click()
    time.sleep(2)
    web_browser.save_screenshot('images/result1.png')


def test_button_post(web_browser):
    """17.Тестируем кнопку 'Отложено'.Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_postponed.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/'


def test_button_cart(web_browser):
    """18.Тестируем кнопку 'Корзина'.Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_cart.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cart/'


def test_book_buy(web_browser):
    """19.Добавление книги в корзину."""
    page = Pages(web_browser)
    page.buy.click()
    time.sleep(10)

    assert page.message_book_buy
