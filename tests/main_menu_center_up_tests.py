from Pages.main_page import Pages


def test_field_search(web_browser):
    """1.Тестирование поле поиска. Поиск книги"""
    page = Pages(web_browser)
    page.field_search.send_keys('Щелкунчик')
    page.button_search.click()

    assert page.message_search


def test_search_field_num(web_browser):
    """2.Тестирование поле поиска. """
    page = Pages(web_browser)
    page.field_search.send_keys('12345678901234567890')
    page.button_search.click()

    assert page.message_result.get_text() == 'Мы ничего не нашли по вашему запросу! Что делать?'


def test_button_book(web_browser):
    """3.Тестируем кнопку "Книги".Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_book.click()

    assert page.get_current_url() == 'https://www.labirint.ru/books/'


def test_button_best(web_browser):
    """4.Тестируем кнопку "Главное 2021".Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_best.click()

    assert page.get_current_url() == 'https://www.labirint.ru/best/'


def test_button_sch(web_browser):
    """5.Тестируем кнопку "Школа".Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_school.click()

    assert page.get_current_url() == 'https://www.labirint.ru/school/'


def test_button_games(web_browser):
    """6.Тестируем кнопку "Игрушки".Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_games.click()

    assert page.get_current_url() == 'https://www.labirint.ru/games/'


def test_button_office(web_browser):
    """7.Тестируем кнопку "Канцелярские товары".Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_office.click()

    assert page.get_current_url() == 'https://www.labirint.ru/office/'


def test_button_still_mul(web_browser):
    """8.Тестируем кнопку "CD/DVD".Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_still.click()
    page.button_multimedia.click()

    assert page.get_current_url() == 'https://www.labirint.ru/multimedia/'


def test_button_still_souvenir(web_browser):
    """9.Тестируем кнопку "Сувениры".Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_still.click()
    page.button_souvenir.click()

    assert page.get_current_url() == 'https://www.labirint.ru/souvenir/'


def test_button_still_jour(web_browser):
    """10.Тестируем кнопку "Журналы".Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_still.click()
    page.button_journals.click()

    assert page.get_current_url() == 'https://www.labirint.ru/journals/'


def test_button_still_house(web_browser):
    """11.Тестируем кнопку "Товары для дома".Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_still.click()
    page.button_household.click()

    assert page.get_current_url() == 'https://www.labirint.ru/household/'


def test_button_club(web_browser):
    """12.Тестируем кнопку "Клуб".Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_club.click()

    assert page.get_current_url() == 'https://www.labirint.ru/club/'


def test_change_region(web_browser):
    """13.Тестируем кнопку 'Регион' доставки."""
    page = Pages(web_browser)
    page.button_region.click()
    page.field_button_region.send_keys("Москва")
    page.click_region.click()

    assert page.message_region


def test_button_maps(web_browser):
    """14.Тестируем кнопку "Доставим завтра".Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.button_maps.click()

    assert page.get_current_url() == 'https://www.labirint.ru/maps/'
