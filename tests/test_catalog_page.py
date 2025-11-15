from page_objects.catalog_page import CatalogPage


def test_catalog_title(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()

def test_catalog_categories_links(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_categories_links()

def test_catalog_filters_suppliers(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_filters_suppliers()

def test_catalog_filters_suppliers_links(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_filters_suppliers_links()

def test_catalog_filters_brands(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_filters_brands()

def test_catalog_filters_brands_links(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_filters_brands_links()

def test_catalog_search_filters(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_search_filters()

def test_catalog_subcategories(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_subcategories()

def test_catalog_products_list(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_products_list()

def test_catalog_products_list_content(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog()
    catalog_page.check_products_list_content()

