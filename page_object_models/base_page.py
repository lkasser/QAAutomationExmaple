from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config import environment

class BasePage:

    TIMEOUT = 30
    TIME = 30
    STEP = 0.5


    MODAL = (By.XPATH, '//div[contains(@class, "modal fade in")]')

    SEARCH_BAR_FIELD = (By.ID, '//txtsearch')

    URL = "https://www.google.com/"

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url=URL):
        self.driver.get(url)

    def wait_for_elem(self, loc, timeout=TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(loc)
            )
            return True
        except Exception as e:
            print('Unable to locate element by %s at %s \n %s' % (loc[0], loc[1], e))
            return False

    def wait_for_clickable(self, loc, timeout=TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(loc)
            )
            return True
        except Exception as e:
            print(f'Unable to click element by {loc[0]} at {loc[1]} \n {e}')
            return False

    def wait_for_visible (self, loc, timeout=TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(loc)
                )
            return True
        except Exception as e:
            print(f'Unable to confirm visibility of element by {loc[0]} at {loc[1]} \n {e}')


    def wait_for_modal(self):
        self.wait_for_elem(self.MODAL)

    def find_element(self, loc):
        elem = self.driver.find_element(*loc)
        return elem

    def find_elements(self, loc):
        elems = self.driver.find_elements(*loc)
        return elems

    def search_bar_input(self, input):
        if self.wait_for_elem(self.SEARCH_BAR_FIELD):
            search_bar_field = self.find_element(self.SEARCH_BAR_FIELD)
            search_bar_field.send_keys(input)

    def get_attribute(self, loc, attribute):
        if self.wait_for_elem(loc):
            elem = self.find_element(loc)
            return elem.get_attribute(attribute)

    def move_to(self, loc):
        elem = self.find_element(loc)
        move_to_loc = ActionChains(self.driver).move_to_element(elem).perform()
        return move_to_loc





