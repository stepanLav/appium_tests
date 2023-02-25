import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseScreen:

    default_timeout = 10

    def take_screenshot(self, filename):

        base_screens_directory = "screenshots/"

        if not os.path.exists(base_screens_directory):
            # create the directory if it doesn't exist
            os.mkdir(base_screens_directory)

        self.driver.save_screenshot(base_screens_directory + filename + ".png")

    def wait_for_screen(self, element_locator):
        WebDriverWait(self.driver, self.default_timeout).until(
            EC.visibility_of_element_located(element_locator))