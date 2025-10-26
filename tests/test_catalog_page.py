import pytest

from framework import wait_title, wait_element
from selenium.webdriver.common.by import By


def test_catalog_title(browser):
    browser.get(f'{browser.base_url}/2-home')
    wait_title("Home", browser)


@pytest.mark.parametrize("href_suffix", [
    ("/3-clothes"),
    ("/6-accessories"),
    ("/9-art"),
])
def test_catalog_categories_links(browser, href_suffix):
    browser.get(f'{browser.base_url}/2-home')
    wait_element(f"a[href$='{href_suffix}']", browser)

 
def test_catalog_filters_suppliers(browser):
    browser.get(f'{browser.base_url}/2-home')
    wait_element("#search_filters_suppliers", browser)


@pytest.mark.parametrize("href_suffix", [
    ("/supplier/2-accessories-supplier"),
    ("/supplier/1-fashion-supplier"),
])
def test_catalog_filters_suppliers_links(browser, href_suffix):
    browser.get(f'{browser.base_url}/2-home')
    wait_element(f"a[href$='{href_suffix}']", browser)    

  
def test_catalog_filters_brands(browser):
    browser.get(f'{browser.base_url}/2-home')
    wait_element("#search_filters_brands", browser)


@pytest.mark.parametrize("href_suffix", [
    ("/brands"),
    ("/brand/2-graphic-corner"),
    ("/brand/1-studio-design"),
])
def test_catalog_filters_brands_links(browser, href_suffix):
    browser.get(f'{browser.base_url}/2-home')
    wait_element(f"a[href$='{href_suffix}']", browser)


def test_catalog_search_filters(browser):
    browser.get(f'{browser.base_url}/2-home')
    wait_element("#search_filters", browser)


def test_catalog_subcategories(browser):
    browser.get(f'{browser.base_url}/2-home')
    wait_element("#subcategories", browser) 


def test_catalog_products_list(browser):
    browser.get(f'{browser.base_url}/2-home')
    wait_element(".products.row", browser)


@pytest.mark.parametrize("product_list_feature", [
    (".btn-unstyle.select-title"),
    (".wishlist-button-add"),
    (".next.js-search-link"),
])
def test_catalog_products_list_content(browser, product_list_feature):
    browser.get(f'{browser.base_url}/2-home')
    wait_element(product_list_feature, browser)

