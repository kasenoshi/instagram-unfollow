import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstagramUnfollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_credential(self):
        print "Enter username:",
        self.username = raw_input()
        print "Enter password:",
        self.password = raw_input()

    def run(self):
        self.get_credential()

        driver = self.driver
        driver.get('http://www.instagram.com')

        log_in = driver.find_element_by_link_text('Log in')
        log_in.click()

        username = driver.find_element_by_css_selector('input[name="username"]')
        username.send_keys(self.username)

        password = driver.find_element_by_css_selector('input[name="password"]')
        password.send_keys(self.password)

        button = driver.find_element_by_css_selector('button')
        button.click()

        profile = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Profile'))
                )
        profile.click()

        try:
            while True:
                following = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'following'))
                        )
                following.click()

                WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//button[text()="Following"]'))
                        )
                followings = driver.find_elements(By.XPATH, '//button[text()="Following"]')
                for f in followings:
                    f.click()
                    time.sleep(60) # Instagram has limits for unfollowing (15 in 15 minutes, no more than 1000 per day)

                close = driver.find_element(By.XPATH, '//button[text()="Close"]')
                close.click()

                driver.refresh()

        finally:
            driver.quit()


if __name__ == '__main__':
    iu = InstagramUnfollower()
    iu.run()
