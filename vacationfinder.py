import configparser
import random
from time import sleep
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def random_sleep(minimum=3, maximum=5):
    return sleep(random.uniform(minimum, maximum))


def load_ini():
    ini_config = configparser.ConfigParser()
    ini_config.read('config.ini')
    account = {
        'membership_number': ini_config['Account']['membership_number'],
        'last_name': ini_config['Account']['last_name'],
        'user_agent': ini_config['Account']['user_agent'],
        'headless': ini_config['Account'].getboolean('headless')
    }
    return account


class VacationFinder:
    # vacation website URL
    WEBSITE_URL = "http://www.globalvacationnetwork.com/"
    # XPATHS
    EXPRESSWAYS_XPATH = "/html/body/table[1]/tbody/tr[2]/td[2]/a[2]"
    MEMBERSHIP_NUMBER_XPATH = f'//*[@id="ctl00_cphBody_tbLoginMembershipID"]'
    LAST_NAME_XPATH = f'//*[@id="ctl00_cphBody_tbLoginLastName"]'
    LOGIN_BUTTON_XPATH = f'//*[@id="ctl00_cphBody_bLoginSubmit"]'
    PAGE_NUMBER_COLUMN_XPATH = f'/html/body/table[3]/tbody/tr/td/form/div[3]/div/div/div[2]/table/tbody/tr[1]/td'

    def __init__(self):
        self.account = load_ini()
        self.driver = self.get_driver()

    def get_driver(self):
        options = webdriver.FirefoxOptions()
        if self.account.get("headless"):
            options.add_argument('--headless')

        profile = webdriver.FirefoxProfile()
        user_agent = self.account.get("user_agent")
        profile.set_preference("general.useragent.override", user_agent)

        driver = webdriver.Firefox(firefox_profile=profile, options=options, executable_path='geckodriver')
        driver.maximize_window()
        return driver

    def open_browser(self):
        return self.driver.get(VacationFinder.WEBSITE_URL)

    def login(self):
        try:
            self._random_wait_until_element_visible(xpath=VacationFinder.EXPRESSWAYS_XPATH)
            print("Logging in.")
            random_sleep()
            self._scroll_and_press(xpath=VacationFinder.EXPRESSWAYS_XPATH)
            print("...Pressed expressways button.")
            random_sleep()
            self._send_keys(xpath=VacationFinder.MEMBERSHIP_NUMBER_XPATH, keys=self.account.get("membership_number"))
            print("...Input membership number.")
            random_sleep()
            self._send_keys(xpath=VacationFinder.LAST_NAME_XPATH, keys=self.account.get("last_name"))
            print("...Input last name.")
            random_sleep()
            self._scroll_and_press(xpath=VacationFinder.LOGIN_BUTTON_XPATH)
            print("...Pressed login button.")
        except Exception as e:
            print(f'Error: {e}. Assuming already be logged in.')

    def get_number_of_pages(self):
        # get text from column that contains page numbers, strip [ and ] characters from it
        text = self._get_text_from_xpath(VacationFinder.PAGE_NUMBER_COLUMN_XPATH)
        # remove "[" and "]" from string
        text = text.replace('[', '').replace(']', '')
        # list of both page number integers. Ex: "Page 1 of 29" returns [1, 29]
        page_numbers = [int(word) for word in text.split() if word.isdigit()]
        max_page_number = page_numbers[-1]
        return max_page_number

    def _get_text_from_xpath(self, xpath):
        self._random_wait_until_element_visible(xpath)
        return self.driver.find_element_by_xpath(xpath).text

    def _scroll_and_press(self, xpath):
        self._random_wait_until_element_visible(xpath=xpath)
        element = self.driver.find_element_by_xpath(xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self._random_wait_until_element_visible(xpath=xpath)
        self.driver.execute_script("arguments[0].click();", element)

    def _send_keys(self, xpath, keys):
        self._random_wait_until_element_visible(xpath=xpath)
        self.driver.find_element_by_xpath(xpath).send_keys(keys)

    def _random_wait_until_element_visible(self, xpath, time=30):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((By.XPATH, xpath)))
