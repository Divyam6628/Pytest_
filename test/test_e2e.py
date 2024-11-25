from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pytest
from baseclass import Baseclass
from optimized_classes.homepage import homepage
# @pytest.mark.usefixtures("setup")
class Test_one(Baseclass):
    def test_e2e(self):
        log = self.getlogger()
        Homepage = homepage(self.driver)
        Homepage.shopitems().click()
        # self.driver.find_element(By.XPATH,"//a[text()='Shop']").click()
        cards = self.driver.find_elements(By.CSS_SELECTOR, '.card')
        log.info('All the cards are available now')
        for card in cards:
            if 'Blackberry' in card.text:
                card.find_element(By.CSS_SELECTOR, 'div button').click()
        log.info('Blackberry has been added to the cart')
        self.driver.find_element(By.CSS_SELECTOR, '.nav-item.active').click()
        self.driver.find_element(By.CSS_SELECTOR, '.form-control').clear()
        self.driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys('2')
        sleep  (3)
        self.driver.find_element(By.CSS_SELECTOR, '.btn.btn-success').click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '.validate').send_keys('in')
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.suggestions')))
        countries = self.driver.find_elements(By.CSS_SELECTOR, 'div.suggestions ul li')
        for country in countries:
            if country.text == 'India':
                country.click()
                break
        log.info('Choise of country is selected')
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.checkbox"))).click()
        self.driver.find_element(By.CSS_SELECTOR,'form input.btn').click()
        message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.alert.alert-success')))
        log.info('The Message recieved is '+message.text)
        assert "Success!" and "Thank you!" in message.text, "Fail at chekout"
        sleep(2)