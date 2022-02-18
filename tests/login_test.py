import time
from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils

@pytest.fixture(scope="session")
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C://Users//Haseeb Ahmed//PycharmProjects//pythonProject//Driver//chromedriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("test completed")

def test_login(test_setup):
    driver.get(utils.URL)
    login = LoginPage(driver)
    login.enter_username(utils.USERNAME)
    login.enter_password(utils.PASSWORD)
    login.click_login()


    #driver.find_element_by_id("txtUsername").send_keys("Admin")
    #driver.find_element_by_id("txtPassword").send_keys("admin123")
    #driver.find_element_by_id("btnLogin").click()

def test_logout(test_setup):
    home = HomePage(driver)
    home.click_welcome()
    home.click_logout()

    #driver.find_element_by_id("welcome").click()
    #driver.find_element_by_link_text("Logout").click()










