import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import logging
import inspect

@pytest.mark.usefixtures("setup")
class Baseclass:
    
    def getlogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        filehandler = logging.FileHandler('teste2e_logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s ")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger

    def verifyelementpresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(By.LINK_TEXT, text)
        )

    def selectfromdropdown(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
        # dropdown.select_by_index(0)