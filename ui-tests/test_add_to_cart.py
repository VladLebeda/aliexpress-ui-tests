#!/usr/bin/python3
# -*- encoding=utf8 -*-

import time
from pages.aliexpress import MainPage

def test_add_item_to_cart(web_browser):
    """ Make sure user can add item to the cart """

    page = MainPage(web_browser)
    page.welcoming_popup_close_button.click()

    # Changing language to predictably working english and currency to USD for the future assertion
    page.regional_settings_button.click()
    page.current_language_button.click()
    page.english_language_button.click()
    page.current_currency_button.click()
    page.usd_currency_button.click()
    page.finish_login_button.click()
    page.wait_page_loaded()

    # TODO Disabled, because aliexpress restricts accounts without linked phone number, find workaround!
    # Logging into existing account (credentials.py)
    #page.user_account_button.click()
    #page.sign_in_button.click()
    #page.email_login_field.send_keys()
    #page.password_login_field.send_keys()
    #page.finish_login_button.click()

    page.main_search = 'car'
    page.search_start_button.click()
    page.orders_number_sort_by.click()
    page.wait_page_loaded()

    # Storing first found item's price for the future assertion
    first_listing_price = page.item_listed_prices.get_text()[0]
    # Also storing its title (aliexpress uses weird long titles)
    first_listing_title = page.titles_searched_found_items.get_text()[0]

    # Clicking on the first found item, it opens up its page in a new window which need control switching
    page.searched_found_items_gallery[0].click()
    page.switch_to_new_tab()

    # Can't add some items to the cart without tagging options (clothes size, color, origin country, etc).
    # Each item can have different options, and search results are unpredictable.
    # AND these option can be either img or txt, each needing different locators
    # The only errors I expect here are 'no such element', thus pass is safe I think
    try:
        page.img_ordering_optn_one.scroll_to_element().click()
        page.img_ordering_optn_two.scroll_to_element().click()
        page.img_ordering_optn_three.scroll_to_element().click()
        page.img_ordering_optn_four.scroll_to_element().click()

        page.txt_ordering_optn_one.scroll_to_element().click()
        page.txt_ordering_optn_two.scroll_to_element().click()
        page.txt_ordering_optn_three.scroll_to_element().click()
        page.txt_ordering_optn_four.scroll_to_element().click()
    except:
        pass
    time.sleep(10000)
    page.add_to_cart_main.click()
    page.go_to_cart_after_adding.click()
    first_cart_item_price = page.item_checkout_price.get_text()[0]

    # Asserting that the price is the same as well as the item itself
    assert first_listing_price == first_cart_item_price, "Wrong price of a single added item in the cart!"
    # Similar assertion of item's title
    assert first_listing_title == first_cart_item_title, "Wrong title of a single added item in the cart!"

    time.sleep(10000)







