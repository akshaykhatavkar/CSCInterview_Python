from selenium import webdriver
from managers.PageObjectManager import PageObjectManager


def test_search_closed_repo(driverManager):
    driver = driverManager
    # driver = webdriver.Chrome()
    driver.get("https://github.com/")
    driver.maximize_window()

    poManager = PageObjectManager(driver)

    poManager.homePage.searchRepoWithText("react")
    poManager.searchPage.clickOnAdvanceSearchLink()
    poManager.advSearchPage.selectLanguage("JavaScript")
    poManager.advSearchPage.selectState("closed")
    poManager.advSearchPage.enterStars(">45")
    poManager.advSearchPage.enterFollowers(">50")
    poManager.advSearchPage.selectLicense("Boost Software License 1.0")
    poManager.advSearchPage.clickSearchBtn()
    ###
    poManager.searchPage.waitUntilAtleastOneRepo()
    noOfRepos = poManager.searchPage.getNumberOfRepos()
    assert noOfRepos == 1
    ###
    repoName = poManager.searchPage.getRepoNameAtLocation(0)
    assert repoName == "mvoloskov/decider"
    ###
    poManager.searchPage.clickOnSpecificRepo(0)
    readMeChars = poManager.repoPage.getSpecificCharsOfReadMe(300)
    print(readMeChars)
    ####
    driver.quit()


