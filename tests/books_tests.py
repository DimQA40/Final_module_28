import time
from Pages.books_page import Pages


# def test_genres(web_browser):
#     """1.Тестируем кнопку 'Билингвы и книги на иностранных языках'.Ожидаем переход на соответствующую страницу """
#     page = Pages(web_browser)
#     page.button_genres.scroll_to_element()
#     page.button_genres.click()
#
#     assert page.get_current_url() == 'https://www.labirint.ru/genres/965/'

# def test_kids(web_browser):
#     """2.Тестируем кнопку 'Книги для детей'.Ожидаем переход на соответствующую страницу """
#     page = Pages(web_browser)
#     page.button_kids.scroll_to_element()
#     page.button_kids.click()
#
#     assert page.get_current_url() == 'https://www.labirint.ru/genres/1850/'

# def test_comic(web_browser):
#     """3.Тестируем кнопку 'Комиксы, Манга, Артбуки'.Ожидаем переход на соответствующую страницу """
#     page = Pages(web_browser)
#     page.comic_book.scroll_to_element()
#     page.comic_book.click()
#
#     assert page.get_current_url() == 'https://www.labirint.ru/genres/2993/'


# def test_youth(web_browser):
#     """4.Тестируем кнопку 'Молодежная литература'.Ожидаем переход на соответствующую страницу """
#     page = Pages(web_browser)
#     page.youth_book.scroll_to_element()
#     page.youth_book.click()
#
#     assert page.get_current_url() == 'https://www.labirint.ru/genres/3066/'


# def test_fiction(web_browser):
#     """5.Тестируем кнопку 'Нехудожественная литература'.Ожидаем переход на соответствующую страницу """
#     page = Pages(web_browser)
#     page.fiction_book.scroll_to_element()
#     page.fiction_book.click()
#
#     assert page.get_current_url() == 'https://www.labirint.ru/genres/3000/'


# def test_periodic(web_browser):
#     """6.Тестируем кнопку 'Периодические издания'.Ожидаем переход на соответствующую страницу """
#     page = Pages(web_browser)
#     page.periodic_book.scroll_to_element()
#     page.periodic_book.click()
#
#     assert page.get_current_url() == 'https://www.labirint.ru/genres/2137/'


# def test_religion(web_browser):
#     """7.Тестируем кнопку 'Религия'.Ожидаем переход на соответствующую страницу """
#     page = Pages(web_browser)
#     page.religion_book.scroll_to_element()
#     page.religion_book.click()
#
#     assert page.get_current_url() == 'https://www.labirint.ru/genres/2386/'


# def test_dict(web_browser):
#     """8.Тестируем кнопку 'Учебная, методическая литература и словари'.Ожидаем переход на соответствующую страницу """
#     page = Pages(web_browser)
#     page.dict_book.scroll_to_element()
#     page.dict_book.click()
#
#     assert page.get_current_url() == 'https://www.labirint.ru/genres/11/'


# def test_art(web_browser):
#     """9.Тестируем кнопку 'Художественная литература'.Ожидаем переход на соответствующую страницу """
#     page = Pages(web_browser)
#     page.art_book.scroll_to_element()
#     page.art_book.click()
#
#     assert page.get_current_url() == 'https://www.labirint.ru/genres/1852/'


# def test_exc(web_browser):
#     """10.Тестируем кнопку 'Главные книги отдела'.Ожидаем переход на соответствующую страницу """
#     page = Pages(web_browser)
#     page.exc_book.scroll_to_element()
#     page.exc_book.click()
#
#     assert page.get_current_url() == 'https://www.labirint.ru/books/?only_exclusive=1'


# def test_trans_2(web_browser):
#     """11.Тестируем переход с страницы 'Книги' с 1 на 2.Ожидаем переход на соответствующую страницу """
#     page = Pages(web_browser)
#     page.trans_2.scroll_to_element()
#     page.trans_2.click()
#     time.sleep(5)
#
#     assert page.get_current_url() == 'https://www.labirint.ru/books/?page=2'


# def test_trans_10(web_browser):
#     """12.Тестируем переход с страницы 'Книги' с 2 на 10.Ожидаем переход на соответствующую страницу """
#     page = Pages(web_browser)
#     page.trans_10.scroll_to_element()
#     page.trans_10.click()
#     time.sleep(5)
#
#     assert page.get_current_url() == 'https://www.labirint.ru/books/?page=10'

# python -m pytest -v --driver Chrome --driver-path /chromedriver_win/chromedriver tests/books_tests.py


