#!/usr/bin/python3
# -*- encoding=utf8 -*-


import pytest
from pages.aliexpress import MainPage


def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)

    page.welcoming_popup_close_button.click()
    page.main_search = 'shotgun shells'
    page.search_start_button.click()
    page.coupon_popup_close_button.click()
    page.newest_sort_by.click()


    #page.computer_category_button.click()
    #page.coupon_popup_close_button.click()
    #page.go_to_the_cart_button.click()

    #todo DONT FORGET TO ASSERT POPUPS IN SMOKE