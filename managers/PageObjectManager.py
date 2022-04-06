from pageObjects.HomePage import HomePage
from pageObjects.SearchPage import SearchPage
from pageObjects.AdvancedSearchPage import AdvanceSearchPage
from pageObjects.RepoPage import RepoPage

class PageObjectManager:

    def __init__(self,driver):
        self.homePage = HomePage(driver)
        self.searchPage = SearchPage(driver)
        self.advSearchPage = AdvanceSearchPage(driver)
        self.repoPage = RepoPage(driver)
