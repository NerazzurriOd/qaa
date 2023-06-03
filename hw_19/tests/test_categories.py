import time


def test_check_choose_categories(dashboard):
    dashboard.click_on_navbar()
    dashboard.choose_subcategory('Легкові')
    time.sleep(2)
    dashboard.click_on_navbar()
    dashboard.choose_subcategory('Комерційні')
    time.sleep(2)


def test_h1_text(dashboard):
    assert dashboard.find_title().is_displayed()


def test_click_logo_to_return_to_homepage(driver, dashboard):
    dashboard.find_title().click()
    assert driver.current_url == 'https://rst.ua/ukr/'


def test_footer(dashboard):
    assert dashboard.find_footer().text == '© 2006-2023 RST™'


# def test_add_to_favorite(dashboard):
#     dashboard.add_car_to_favorite()
#     time.sleep(2)
#     assert dashboard.count_of_added_car_to_favorite().text == '1'
#     time.sleep(2)


def test_delete_from_favorite(dashboard):
    dashboard.add_car_to_favorite()
    dashboard.click_on_navbar()
    dashboard.open_notebook()
    dashboard.delete_from_favorite()
    assert dashboard.count_of_deleted_cars_from_favorite().text == ''


def test_open_feedback_page(driver, feedback):
    feedback.open_feedback_page()
    assert driver.current_url == 'https://rst.ua/ukr/help/feedback.html'


def test_write_feedback(driver, feedback):
    feedback.open_feedback_page()
    feedback.find_text_area().click()
    feedback.write_feedback_text('Good morning')
    feedback.find_name_input()
    feedback.enter_name('Marcelo Brozovich')
    feedback.find_send_button().click()
    assert feedback.success_message('Дякуємо за відгук')
