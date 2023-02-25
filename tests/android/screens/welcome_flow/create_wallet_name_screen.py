from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.android.screens.base_screen import BaseScreen

class CreateWalletNameScreen(BaseScreen):

    def __init__(self, driver, location):
        self.driver = driver

        # Define the selectors for the elements on the login screen
        self.name_field = (AppiumBy.ID, "createWalletNameInput")
        self.continue_button = (AppiumBy.ID, "createWalletNameContinue")

        self.wait_for_screen(self.name_field)
        self.take_screenshot(location)


    def fill_wallet_name(self, wallet_name):
        name_field = WebDriverWait(self.driver, self.default_timeout).until(
            EC.element_to_be_clickable(self.name_field)
        )
        name_field.send_keys(wallet_name)

        self.take_screenshot('enterred_name')

        return self

    def click_continue(self):
        continue_button = WebDriverWait(self.driver, self.default_timeout).until(
            EC.element_to_be_clickable(self.continue_button)
        )
        continue_button.click()
