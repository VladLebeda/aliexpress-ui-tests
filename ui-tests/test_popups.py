#!/usr/bin/python3
# -*- encoding=utf8 -*-


from selenium.common.exceptions import NoSuchElementException
from pages.aliexpress import MainPage


def test_welcoming_popup(web_browser):
    """ Make sure welcoming popup is shown and correct"""

    page = MainPage(web_browser)

    # Here we should get the welcoming pop-up
    assert page.welcoming_popup_close_button.is_visible(), "No welcoming pop-up!"
    assert page.welcoming_popup_title.get_text() == "Разрешить уведомления", "Wrong pop-up title!"

    # After allowing notifications via allow button new window opens up
    page.welcoming_popup_allow_button.click()

    # Asserting that new window has proper message
    page.switch_to_new_tab()
    assert page.welcoming_popup_new_window_desc.get_text() == "Разрешить уведомления", "Wrong pop-up (new window) " \
                                                                                       "title! "


def test_coupon_popup(web_browser):
    """ Make sure coupon popup is shown and correct"""

    page = MainPage(web_browser)
    page.welcoming_popup_close_button.click()

    # This coupon is available only in russian region, thus I don't change settings for it to show

    page.main_search = 'shotgun'
    page.search_start_button.click()

    # Checking if coupon pop-up title is correct (currently it shows only in russian)
    assert "ВПЕРВЫЕ НА ALIEXPRESS?" in page.coupon_popup_title.get_text(), "Wrong coutpon pop-up title text!"

    # Accepting the coupon opens up a new window
    page.coupon_popup_accept_button.click()
    page.switch_to_new_tab()

    # Asserting if user was linked to the proper page
    assert "Newuser_gifts" in page.get_current_url(), "Wrong coupon pop-up redirection!"


def test_accept_adult_popup(web_browser):
    """ Making sure that confirming age closes adult popup"""

    page = MainPage(web_browser)
    page.welcoming_popup_close_button.click()

    # Changing language to predictably working english
    page.regional_settings_button.click()
    page.current_language_button.click()
    page.english_language_button.click()
    page.finish_login_button.click()
    page.wait_page_loaded()

    page.main_search = 'dildo'
    page.search_start_button.click()
    page.wait_page_loaded()

    assert page.adult_popup_title.get_text() == "You must be at least 18 years of age to enter this section of " \
                                                "AliExpress.", "Wrong adult popups message! "

    page.adult_popup_accept_button.click()

    # If previous button is no longer clickable, adult pop-up was successfully closed
    # Need a 'try' block to avoid errors in report
    try:
        assert not page.adult_popup_accept_button.is_visible(), "Adult pop-up wasn't closed by age confirmation!"
    except NoSuchElementException:
        pass  # I expect that error, it is needed for assertion


def test_dismissing_adult_popup(web_browser):
    """ Making sure that dismissing adult pop-up returns previous page"""

    page = MainPage(web_browser)
    page.welcoming_popup_close_button.click()

    # Changing language to predictably working english
    page.regional_settings_button.click()
    page.current_language_button.click()
    page.english_language_button.click()
    page.finish_login_button.click()
    page.wait_page_loaded()

    keyword = 'dildo'
    page.main_search = keyword
    page.search_start_button.click()
    page.wait_page_loaded()

    assert page.adult_popup_title.get_text() == "You must be at least 18 years of age to enter this section of " \
                                                "AliExpress.", "Wrong adult popups message! "
    page.adult_popup_dismiss_button.click()

    # Asserting if we were redirected back to the original page, instead of proceeding with adult content
    assert keyword not in page.get_current_url(), "Redirecting from adult content for underaged has failed!"
