"""This script unfollows all followings in entered Instagram account
selenium is used to do the web manipulation"""
import json
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class InstagramUnfollower(object):
    """Class to unfollow all followings in Instagram"""

    def __init__(self):
        print("Loading config.json ...")
        with open('config.json') as json_file:
            data = json.load(json_file)
            self.username = data['username']
            self.password = data['password']
            self.skiplist = set()
            for i in data['skiplist']:
                self.skiplist.add(i)

        self.driver = webdriver.Chrome()

    def log_in(self):
        """Method to log in.

        Args:
        Returns:
        """
        driver = self.driver

        stop_condition = EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))
        WebDriverWait(driver, 10).until(stop_condition)

        username = driver.find_element_by_css_selector('input[name="username"]')
        username.send_keys(self.username)

        password = driver.find_element_by_css_selector('input[name="password"]')
        password.send_keys(self.password)

        button = driver.find_element_by_css_selector('button[type="submit"]')
        button.click()

    def open_profile(self):
        """Method to open profile on Instagram.

        Args:
        Returns:
        """
        driver = self.driver

        stop_condition = EC.presence_of_element_located((By.CSS_SELECTOR, 'span.coreSpriteKeyhole'))
        WebDriverWait(driver, 10).until(stop_condition)

        driver.get('http://www.instagram.com/' + self.username)

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
                print(following.text)
                num_following = int(re.search(r'\d+', following.text).group())
                following.click()

                following_xpath = '//button[text()="Following"]'
                unfollow_xpath = '//button[text()="Unfollow"]'

                stop_condition = EC.presence_of_element_located((By.XPATH, following_xpath))
                WebDriverWait(driver, 10).until(stop_condition)
                followings = driver.find_elements(By.XPATH, following_xpath)
                names = driver.find_elements(By.CSS_SELECTOR, 'a.notranslate')

                i = 0
                for following in followings:
                    # skip for names in skiplist
                    if names[i].text in self.skiplist:
                        print("In skiplist, skip " + names[i].text)
                        i += 1
                        continue
                    print("Unfollow " + names[i].text)
                    following.click()
                    stop_condition = EC.presence_of_element_located((By.XPATH, unfollow_xpath))
                    unfollow = WebDriverWait(driver, 10).until(stop_condition)
                    unfollow.click()
                    # Instagram has limits for unfollowing
                    # (15 in 15 minutes, no more than 1000 per day)
                    time.sleep(60)
                    i += 1

                # Stop if check followings
                if i == num_following:
                    break
                driver.refresh()
        except TimeoutException:
            print("no followings left, program stops")
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
