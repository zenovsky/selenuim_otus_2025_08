import allure

from page_objects.catalog_page import CatalogPage


@allure.epic("Страница каталога")
@allure.feature("Загрузка страницы каталога")
@allure.story("Проверка отображения загаловка страницы каталога")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_title(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_catalog_title()

@allure.epic("Страница каталога")
@allure.feature("Загрузка страницы каталога")
@allure.story("Проверка отображения категорий товаров")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_categories_links(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_categories_links()

@allure.epic("Страница каталога")
@allure.feature("Загрузка страницы каталога")
@allure.story("Проверка отображения фильтров по поставщикам")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_filters_suppliers(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_filters_suppliers()

@allure.epic("Страница каталога")
@allure.feature("Загрузка страницы каталога")
@allure.story("Проверка отображения ссылок на поставщиков")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_filters_suppliers_links(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_filters_suppliers_links()

@allure.epic("Страница каталога")
@allure.feature("Загрузка страницы каталога")
@allure.story("Проверка отображения фильтров по брендам")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_filters_brands(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_filters_brands()

@allure.epic("Страница каталога")
@allure.feature("Загрузка страницы каталога")
@allure.story("Проверка отображения ссылок на бренды")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_filters_brands_links(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_filters_brands_links()

@allure.epic("Страница каталога")
@allure.feature("Загрузка страницы каталога")
@allure.story("Проверка отображения фильтров поиска")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_search_filters(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_search_filters()

@allure.epic("Страница каталога")
@allure.feature("Загрузка страницы каталога")
@allure.story("Проверка отображения подкатегорий товаров")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_subcategories(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_subcategories()

@allure.epic("Страница каталога")
@allure.feature("Загрузка страницы каталога")
@allure.story("Проверка отображения списка товаров")
@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_products_list(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_products_list()

@allure.epic("Страница каталога")
@allure.feature("Загрузка страницы каталога")
@allure.story("Проверка отображения контента страницы каталога")
@allure.severity(allure.severity_level.NORMAL)
def test_catalog_products_list_content(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_products_list_content()

