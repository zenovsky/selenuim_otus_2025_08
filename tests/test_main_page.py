import allure

from page_objects.main_page import MainPage


@allure.epic("Главная страница")
@allure.feature("Загрузка главной страницы")
@allure.story("Проверка заголовка главной страницы")
@allure.severity(allure.severity_level.CRITICAL)
def test_main_title(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    main_page.check_title_main()


@allure.epic("Главная страница")
@allure.feature("Загрузка главной страницы")
@allure.story("Проверка отображения элементов хэдера")
@allure.severity(allure.severity_level.CRITICAL)
def test_header_elements(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    main_page.check_header_elements()


@allure.epic("Главная страница")
@allure.feature("Загрузка главной страницы")
@allure.story("Проверка отображения списка товаров на главной странице")
@allure.severity(allure.severity_level.CRITICAL)
def test_products(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    main_page.check_product_blocks()


@allure.epic("Главная страница")
@allure.feature("Загрузка главной страницы")
@allure.story("Проверка отображения основных блоков на главной странице")
@allure.severity(allure.severity_level.CRITICAL)
def test_key_blocks(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    main_page.check_key_blocks()


@allure.epic("Главная страница")
@allure.feature("Загрузка главной страницы")
@allure.story("Проверка отображения элементов футера")
@allure.severity(allure.severity_level.CRITICAL)
def test_footer(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    main_page.check_footer_elements()
