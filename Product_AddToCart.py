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
    time.sleep(2)
    yield driver
    driver.quit()

def test_AddtoCart(driver):
    driver.get("https://www.ecommerce.sebs.asia/")
    #Hover the Elements 
    time.sleep(5)
    HoverElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='root']/div/div/div[contains(@class,'')]/div[contains(@class,'container-fixed d-flex flex-column flex-lg-row justify-content-between align-content-center align-items-center')]/ul[contains(@class,'align-content-center gap-4 list-unstyled text-uppercase align-items-center justify-content-start m-0 d-none d-lg-flex w-100')]/li[2]")))
    HoverElement.click()
    time.sleep(2)
    #Click on the Dropdown
    DropdownElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Home Kitchen & Dining')]")))
    DropdownElement.click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//body//div[@id='root']//div[contains(@class,'row')]//div[contains(@class,'row')]//div[2]//div[1]//img[1]").click()
    time.sleep(2)
    Add_to_cart_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'btn btn-dark w-100')]")))
    if Add_to_cart_btn.is_enabled():
        Add_to_cart_btn.click()
        print("Product added to cart successfully.")
    else:
        print("Add to cart button is not enabled.")