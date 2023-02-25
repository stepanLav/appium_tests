from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.android.screens.base_screen import BaseScreen
from tests.android.screens.welcome_flow.create_wallet_name_screen import CreateWalletNameScreen

class MnemonicScreen(BaseScreen):

    def __init__(self, driver, location):
        self.driver = driver

        # Define the selectors for the elements on the login screen
        self.alert_title = (AppiumBy.ID, "alertTitle")
        self.alert_cancel_button = (AppiumBy.ID, "button2")
        self.alert_ok_button = (AppiumBy.ID, "button1")

        self.wait_for_screen(self.alert_title)
        self.take_screenshot(location)


    def alert_click_cancel(self):
        alert_cancel_button = WebDriverWait(self.driver, self.default_timeout).until(
            EC.element_to_be_clickable(self.alert_cancel_button)
        )
        alert_cancel_button.click()

        create_wallet_name_screen = CreateWalletNameScreen(self.driver, 'create_wallet_name_after_deny_alert')

        return create_wallet_name_screen

    def alert_click_ok(self):
        alert_ok_button = WebDriverWait(self.driver, self.default_timeout).until(
            EC.element_to_be_clickable(self.alert_ok_button)
        )
        alert_ok_button.click()

        return self
