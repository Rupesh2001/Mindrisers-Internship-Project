from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time , pytest

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    time.sleep(5)
    yield driver
    driver.quit()

def test_country_swap(driver):
    driver.get("https://ecommerce.sebs.asia/")
    driver.find_element(By.XPATH,"//div[contains(@class,'select-order-country-btn d-flex align-items-center p-0 bg-warning px-2 rounded-5 hover-effect dropdown')]//img[@alt='country flag']").click()
    time.sleep(5)  # Wait for the page to load
    driver.find_element(By.XPATH,"//button[1]//div[1]//div[1]//img[1]").click()
    time.sleep(5)  # Wait for the page to load
    driver.find_element(By.XPATH,"//button[contains(@class,'btn btn-icon btn-topbar rounded-circle d-flex align-items-center btn btn-secondary')]//img[contains(@alt,'country flag')]").click()
    time.sleep(5)  # Wait for the page to load
    driver.find_element(By.XPATH,"//div[contains(@class,'country-name')][normalize-space()='United States']").click()
    time.sleep(5)  # Wait for the page to load
    driver.find_element(By.XPATH,"//input[@placeholder='Search our global search engine for products']").send_keys("Alpa Glass")
    time.sleep(5)  # Wait for the page to load
    driver.find_element(By.XPATH,"//h6[@class='font-level-2 mb-1 cursor-pointer']").click()
    time.sleep(5)
    

