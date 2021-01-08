import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element_by_class_name("btn-add-to-basket"), "Button 'Add to basket' not found :("
