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

def test_Footer_brandAndCategory(driver):
    driver.get("https://ecommerce.sebs.asia/")
    time.sleep(4)
    page_height = driver.execute_script("return document.body.scrollHeight")
    scroll_speed = 300
    scroll_iteration = int(page_height / scroll_speed)
    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        time.sleep(2)

    Footer_Brand = driver.find_element(By.XPATH,"//a[normalize-space()='Konka']")
    Footer_Brand.click()
    time.sleep(5)
    if driver.current_url == "https://ecommerce.sebs.asia/brand/konka":
        print("Click on Konka ,  page is opened")
    else:
        print("Click on Konka ,  page is not opened")
    time.sleep(2)
    driver.back()
    time.sleep(2)

    Footer_Category = driver.find_element(By.XPATH,"//a[normalize-space()='Perfume & Fragrances']")
    Footer_Category.click()
    time.sleep(5)
    if driver.current_url == "https://ecommerce.sebs.asia/category/perfume-and-fragrances-000024":
        print("Click on Category ,  page is opened")
    else:
        print("Click on Category ,  page is not opened")
    time.sleep(2)