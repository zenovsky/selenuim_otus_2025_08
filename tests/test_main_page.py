from page_objects.main_page import MainPage


def test_main_title(browser):
    main_page = MainPage(browser)
    main_page.open_main()

def test_header_elements(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    main_page.check_header_elements()

def test_products(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    main_page.check_product_blocks()

def test_key_blocks(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    main_page.check_key_blocks()

def test_footer(browser):
    main_page = MainPage(browser)
    main_page.open_main()
    main_page.check_footer_elements()
