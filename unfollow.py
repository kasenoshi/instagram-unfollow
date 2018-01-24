"""This script unfollows all followings in entered Instagram account
selenium is used to do the web manipulation"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class InstagramUnfollower(object):
    """Class to unfollow all followings in Instagram"""

    def __init__(self):
        print "Enter username:",
        self.username = raw_input()
        print "Enter password:",
        self.password = raw_input()
        self.driver = webdriver.Chrome()

    def log_in(self):
        """Method to log in.

        Args:
        Returns:
        """
        driver = self.driver

        log_in = driver.find_element_by_link_text('Log in')
        log_in.click()

        username = driver.find_element_by_css_selector('input[name="username"]')
        username.send_keys(self.username)

        password = driver.find_element_by_css_selector('input[name="password"]')
        password.send_keys(self.password)

        button = driver.find_element_by_css_selector('button')
        button.click()

    def open_profile(self):
        """Method to open profile on Instagram.

        Args:
        Returns:
        """
        driver = self.driver

        stop_condition = EC.presence_of_element_located((By.LINK_TEXT, 'Profile'))
        profile = WebDriverWait(driver, 10).until(stop_condition)
        profile.click()

    def unfollow_all(self):
        """Method to unfollow all followings on Instagram.

        Args:
        Returns:
        """
        driver = self.driver

        try:
            while True:
                stop_condition = EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'following'))
                following = WebDriverWait(driver, 10).until(stop_condition)
                following.click()

                following_xpath = '//button[text()="Following"]'
                stop_condition = EC.presence_of_element_located((By.XPATH, following_xpath))
                WebDriverWait(driver, 10).until(stop_condition)
                followings = driver.find_elements(By.XPATH, following_xpath)
                for following in followings:
                    following.click()
                    # Instagram has limits for unfollowing
                    # (15 in 15 minutes, no more than 1000 per day)
                    time.sleep(60)

                close = driver.find_element(By.XPATH, '//button[text()="Close"]')
                close.click()

                driver.refresh()
        except TimeoutException:
            print "no followings left, program stops"
        finally:
            driver.quit()

    def run(self):
        """Method to run the steps to unfollow followings on Instagram.

        Args:
        Returns:
        """
        driver = self.driver
        driver.get('http://www.instagram.com')

        self.log_in()
        self.open_profile()
        self.unfollow_all()

if __name__ == '__main__':
    IU = InstagramUnfollower()
    IU.run()
