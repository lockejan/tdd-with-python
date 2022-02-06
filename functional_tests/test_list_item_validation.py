from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the homepage and accidentally tries to submit
        # an empty list item. She hits Enter on the empty inputbox.
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # The browser intercepts the request, and does not load the list page
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:invalid'))

        # She tries again with some text for the item, which now works
        self.get_item_input_box().send_keys('Buy coffee beans')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:valid'))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy coffee beans')

        # Perversely, she now decides to submit a second blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Again, the browser will not comply
        self.wait_for_row_in_list_table('1: Buy coffee beans')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:invalid'))

        # And she can corret it by filling some text in
        self.get_item_input_box().send_keys('Brew coffee')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy coffee beans')
        self.wait_for_row_in_list_table('2: Brew coffee')

    def test_cannot_add_duplicate_items(self):
        # Edith goes to the home page and starts a new list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Buy coffee beans')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy coffee beans')

        # She tries to enter the same item again
        self.get_item_input_box().send_keys('Buy coffee beans')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # She sees a helpful error message
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You've already got this in your list"))
