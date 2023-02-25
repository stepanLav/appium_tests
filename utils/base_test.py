import unittest
import os
import json

from utils.logger import get_logger
from appium import webdriver
from typing import Dict

from utils.appium_utils import get_platform_config

class BaseTestCase(unittest.TestCase):
    """
    Base test case class with a logger and Appium driver.
    """
    screens_folder = "screens"
    logger = get_logger()

    @classmethod
    def setUpClass(cls) -> None:
        """
        Creates an Appium driver object before the test suite runs.
        """
        # Load configuration for the specified platform
        platform = os.getenv('PLATFORM', 'android')
        config = get_platform_config(platform)

        # Start Appium session
        cls.logger.info("Starting Appium session...")
        cls.driver = webdriver.Remote(config['appium_server'], config['capabilities'])
        cls.logger.info("Appium session started successfully.")

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Cleans up the Appium driver after the test suite runs.
        """
        cls.logger.info("Cleaning up...")
        cls.driver.quit()
        cls.logger.info("Done.")

    def setUp(self) -> None:
        """
        Resets the Appium driver before each test.
        """
        self.driver.reset()

    def get_platform_config(self, platform: str) -> Dict:
        """
        Returns the configuration for the specified platform.

        Args:
            platform (str): The name of the platform (e.g. 'android', 'ios').

        Returns:
            dict: The configuration for the specified platform.
        """
        config_file = f"{platform}_config.json"
        with open(config_file) as f:
            return json.load(f)
