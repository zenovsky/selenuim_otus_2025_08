from page_objects.product_card_page import ProductCardPage


def test_product_title(browser):
    product_card_page = ProductCardPage(browser)
    product_card_page.open_card()

def test_product_card_image(browser):
    product_card_page = ProductCardPage(browser)
    product_card_page.open_card()
    product_card_page.check_product_card_image()

def test_product_card_css_elements_present(browser):
    product_card_page = ProductCardPage(browser)
    product_card_page.open_card()
    product_card_page.check_css_elements()

def test_product_card_xpath_elements_present(browser,):
    product_card_page = ProductCardPage(browser)
    product_card_page.open_card()
    product_card_page.check_xpath_elements()
