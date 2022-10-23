"""Utility Class for Selenium Webdriver Setup Methods."""
import json
import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


class Setup:
    """Utility Class for Selenium Webdriver Setup Methods."""

    @staticmethod
    def get_configuration():
        """Load configuration from JSON file."""
        cfg_path = os.path.join(os.getcwd(), 'tests', 'config.json')
        with open(cfg_path) as configuration:
            data = json.load(configuration)
        print(data)
        return data

    @staticmethod
    def get_selenium_driver(configuration):
        """Initialize Selenium Webdriver with configuration options.

        :param configuration: selenium driver options
        """
        options = None

        if "Firefox" in configuration['browser']:
            options = FirefoxOptions()
            options.log.level = "trace"
        elif "Chrome" in configuration['browser']:
            options = ChromeOptions()

        if "Safari" not in configuration['browser']:
            options.set_capability('unhandledPromptBehavior', 'accept')
            options.add_argument('--ignore-ssl-errors=yes')
            options.add_argument('--ignore-certificate-errors')

            if configuration['environment'] == "server":
                for i in range(0, len(configuration['options'])):
                    options.add_argument(configuration['options'][i])
            elif configuration['environment'] == "standalone":
                pass
            else:
                raise Exception(
                    f"{configuration['environment']} is not supported."
                )

        if "Firefox" in configuration['browser']:
            driver = webdriver.Firefox(options=options)
        elif "Chrome" in configuration['browser']:
            driver = webdriver.Chrome(options=options)
        elif "Safari" in configuration['browser']:
            # Basic Auth with user and password in the url
            # does not work with Safari webdriver
            driver = webdriver.Safari()
        else:
            raise Exception(f"{configuration['browser']} is not supported.")

        return driver
