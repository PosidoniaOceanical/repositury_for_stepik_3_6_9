import pytest
import time
from selenium import webdriver


def test_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert len(button) > 0, 'Кнопка "Add to basket" не найдена.'
