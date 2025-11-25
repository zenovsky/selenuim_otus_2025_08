import allure

from page_objects.product_card_page import ProductCardPage


@allure.epic("Карточка товара")
@allure.feature("Загрузка страницы карточки товара")
@allure.story("Проверка заголовка карточки товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_product_title(browser):
    product_card = ProductCardPage(browser)
    product_card.open_card()
    product_card.check_title_product_card()

@allure.epic("Карточка товара")
@allure.feature("Загрузка страницы карточки товара")
@allure.story("Проверка изображения товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_product_card_image(browser):
    product_card = ProductCardPage(browser)
    product_card.open_card()
    product_card.check_product_card_image()

@allure.epic("Карточка товара")
@allure.feature("Загрузка страницы карточки товара")
@allure.story("Проверка отображения веб-элементов страницы карточки товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_product_card_css_elements_present(browser):
    product_card = ProductCardPage(browser)
    product_card.open_card()
    product_card.check_css_elements()

@allure.epic("Карточка товара")
@allure.feature("Покупка товара")
@allure.story("Проверка отображения веб-элементов страницы карточки товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_product_card_xpath_elements_present(browser):
    product_card = ProductCardPage(browser)
    product_card.open_card()
    product_card.check_xpath_elements()
