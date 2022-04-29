#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging


from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

logger = logging.getLogger(__name__)


class ChromeDriver(object):

    def __init__(self):
        self.driver = self.set_driver()

    def set_driver(self):
        options = ChromeOptions()
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities["acceptInsecureCerts"] = True
        options.add_argument("--window-size=950, 800")
        options.add_argument('--incognito')
        options.add_experimental_option("detach", True)

        return Chrome(executable_path=ChromeDriverManager().install(),
                        options=options,
                        desired_capabilities=capabilities)

    def close_driver(self):
        self.driver.close()
        self.driver.quit()

    def open_url(self, url):
        self.driver.get(url)
        

    def get_elements(self, target, elements):
        elements_ = self.driver.find_elements(By.CSS_SELECTOR, target)
        if not elements_:
            logger.error(
                f"Failed to get target. target: {target}", exc_info=True)
            return False

        elements.extend(elements_)

        return True

    def get_blocks(self, target):
    
        elements = []
        if self.get_elements(target, elements):
            blocks = elements

        return blocks

    def get_text_from_block(self, block, target):
        elements = block.find_elements(By.CSS_SELECTOR, target)
        if not elements:
            logger.error(
                "Failed to get target element!", exc_info=True)
            return ''

        return elements[0].text.replace( '\n' , '' )
    

    def get_url_from_block(self, block, target):
        elements = block.find_elements(By.CSS_SELECTOR, target)
        if not elements:
            logger.error(
                "Failed to get target element!", exc_info=True)
            return ''

        return elements[0].get_attribute("href")