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


    """ Header elements: """

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

    # Hot words, situated below the meain search bar. Unpredictable, they change constantly
    first_hot_word = WebElement(xpath='//div[@class="hot-words"]/a[1]')

    # Title of the aliexpress logo slogan, main banner in the top left corner
    logo_slogan_title = WebElement(xpath='//span[@class="logo-slogan"]')


    """ Account actions: """

    # User account icon, summons drop-down menu with 'Join' and 'Sign in' buttons and other account controls
    user_account_button = WebElement(xpath='//span[@class="user-account-port"]/a/i')

    # 'Sign in' button located in drop-down menu under user account icon when latter is clicked
    sign_in_button = WebElement(xpath='//a[@class="sign-btn"]')

    # Email address login field (account sign in pop-up)
    email_login_field = WebElement(id="fm-login-id")

    # Password login field (account sign in pop-up)
    password_login_field = WebElement(id="fm-login-password")

    # Finish signing in button (account sign in pop-up)
    finish_login_button = WebElement(xpath='//button[@data-role="save"]')


    """ Language, currency and shipping drop-down menu: """

    # Language changing button, summons a drop down menu with language, currency and shipping settings
    # Can also be summoned by currency and flag buttons, I see no difference between these ways
    regional_settings_button = WebElement(xpath='//span[@class="language_txt"]')

    # In the previous drop-down menu current language button needs to be clicked to proceed to choosing languages
    current_language_button = WebElement(xpath='//span[@data-role="language-input"]/a')

    # English language option button in language selection
    english_language_button = WebElement(xpath='//a[@data-locale="en_US"]')

    # Spanish language option button in language selection
    spanish_language_button = WebElement(xpath='//a[@data-locale="es_ES"]')

    # Korean language option button in language selection
    korean_language_button = WebElement(xpath='//a[@data-locale="ko_KR"]')

    # Turkish language option button in language selection
    turkish_language_button = WebElement(xpath='//a[@data-locale="tr_TR"]')

    # Current currency button, needed to be clicked to be changed
    current_currency_button = WebElement(xpath='//div[@data-role="switch-currency"]')

    # USD currency option button
    usd_currency_button = WebElement(xpath='//a[@data-currency="USD"]/em')

    # Save settings button, applies changes made to the currency, language and shipping choices
    save_settings_button = WebElement(xpath='//button[@data-role="save"]')


    """ Listings: """

    # Items showed after a successful search by the main search bar and key words
    # With these xpaths it doesn't select similar premium items at the bottom of the page unrelated to searches
    # And weirdly 'icon list' and 'icon gallery' view options for found items result in them needing different locators

    searched_found_items_gallery = ManyWebElements(xpath='//div[@class="place-container"]/a/img')
    searched_found_items_list = ManyWebElements(xpath='//div[@class="product-img"]/a/img')


    # Titles for items listed after successful search of picking category
    titles_searched_found_items = ManyWebElements(xpath='//a[@class="item-title"]')

    # Prices of the items
    item_listed_prices = ManyWebElements(xpath='//span[@class="price-current"]')


    """ Sorting: """

    # Sort by the best match (this is the default category)
    best_match_sort_by = WebElement(xpath='//span[@class="sort-item" and @ae_object_value="best_match"]')

    # Sort by the newest
    newest_sort_by = WebElement(xpath='//span[@class="sort-item" and @ae_object_value="date_added"]')

    # Sort by the number of orders
    orders_number_sort_by = WebElement(xpath='//span[@ae_object_value="number_of_orders"]')

    # Sort by the price (switches between 'lowest'and 'highest' arguments, first one is the default)
    price_sort_by = WebElement(xpath='//span[@class="sort-item" and @ae_object_value="price(lowest)"]')


    """ Pop-ups: """

    # Welcoming pop-up, asking for notifications permission (blocks other elements)
    welcoming_popup_close_button = WebElement(xpath='//div[@class="Sk1_X _1-SOk"]')

    # Welcoming pop-up icon title for assertion, should contain 'Allow notification' in different languages
    welcoming_popup_title = WebElement(xpath='//div[@class="_1u9ll"]')

    # Welcoming pop-up allow notifications button
    welcoming_popup_allow_button = WebElement(xpath='//div[@class ="_1ZwH_"]/div')

    # Welcoming pop-up new window text, should contain 'Allow notification' in different languages
    welcoming_popup_new_window_desc = WebElement(xpath='//div[@class ="_1dBWRLoGsivAFXXNtXSVjo"]')

    # Newcomer coupon gifting pop-up, shows up after clicking any items category (blocks other elements)
    coupon_popup_close_button = WebElement(xpath='//a[@class="next-dialog-close"]')

    # Coupon pop-up title for assertion
    coupon_popup_title = WebElement(xpath='//h4[@class="promotion-title"]')

    # Coupon pop-up accepting button
    coupon_popup_accept_button = WebElement(xpath='//a[@data-role="enter-promotion"]')

    # Adult pop-up title, opens up after searching for age restricted content (for example "dildo")
    adult_popup_title = WebElement(xpath='//div[@class="next-dialog-body"]')

    # Adult pop-up 'I am over 18' button
    adult_popup_accept_button = WebElement(xpath='//button[contains(@class, "law-18-dialog-yes")]')

    # Adult pop-up 'I am under 18' button
    adult_popup_dismiss_button = WebElement(xpath='//button[contains(@class, "law-18-dialog-no")]')


    """ Categories, currently situated on the left side of the page: """

    # Automobiles and motorcycles category button
    cars_category_button = WebElement(xpath='//dl[@data-spm="112"]/dt/span/a')

    # Computer and Office category button
    computer_category_button = WebElement(xpath='//a[contains(@href, "computer-office.html")]')

    # Sports and outdoor fun category button
    sports_category_button = WebElement(xpath='//dl[contains(@class, "cl-item-sports")]/dt/span/a')


    """ Applications download buttons (download_app_guide.htm page): """

    # iPhone App Store redirect button
    iphone_app_download_button = WebElement(xpath='//*[@id="o18fab9"]/div[1]/a')

    # iPad App Store redirect button
    ipad_app_download_button = WebElement(xpath='//*[@id="o18fab9"]/div[2]/a')

    # Android Google Play redirect button
    android_app_download_button = WebElement(xpath='//*[@id="o18fab9"]/div[3]/a')


    """ Item page: """

    # Add to the cart button, main one on the item page, next to the 'Buy Now' button
    # Page code shows another similar button with same class and structure, thus the long and ugly xpath
    add_to_cart_main = WebElement(xpath='//div[@class="product-action"]/span[@class="addcart-wrap"]/button')

    # Go to the cart button, located in a pop-up shown after successfully adding item to the cart
    go_to_cart_after_adding = WebElement(xpath='//div[@class="addcart-result-action"]/a/button')

    # List of possible options for ordering on the item page (size, color, etc)
    # The idea is - we will check if 8 option categories are available and if true click on the each first element
    # 4 for img options (color, set, accessories, etc) and 4 for txt (size, country of origin, etc)
    # TODO find a cleaner solution, for example via 'for i in options try click'

    img_ordering_optn_one = WebElement(xpath='//div[@class="sku-property"][1]/ul/li[1]/div/img')
    img_ordering_optn_two = WebElement(xpath='//div[@class="sku-property"][2]/ul/li[1]/div/img')
    img_ordering_optn_three = WebElement(xpath='//div[@class="sku-property"][3]/ul/li[1]/div/img')
    img_ordering_optn_four = WebElement(xpath='//div[@class="sku-property"][4]/ul/li[1]/div/img')

    txt_ordering_optn_one = WebElement(xpath='//div[@class="sku-property"][1]/ul/li[1]/div/span')
    txt_ordering_optn_two = WebElement(xpath='//div[@class="sku-property"][2]/ul/li[1]/div/span')
    txt_ordering_optn_three = WebElement(xpath='//div[@class="sku-property"][3]/ul/li[1]/div/span')
    txt_ordering_optn_four = WebElement(xpath='//div[@class="sku-property"][4]/ul/li[1]/div/span')


    """ Checkout page: """

    # Prices of items shown on the checkout page, individual for each item
    item_checkout_price = ManyWebElements(xpath='//span[@class="main-cost-price"]')

    # Titles of items shown on the checkout page
    first_cart_item_title = ManyWebElements(xpath='//a[@class="product-name-link"]')
