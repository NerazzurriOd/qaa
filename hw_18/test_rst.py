import time

from selenium.webdriver import Chrome, Keys


web_site = 'https://rst.ua/ukr/'


# 1. Check h1 of the main page
def test_check_h1():
    driver = Chrome('hw_18/drivers/chromedriver.exe')
    try:
        driver.maximize_window()
        driver.get(web_site)
        time.sleep(2)
        text_h1_locator = '//h1[contains(text(), "Авто базар - Авторинок України.")]'
        text_h1 = driver.find_element(by='xpath', value=text_h1_locator).text
        h1 = 'Авто базар - Авторинок України.'
        assert h1 == text_h1
    finally:
        driver.quit()


# 2. Check footer of the main page
def test_footer_text():
    driver = Chrome('hw_18/drivers/chromedriver.exe')
    try:
        driver.maximize_window()
        driver.get(web_site)
        time.sleep(2)
        text_footer_locator = '//footer/small[@class="text-grey"]'
        text_footer = driver.find_element(by='xpath', value=text_footer_locator).text
        text = '© 2006-2023 RST™'
        assert text == text_footer
    finally:
        driver.quit()


# 3. Check feedback page
def test_feedback_page():
    driver = Chrome('hw_18/drivers/chromedriver.exe')
    try:
        driver.maximize_window()
        driver.get(web_site)
        time.sleep(2)
        menu_locator = '//i[@class="icon-menu"][1]'
        feedback_button_locator = '//li/a[@href="//rst.ua/ukr/help/feedback.html"]'
        feedback_h4_text_locator = '//h4/b[contains(text(), "Написати тех. підтримці")]'
        menu = driver.find_element(by='xpath', value=menu_locator)
        menu.click()
        feedback_button = driver.find_element(by='xpath', value=feedback_button_locator)
        feedback_button.click()
        time.sleep(2)
        feedback_h4_text = driver.find_element(by='xpath', value=feedback_h4_text_locator).text
        feedback_text = 'Написати тех. підтримці'
        assert feedback_text == feedback_h4_text
    finally:
        driver.quit()


# 3. Check ability to write feedback
def test_ability_to_write_feedback():
    driver = Chrome('hw_18/drivers/chromedriver.exe')
    try:
        driver.maximize_window()
        driver.get(web_site)
        time.sleep(2)
        menu_locator = '//i[@class="icon-menu"][1]'
        feedback_button_locator = '//li/a[@href="//rst.ua/ukr/help/feedback.html"]'
        text_area_locator = '//textarea[@class="form-control"]'
        name_input_locator = '//input[@id="email"]'
        send_button_locator = '//button[contains(text(), "Відправити")]'
        success_message_locator = '//div[contains(text(), "Дякуємо за відгук")]'
        menu = driver.find_element(by='xpath', value=menu_locator)
        menu.click()
        feedback_button = driver.find_element(by='xpath', value=feedback_button_locator)
        feedback_button.click()
        time.sleep(2)
        text_area = driver.find_element(by='xpath', value=text_area_locator)
        text_area.click()
        text_area.send_keys('Hello from automation test')
        name_input = driver.find_element(by='xpath', value=name_input_locator)
        name_input.click()
        name_input.send_keys('Automation test')
        time.sleep(2)
        send_button = driver.find_element(by='xpath', value=send_button_locator)
        send_button.click()
        time.sleep(2)
        success_message = driver.find_element(by='xpath', value=success_message_locator).text
        message = 'Дякуємо за відгук'
        time.sleep(2)
        assert message == success_message
    finally:
        driver.quit()


# 4. Check add to favorite functionality
def test_add_to_favorite():
    driver = Chrome('hw_18/drivers/chromedriver.exe')
    try:
        driver.maximize_window()
        driver.get(web_site)
        time.sleep(2)
        favorite_button_locator = '//a[@class="bstar"][1]'
        added_car_to_favorite_locator = '//a[@data-bs-toggle="modal"][1]/i[@class ="bstar-s"][contains(text(), "1")]'
        favorite_button = driver.find_element(by='xpath', value=favorite_button_locator)
        favorite_button.click()
        time.sleep(1)
        added_car_to_favorite = driver.find_element(by='xpath', value=added_car_to_favorite_locator).text
        added_car = '1'
        assert added_car == added_car_to_favorite
    finally:
        driver.quit()


# 5. Check delete car from favorite list
def test_delete_from_favorite():
    driver = Chrome('hw_18/drivers/chromedriver.exe')
    try:
        driver.maximize_window()
        driver.get(web_site)
        time.sleep(2)
        favorite_button_locator = '//a[@class="bstar"][1]'
        menu_locator = '//i[@class="icon-menu"][1]'
        notebook_locator = '//a[@id="bstar"]/b[contains(text(), "Мій блокнот")][1]'
        delete_favorite_button_locator = '//a[@title="видалити з блокноту"]'
        deleted_car_from_favorite_locator = '//a[@data-bs-toggle="modal"]/i[contains(text(), "0")]'
        favorite_button = driver.find_element(by='xpath', value=favorite_button_locator)
        favorite_button.click()
        time.sleep(1)
        menu = driver.find_element(by='xpath', value=menu_locator)
        menu.click()
        notebook = driver.find_element(by='xpath', value=notebook_locator)
        notebook.click()
        delete_favorite_button = driver.find_element(by='xpath', value=delete_favorite_button_locator)
        delete_favorite_button.click()
        time.sleep(1)
        deleted_car_from_favorite = driver.find_element(by='xpath', value=deleted_car_from_favorite_locator).text
        deleted_car = ''
        assert deleted_car == deleted_car_from_favorite
    finally:
        driver.quit()
