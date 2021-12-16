from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language_browser_link_button(browser):
    browser.get(link)
    button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary"))
    ).text
    text_result = ['Добавить в корзину', 'Ajouter au panier', 'Añadir al carrito']
    assert button in text_result, f"Кнопки <{button}> нет!"
