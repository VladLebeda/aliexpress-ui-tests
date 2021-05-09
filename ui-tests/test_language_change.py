#!/usr/bin/python3
# -*- encoding=utf8 -*-


from pages.aliexpress import MainPage

def test_switching_to_english(web_browser):
    """ Make sure switching to english changes language """

    page = MainPage(web_browser)
    page.welcoming_popup_close_button.click()

    # Changing language to english
    page.regional_settings_button.click()
    page.current_language_button.click()
    page.english_language_button.click()
    page.finish_login_button.click()
    page.wait_page_loaded()

    assert "Smarter Shopping, Better Living!" == page.logo_slogan_title.get_text(), "Switching to english lang failed!"

def test_switching_to_spanish(web_browser):
    """ Make sure switching to spanish changes language """

    page = MainPage(web_browser)
    page.welcoming_popup_close_button.click()

    # Changing language to spanish
    page.regional_settings_button.click()
    page.current_language_button.click()
    page.spanish_language_button.click()
    page.finish_login_button.click()
    page.wait_page_loaded()

    assert "¡Compra fácil, vive mejor!" == page.logo_slogan_title.get_text(), "Switching to spanish lang failed!"

def test_switching_to_korean(web_browser):
    """ Make sure switching to korean changes language """

    page = MainPage(web_browser)
    page.welcoming_popup_close_button.click()

    # Changing language to korean
    page.regional_settings_button.click()
    page.current_language_button.click()
    page.korean_language_button.click()
    page.finish_login_button.click()
    page.wait_page_loaded()

    assert "더 똑똑한 쇼핑, 더 나은 생활!" == page.logo_slogan_title.get_text(), "Switching to korean lang failed!"

