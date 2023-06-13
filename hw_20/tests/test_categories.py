import time


def test_check_choose_categories(mainpage):
    mainpage.click_on_navbar()
    pick_subcategory = mainpage.choose_subcategory('Побутова техніка')
    time.sleep(1)
    pick_kitchen_technique_category = pick_subcategory.choose_kitchen_technique_category()
    time.sleep(1)


def test_check_footer_text(mainpage):
    assert mainpage.find_footer().text == '© Всі права захищені 1998-2023'


def test_open_header_page(mainpage):
    mainpage.choose_header_page('Магазини')
    assert mainpage.check_link('https://allo.ua/ua/offline_stores/')
    mainpage.choose_header_page('Акції')
    assert mainpage.check_link('https://allo.ua/ua/events-and-discounts/')
    mainpage.choose_header_page('АЛЛО Гроші')
    assert mainpage.check_link('https://allo.ua/ua/loyalty-program/')
    mainpage.choose_header_page('АЛЛО Обмін')
    assert mainpage.check_link('https://allo.ua/ua/tradein/')


def test_header_seller_subpages(mainpage):
    mainpage.choose_sellers_subpages('Доставка і оплата')
    assert mainpage.check_link('https://allo.ua/ua/help/shipment_payment/')
    mainpage.choose_sellers_subpages('Оплата чаcтинами')
    assert mainpage.check_link('https://allo.ua/ua/help/oplata-chastami/')
    mainpage.choose_sellers_subpages('Гарантія / Повернення')
    assert mainpage.check_link('https://allo.ua/ua/warranty_and_service/')


def test_logo_is_displayed(mainpage):
    mainpage.find_logo().is_displayed()


def test_return_to_home_page(mainpage):
    mainpage.choose_sellers_subpages('Доставка і оплата')
    mainpage.find_logo().click()
    assert mainpage.check_link('https://allo.ua/')


def test_check_login(mainpage, login_form):
    mainpage.click_on_profile()
    time.sleep(2)
    login_form.login()
    time.sleep(7)


def test_add_item_to_basket(mainpage, login_form, kitchen_technique):
    mainpage.click_on_profile()
    login_form.login()
    time.sleep(2)
    mainpage.click_on_navbar()
    time.sleep(3)
    pick_subcategory = mainpage.choose_subcategory('Побутова техніка')
    kitchen_technique.choose_kitchen_technique_category()


