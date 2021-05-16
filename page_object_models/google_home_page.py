import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(__file__, "../..")))
from selenium.webdriver.common.by import By
from page_object_models.base_page import BasePage
from selenium.webdriver.common.keys import Keys

# PATHS
GOOGLE_SEARCH_BAR = By.XPATH, '//input[@class="gLFyf gsfi"]'
GMAIL_LINK = By.XPATH, '//a[@data-pid="23"]'
GOOGLE_IMAGES = By.XPATH, '//a[@data-pid="2"]'
GOOGLE_MENU = By.XPATH, '//a[@class="gb_D"]'

class GoogleHomePage(BasePage):

    def enter_text_in_search_field(self, input):
        if self.find_element(GOOGLE_SEARCH_BAR):
            search_bar_input = self.wait_for_clickable(GOOGLE_SEARCH_BAR)
            search_bar_input.send_keys(str(input))

    def click_gmail_link(self):
        if self.find_element(GMAIL_LINK):
            gmail_link = self.wait_for_clickable(GMAIL_LINK)
            gmail_link.click()

    def click_google_menu(self):
        if self.find_element(GOOGLE_MENU):
            google_menu_button = self.wait_for_clickable(GOOGLE_MENU)
            google_menu_button.click()




