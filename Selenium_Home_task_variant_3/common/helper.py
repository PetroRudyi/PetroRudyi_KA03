import time

from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


delay_to_load_page = 10  # seconds

random_name = 'RandomName'

class GradestTest:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    def login_page(self):
        FormLoginXpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
        try:
            WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located((By.XPATH, FormLoginXpath)))
            self.driver.find_element(By.XPATH, FormLoginXpath).send_keys('Admin')
        except TimeoutException:
            print("Timed out waiting for page to load")

        FormPasswordXpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
        try:
            WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located((By.XPATH, FormPasswordXpath)))
            self.driver.find_element(By.XPATH, FormPasswordXpath).send_keys('admin123')
        except TimeoutException:
            print("Timed out waiting for page to load")

        ButtonLoginXpath = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
        try:
            WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located((By.XPATH, ButtonLoginXpath)))
            self.driver.find_element(By.XPATH, ButtonLoginXpath).click()
        except TimeoutException:
            print("Timed out waiting for page to load")

    def main_page(self):
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//span[text()="Admin"]'))).click()
        time.sleep(3)
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//span[contains(text(),"Job")]'))).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//a[contains(text(),"Pay Grades")]').click()
        time.sleep(3)
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//button[contains(.,"Add")]'))).click()

    def pay_grades_page(self):
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//input[not(@placeholder)]'))).send_keys(random_name)

        time.sleep(3)

        self.driver.find_element(By.XPATH, '//button[contains(.,"Save")]').click()

    def add_currency(self):
        time.sleep(3)

        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//button[contains(.,"Add")]'))).click()

        time.sleep(3)

        CurrencyXpath = f'/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/div/div/div[2]/div/div'
        #WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located((By.XPATH, CurrencyXpath)))
        #self.driver.find_element(By.XPATH, CurrencyXpath).click()
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, CurrencyXpath))).click()

        time.sleep(3)

        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//span[contains(text(),"AED")]'))).click()

        time.sleep(3)

        MinXpath = f'/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[1]/div/div[2]/input'
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, MinXpath))).send_keys('10')

        time.sleep(3)

        MaxXpath = f'/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div/div[2]/input'
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, MaxXpath))).send_keys('20')

        buttonSave = f'/html/body/div/div[1]/div[2]/div[2]/div[2]/form/div[3]/button[2]'
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, buttonSave))).click()


    def check_new_Currency(self):
        xpath_found_row = f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "10.00")]'
        found_row = WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, xpath_found_row)))

        found_row.find_element(By.XPATH, '//div[contains(., "10.00")]')
        found_row.find_element(By.XPATH, '//div[contains(., "20.00")]')

    def remove_Currency(self):
        DeleteButton = f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "10.00")]//i[@class="oxd-icon bi-trash"]'
        found_Currency = self.driver.find_element(By.XPATH, DeleteButton)
        time.sleep(3)
        found_Currency.find_element(By.XPATH, '//i[@class="oxd-icon bi-trash"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//button[contains(.,"Yes, Delete")]').click()
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, DeleteButton)
            assert 'Grades not removed'
        except NoSuchElementException:
            pass

    def delete_grades(self):
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//button[contains(.,"Cancel")]'))).click()
        time.sleep(3)
        DeleteButton = f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "{random_name}")]//i[@class="oxd-icon bi-trash"]'
        self.driver.find_element(By.XPATH, DeleteButton).click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, '//button[contains(.,"Yes, Delete")]').click()
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, DeleteButton)
            assert 'Element not removed'
        except NoSuchElementException:
            pass

        self.driver.close()
