from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.fixture(scope="module")

def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    time.sleep(5)
    yield driver
    driver.quit()

def test_InvalidLogin(driver):
    driver.get("https://www.ecommerce.sebs.asia/login")
    time.sleep(2)
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter email']")))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Password']")))
    email_input.send_keys("Invalid Email") # Invalid email for testing
    password_input.send_keys("Sebs@1234") # Invalid password for testing
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign In']")))
    login_button.click()
    error_msg_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='status']")))
    error_msg = error_msg_element.text.strip()
    if error_msg == "User name or password is incorrect":
        print("Test Passed: Invalid login error message displayed correctly.")
    else:
        print("Test Failed: Expected an error message but got:", error_msg)
def test_validLogin(driver):
    driver.get("https://www.ecommerce.sebs.asia/login")
    time.sleep(2)
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter email']")))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Password']")))
    email_input.send_keys("themax123@gmail.com") # valid email for testing
    password_input.send_keys("Sebs@123") # valid password for testing
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign In']")))
    login_button.click()
    error_msg_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='status']")))
    error_msg = error_msg_element.text.strip()
    if error_msg == "Welcome!":
        print("Test Passed: Valid login successful, no error message displayed.")
    else:
        print("Test Failed: Expected no error message but got:", error_msg)
    
