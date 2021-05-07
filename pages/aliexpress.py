#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://best.aliexpress.com/'

        super().__init__(web_driver, url)


    # Header:

    # Main search bar
    main_search = WebElement(id='search-key')

    # Search-starting button (magnifying glass)
    search_start_button = WebElement(xpath='//input[@class="search-button"]')

    # Open the cart button, global
    go_to_the_cart_button = WebElement(xpath='//dl[contains(@class, "right-cart-button")]')

    # Get mobile apps button
    get_apps_button = WebElement(xpath='//div[@class="ng-item ng-mobile"]/a')


    # Sorting:

    # Sort by the best match (this is the default category)
    best_match_sort_by = WebElement(xpath='//span[@class="sort-item" and @ae_object_value="best_match"]')

    # Sort by the newest
    newest_sort_by = WebElement(xpath='//span[@class="sort-item" and @ae_object_value="date_added"]')

    # Sort by the number of orders
    orders_number_sort_by = WebElement(xpath='//span[@class="sort-item" and @ae_object_value="number_of_orders"]')

    # Sort by the price (switches between 'lowest'and 'highest' arguments, first one is the default)
    price_sort_by = WebElement(xpath='//span[@class="sort-item" and @ae_object_value="price(lowest)"]')

    # Pop-ups:

    # Welcoming pop-up, asking for notifications permission (blocks other elements)
    welcoming_popup_close_button = WebElement(xpath='//div[@class="Sk1_X _1-SOk"]')

    # Newcomer coupon gifting pop-up, shows up after clicking any items category (blocks other elements)
    coupon_popup_close_button = WebElement(xpath='//a[@class="next-dialog-close"]')

    # Age confirmation pop-up (shows up when any adult category is clicked?)
    confirm_age_button = WebElement(id="a2g0o.productlist.0.i34.6ca63e42Xkdl0j")

    # Categories, currently situated on the left side of the page:

    # Computer & Office category button
    computer_category_button = WebElement(xpath='//dl[contains(@class, "cl-item-computer")]')

    # Sports and outdoor fun category button
    sports_category_button = WebElement(xpath='//dl[contains(@class, "cl-item-sports")]')


    # Applications download buttons (download_app_guide.htm page):

    # iPhone App Store redirect button
    iphone_app_download_button = WebElement(xpath='//*[@id="o18fab9"]/div[1]/a')

    # iPad App Store redirect button
    ipad_app_download_button = WebElement(xpath='//*[@id="o18fab9"]/div[2]/a')

    # Android Google Play redirect button
    android_app_download_button = WebElement(xpath='//*[@id="o18fab9"]/div[3]/a')
