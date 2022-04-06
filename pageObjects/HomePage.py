from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePage:

    __searchRepoText = "//input[@name='q']"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout=30)

    def searchRepoWithText(self,searchText):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.__searchRepoText)))
        element = self.driver.find_element(By.XPATH,value=self.__searchRepoText)
        element.send_keys(searchText)
        element.send_keys(Keys.ENTER)


