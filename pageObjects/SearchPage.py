from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchPage:

    __advanceSearchLink = "//a[text()='Advanced search']"
    __allRepoLinks = "//a[@class='v-align-middle']"

    def __init__(self,driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=30)

    def clickOnAdvanceSearchLink(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.__advanceSearchLink)))
        self.driver.find_element(By.XPATH,self.__advanceSearchLink).click()

    def waitUntilAtleastOneRepo(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.__allRepoLinks)))

    def getNumberOfRepos(self):
        elemenets = self.driver.find_elements(By.XPATH,self.__allRepoLinks)
        return len(elemenets)

    def getRepoNameAtLocation(self,location):
        elemenets = self.driver.find_elements(By.XPATH, self.__allRepoLinks)
        return elemenets[location].text

    def clickOnSpecificRepo(self,location):
        elemenets = self.driver.find_elements(By.XPATH, self.__allRepoLinks)
        elemenets[location].click()




