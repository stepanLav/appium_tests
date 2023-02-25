from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.android.screens.base_screen import BaseScreen
from tests.android.screens.welcome_flow.create_wallet_name_screen import CreateWalletNameScreen

class WelcomeScreen(BaseScreen):

    def __init__(self, driver, location):
        self.driver = driver

        # Define the selectors for the elements on the login screen
        self.create_button = (AppiumBy.ID, "createAccountBtn")
        self.import_button = (AppiumBy.ID, "importAccountBtn")
        self.hardware_button = (AppiumBy.ID, "welcomeConnectHardwareWallet")
        self.watch_only_button = (AppiumBy.ID, "welcomeAddWatchWallet")

        self.wait_for_screen(self.create_button)
        self.take_screenshot(location)


    def create_new_wallet(self) -> CreateWalletNameScreen:
        create_button = WebDriverWait(self.driver, self.default_timeout).until(
            EC.element_to_be_clickable(self.create_button)
        )
        create_button.click()

        enter_wallet_name_screen = CreateWalletNameScreen(self.driver, 'create_wallet_enter_name')

        return enter_wallet_name_screen

    def import_wallet(self):
        import_button = WebDriverWait(self.driver, self.default_timeout).until(
            EC.element_to_be_clickable(self.import_button)
        )
        import_button.click()

    def connect_hardware_wallet(self):
        hardware_button = WebDriverWait(self.driver, self.default_timeout).until(
            EC.element_to_be_clickable(self.hardware_button)
        )
        hardware_button.click()

    def add_watch_only_wallet(self):
        watch_only_button = WebDriverWait(self.driver, self.default_timeout).until(
            EC.element_to_be_clickable(self.watch_only_button)
        )
        watch_only_button.click()
