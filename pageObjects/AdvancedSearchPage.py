import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class AdvanceSearchPage:

    __language = "search_language"
    __state = "search_state"
    __license = "search_license"
    __followers = "search_followers"
    __stars = "search_stars"
    __searchBtn = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=30)

    def selectLanguage(self,language):
        self.wait.until(EC.visibility_of_element_located((By.ID,self.__language)))
        element = self.driver.find_element(By.ID,self.__language)
        sel = Select(element)
        sel.select_by_visible_text(language)

    def selectState(self,state):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__state)))
        element = self.driver.find_element(By.ID, self.__state)
        sel = Select(element)
        sel.select_by_visible_text(state)

    def selectLicense(self,license):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__license)))
        element = self.driver.find_element(By.ID, self.__license)
        sel = Select(element)
        sel.select_by_visible_text(license)

    def enterFollowers(self,followers):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__followers)))
        element = self.driver.find_element(By.ID, self.__followers)
        element.send_keys(followers)

    def enterStars(self,stars):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__stars)))
        element = self.driver.find_element(By.ID, self.__stars)
        element.send_keys(stars)

    def clickSearchBtn(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.__searchBtn)))
        element = self.driver.find_element(By.XPATH, self.__searchBtn)
        element.click()


