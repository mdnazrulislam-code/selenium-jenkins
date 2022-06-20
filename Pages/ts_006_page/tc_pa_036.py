import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BasePage.HomePage import HomePage


class tc_pa_036(HomePage):

    def __init__(self, driver):
        self.driver = driver
        super(tc_pa_036, self).__init__(driver)

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

    def showMetrics(self):
        wait = WebDriverWait(self.driver, 60)
        metrics = wait.until(EC.visibility_of_element_located((By.XPATH, "(//i[@title='Show Metrics'])[1]")))
        self.driver.execute_script("arguments[0].click();", metrics)

    def marginFuel(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        margin = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='text'][@class='highcharts-title'])[12]")))
        margin.click()

    def zoom3m(self):
        wait = WebDriverWait(self.driver, 60)
        zoom = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[name()='text'][contains(text(),'3m')])[1]")))
        zoom.click()

    def premMargin(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        prem = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='mmfch'][normalize-space()='PREM'])[1]")))
        self.driver.execute_script("arguments[0].click();", prem)

    def premMarginFuelUncheck(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        prem = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Show PREM Margin Fuel']")))
        self.driver.execute_script("arguments[0].click();", prem)

    def premMarginFuelCheck(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        prem = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Show PREM Margin Fuel']")))
        self.driver.execute_script("arguments[0].click();", prem)

    def premCpgUnCheck(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        cpg = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Show CPG']")))
        self.driver.execute_script("arguments[0].click();", cpg)

    def premCpgCheck(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 60)
        cpg = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Show CPG']")))
        self.driver.execute_script("arguments[0].click();", cpg)



