�������
���������� ������� ����� ���� ��������-�������� � �������� ��� ���� 50-70 ������������������ ������ 
� �������������� PyTest � Selenium.
���-����� ��������� �� ��� �����:
Ozon,
Tmall,
Labirint.
��� ����� ���� ��������-��������, � ������� ���� ������� ���������� �������, � ����� ���������� ������ � 
���������� / ���������� �������.

����������
������ ����������� �������� �������� �������� ��� ��������-�������� Labirint.ru ��� ������������ ����������� �� �����.

�����:
 - � ����� tests:
     main_menu_center_up_tests.py - ����� ������������ ���� �������� � ����� ������� ��������
     main_menu_down_tests.py - ����� ������������ ���� ������� � ����� ������� ��������
     main_menu_right_tests.py - ����� ������ ������ � ����� ������� ��������
     social_footer_tests.py - ����� ������ �� ���������� ���� � ������� �� ������� ��������
     books_tests.py - ����� ����������� ������ � ���� �������� "�����" � ��������� �� ����������� ��������

 - � ����� Pages:
     base.py �������� ���������� Smart Page Object
     books_page.py �������� ����� ��� �������� "�����"
     elements.py �������� ����� ��� ����������� ��������� �� ���-���������
     main_page.py �������� ����� ��� "������� ��������"
 - ����� images �������� ��������� ���������� ������

������ ������:
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> tests/books_tests.py
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> tests/main_menu_center_up_tests.py
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> tests/main_menu_down_tests.py
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> tests/main_menu_right_tests.py
python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>/<chromedriver_file> tests/social_footer_tests.py

