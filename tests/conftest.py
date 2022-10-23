import pytest
from pytest_bdd import given

from tests.framework.setup import Setup


@pytest.fixture(scope="session")
def configuration():
    """Get configuration options for the selenium webdriver.

    :return configuration: config values from JSON file
    """
    return Setup.get_configuration()


@pytest.fixture(scope="class")
def driver(configuration):
    """Initialize selenium Webdriver instance with options.

    :param configuration: selenium driver options fixture
    :return driver: selenium webdriver
    """
    driver = Setup.get_selenium_driver(configuration)

    yield driver

    driver.quit()


@given("the user navigates to the front page")
def user_navigates_to_front_page(driver, configuration):
    driver.get('%s' % (configuration['domain']))
    driver.maximize_window()
