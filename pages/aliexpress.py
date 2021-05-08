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

    # Autocomplete list items, shown when typing key words into the main search bar
    autocomplete_search_items = ManyWebElements(xpath='//span[@class="suggest_key"]')

    # Open the cart button
    go_to_cart_button = WebElement(xpath='//dl[contains(@class, "right-cart-button")]')

    # Get mobile apps button
    get_apps_button = WebElement(xpath='//div[@class="ng-item ng-mobile"]/a')

    # Corrected word in russian, when search bar gets wrong input with russian meaning in english
    # Just a part of the whole correcting message, other parts are different page objects
    russian_corrected_search_word = WebElement(xpath='//div[@class="spell-correction"]/div/span')


    # Language, currency and shipping drop-down menu

    # Language changing button, summons a drop down menu with language, currency and shipping settings
    # Can also be summoned by currency and flag buttons, I see no difference between these ways
    regional_settings_button = WebElement(xpath='//span[@class="language_txt"]')

    # In the previous drop-down menu current language button needs to be clicked to proceed to choosing languages
    current_language_button = WebElement(xpath='//span[@data-role="language-input"]/a')

    # English language option button in language selection
    english_language_button = WebElement(xpath='//a[@data-locale="en_US"]')

    # Save settings button, applies changes made to the currency, language and shipping choices
    save_settings_button = WebElement(xpath='//button[@data-role="save"]')


    # Listings

    # Items showed after a successful search by the main search bar and key words
    # With that xpath it doesn't select similar premium items at the bottom of the page unrelated to searches
    searched_found_items = ManyWebElements(xpath='//div[@class="place-container"]/a/img')

    # Titles for items listed after successful search of picking category
    titles_searched_found_items = ManyWebElements(xpath='//a[@class="item-title"]')


    # Sorting:

    # Sort by the best match (this is the default category)
    best_match_sort_by = WebElement(xpath='//span[@class="sort-item" and @ae_object_value="best_match"]')

    # Sort by the newest
    newest_sort_by = WebElement(xpath='//span[@class="sort-item" and @ae_object_value="date_added"]')

    # Sort by the number of orders
    orders_number_sort_by = WebElement(xpath='//span[@class="product-index" and @ae_object_value="number_of_orders"]')

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
