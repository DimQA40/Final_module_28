import time
from Pages.main_page import Pages


def test_scroll_down(web_browser):
    """29.Тестируем прокрутку по вертикали вниз."""
    page = Pages(web_browser)
    page.scroll_footer()
    time.sleep(5)

    web_browser.save_screenshot('images/result3.png')


def test_link_vk(web_browser):
    """30.Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'ВКонтакте'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_VK.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://vk.com/labirint_ru'


def test_link_vk_kids(web_browser):
    """31.Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'ВКонтакте.Дети'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_VK_kids.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://vk.com/labirintdeti'


def test_link_youtube(web_browser):
    """32.Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'Ютьюб'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_youtube.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://www.youtube.com/user/labirintruTV'


def test_link_instagram(web_browser):
    """33.Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'Инстаграм'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_instagram.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://www.instagram.com/labirintru/'


def test_link_instagram_kids(web_browser):
    """34.Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'Инстаграм.Дети'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_instagram_kids.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://www.instagram.com/labirintdeti/'


def test_link_facebook(web_browser):
    """35.Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'Фейсбук'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_facebook.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://www.facebook.com/labirintru'


def test_link_classmates(web_browser):
    """36.Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'Одноклассники'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_classmates.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://ok.ru/labirintru'


def test_link_twitter(web_browser):
    """37.Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'Твиттер'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_twitter.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://twitter.com/labirint_ru'


def test_link_zen(web_browser):
    """38.Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'Дзен'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_zen.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://zen.yandex.ru/labirintru'


def test_link_t_me(web_browser):
    """39.Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'Телеграм'.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_t_me.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://t.me/labirintru'


def test_link_tiktok(web_browser):
    """40.Тестируем из группы 'Мы в соцсетях' в подвале переход по ссылке 'ТикТок '.
    Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_tiktok.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    time.sleep(5)

    assert page.get_current_url() == 'https://www.tiktok.com/@labirintru?'


