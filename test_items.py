import time

def test_button_add_to_busket_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/12"
    browser.get(link)
    time.sleep(3)
    button = len(browser.find_elements_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert button == 1, 'no button'