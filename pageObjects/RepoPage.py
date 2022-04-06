from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class RepoPage:

    __readMe = "//div[@data-target='readme-toc.content']"

    def __init__(self,driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=30)

    def getSpecificCharsOfReadMe(self,noOfChars):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.__readMe)))
        element = self.driver.find_element(By.XPATH,self.__readMe)
        txt = element.text
        return txt[0:noOfChars]