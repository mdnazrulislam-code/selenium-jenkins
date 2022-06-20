import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_007(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_007, self).__init__(driver)

    def set_email(self, email):
        wait = WebDriverWait(self.driver, 60)
        loginEmail = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='txtemail']")))
        loginEmail.send_keys(email)

    def set_password(self, password):
        wait = WebDriverWait(self.driver, 60)
        loginEmail = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='txtpassword']")))
        loginEmail.send_keys(password)

    def click_sign_in(self):
        wait = WebDriverWait(self.driver, 60)
        loginEmail = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='btnsubmit']")))
        loginEmail.click()

    def selectState(self):
        wait = WebDriverWait(self.driver, 60)
        station = wait.until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//ul[@id='treePricing']//ul[@id='treePricing']//span[@class='statesName tradeclusters'][normalize-space()='New York']")))
        station.click()

    def selectStation(self):
        wait = WebDriverWait(self.driver, 60)
        newYork = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='checkbox'])[5]")))
        newYork.click()

    def showMetrics(self):
        wait = WebDriverWait(self.driver, 60)
        showMetrics = wait.until(EC.visibility_of_element_located((By.XPATH, "(//i[@title='Show Metrics'])[1]")))
        showMetrics.click()

    def closeMetrics(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        closeMetrics = wait.until(EC.visibility_of_element_located((By.XPATH, "(//i[@class='fa fa-chart-line ism lineevent active'])[1]")))
        closeMetrics.click()
