#!/usr/bin/python3
# -*- encoding=utf8 -*-


from pages.aliexpress import MainPage


def test_check_apps_download_links(web_browser):
    """ Make sure apps download links are clickable and have proper addresses """

    # Opening main apps page
    page = MainPage(web_browser)
    page.welcoming_popup_close_button.click()
    page.get_apps_button.click()

    # Checking if iphone button is clickable and redirects to the proper page (and it is available)
    page.iphone_app_download_button.click()
    choose_app_window = page.switch_to_new_tab()  # Needed to initialize selenium in the new window and get back later
    # First we save window handle from the general apps page and THEN we are redirected to the new download window
    assert 'apps.apple.com/us/app/aliexpress' in page.get_current_url(), "Iphone app download link is invalid or down!"
    page.switch_back_from_new_tab(choose_app_window)

    # Checking if ipad button is clickable and redirects to the proper page (and it is available)
    page.ipad_app_download_button.click()
    page.switch_to_new_tab()
    assert 'apps.apple.com/app/aliexpress-for-ipad' in page.get_current_url(), "Ipad app download link is invalid or " \
                                                                               "down! "
    page.switch_back_from_new_tab(choose_app_window)

    # Checking if android button is clickable and redirects to the proper page (and it is available)
    page.android_app_download_button.click()
    page.switch_to_new_tab()
    assert 'play.google.com/store/apps' in page.get_current_url(), "Android app download link is invalid or down!"
    page.switch_back_from_new_tab(choose_app_window)
