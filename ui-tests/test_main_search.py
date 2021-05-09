#!/usr/bin/python3
# -*- encoding=utf8 -*-


from pages.aliexpress import MainPage

def test_search_autocomplete(web_browser):
    """ Make sure search field autocompletes the key word"""

    page = MainPage(web_browser)
    page.welcoming_popup_close_button.click()
    page.main_search = keywords = 'honda'
    page.wait_page_loaded()  # Sometimes autocomplete doesn't work fast enough

    # Checking each (up to 10) of autocomplete options for the search keyword
    for autocomple_text in page.autocomplete_search_items.get_text():
        msg = 'Wrong autocomplete for the keyword "{}"'.format(autocomple_text)
        assert keywords in autocomple_text, msg
        # assert 'toyota' in autocomple_text, msg - To make it XFAIL.


def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)
    page.welcoming_popup_close_button.click()

    # Need to change regional language settings for consistency, or search titles can yield unexpected titles
    page.regional_settings_button.click()
    page.current_language_button.click()
    page.english_language_button.click()
    page.save_settings_button.click()
    # Need to wait for language changes to apply, or the next assert will be too fast and fail
    page.wait_page_loaded()

    keyword = 'cat'
    page.main_search = keyword
    page.search_start_button.click()
    assert keyword in page.get_current_url(), "Wrong search result url!"

    # Verifying visibility of found items, should be 60 for any popular aliexpress search.
    # This number is for one full page, both for 'list' and 'set' items view options.
    # If all 60 elements need to be asserted, don't forget to .scroll_down(), or only 8 will load.
    assert page.searched_found_items_gallery.count() > 0, "No items present after the search!"

    # Verifying that search result yields at least ONE item relevant to the keyword
    # Can't verify ALL titles, because some of them will always be a synonym, like Wheel - Roller
    counter = 0
    for title in page.titles_searched_found_items.get_text():
        if keyword in title.lower():
            counter += 1
        assert counter > 0, "No relevant items found!"


def test_russian_search_in_english_lang(web_browser):
    """Make sure russian search in english language recognised properly"""

    page = MainPage(web_browser)
    page.welcoming_popup_close_button.click()

    # Need to change regional language settings for consistency, or search titles can yield unexpected titles
    page.regional_settings_button.click()
    page.current_language_button.click()
    page.english_language_button.click()
    page.save_settings_button.click()
    page.wait_page_loaded()

    keywords = ['rjktcj', 'колесо', 'wheel']
    page.main_search = keywords[0]
    page.search_start_button.click()

    # Verifying that aliexpress recognised and properly corrected russian word search
    assert keywords[1] in page.russian_corrected_search_word.get_text(), "Russian word in english wasn't recognised!"

    # Verifying that at least one item is found
    assert page.searched_found_items_gallery.count() > 0, "No items present after the search!"

    # Verifying that search result yields at least ONE item relevant to the keyword
    # (either translated [1] or corrected [2], I've encountered both)
    # Can't verify ALL titles, because some of them will always be a synonym, like Wheel - Roller
    counter = 0
    for title in page.titles_searched_found_items.get_text():
        if keywords[1] in title.lower() or keywords[2] in title.lower():
            counter += 1
        assert counter > 0, "No relevant items found for the auto-corrected bad language input!"
