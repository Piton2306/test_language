import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language_browser_link_button(browser):
    browser.get(link)
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert button, "Кнопки 'добавить в корзину' нет!"
    # time.sleep(30)
