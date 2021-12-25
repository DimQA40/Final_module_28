Задание
Необходимо выбрать любой сайт интернет-магазина и написать для него 50-70 автоматизированных тестов 
с использованием PyTest и Selenium.
Веб-сайты магазинов на ваш выбор:
Ozon,
Tmall,
Labirint.
Или любой сайт интернет-магазина, в котором есть большое количество товаров, а также функционал поиска и 
сортировки / фильтрации товаров.

Вступление

Данный репозиторий содержит тестовые сценарии для интернет-магазина Labirint.ru без тестирования авторизации на сайте.

Файлы:
 - в папке tests:
     main_menu_center_up_tests.py - тесты центрального меню верхнего в шапке главной страницы
     
     main_menu_down_tests.py - тесты центрального меню нижнего в шапке главной страницы
     
     main_menu_right_tests.py - тесты кнопок справа в шапке главной страницы
     
     social_footer_tests.py - тесты ссылок на социальные сети в подвале на главной странице
     
     books_tests.py - тесты центральных кнопок в теле страницы "Книги" и переходов на последующие страницы

 - в папке Pages:
     base.py содержит библиотеку Smart Page Object
     books_page.py содержит класс для страницы "Книги"
     elements.py содержит класс для определения элементов на веб-страницах
     main_page.py содержит класс для "Главной страницы"
 - папка images содержит скриншоты выполнения тестов

Запуск тестов:

python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> tests/books_tests.py

python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> tests/main_menu_center_up_tests.py

python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> tests/main_menu_down_tests.py

python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> tests/main_menu_right_tests.py

python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> tests/social_footer_tests.py

