from tests.android.screens.welcome_flow.welcome_screen import WelcomeScreen

from utils.base_test import BaseTestCase


class WelcomeScreenAndroidTest(BaseTestCase):

    def test_default_welcome_screen_is_shown(self):
        """
        Test case for printing 'Hello, world!' to the console.
        """
        self.logger.info("Starting 'Hello, world!' test...")

        welcome_screen = WelcomeScreen(self.driver, 'welcome_screen')
        welcome_screen.create_new_wallet().fill_wallet_name('test_wallet').click_continue()


        self.assertIn("Hello, world!", "")

        self.logger.info("'Hello, world!' test passed.")
