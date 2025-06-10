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

def test_Checking_footerElement(driver):
    driver.get("https://ecommerce.sebs.asia/")
    time.sleep(4)
    page_height = driver.execute_script("return document.body.scrollHeight")
    scroll_speed = 300
    scroll_iteration = int(page_height / scroll_speed)
    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        time.sleep(2)
    # Information
    shipping_and_Return = driver.find_element(By.XPATH,"//a[@class='text-decoration-none text-light custom-hover'][normalize-space()='Shipping & Returns']")
    shipping_and_Return.click()
    if driver.current_url == "https://ecommerce.sebs.asia/shipping-return":
        print("Shipping & Returns page is opened")
    else:
        print("Shipping & Returns page is not opened")
    time.sleep(2)
    driver.back()
    time.sleep(5)
    ContactUs = driver.find_element(By.XPATH,"//a[@class='text-decoration-none text-light custom-hover'][normalize-space()='Contact Us']")
    ContactUs.click()
    if driver.current_url == "https://ecommerce.sebs.asia/contact-us":
        print("Contact Us page is opened")
    else:
        print("Contact Us page is not opened")
    time.sleep(2)
    driver.back()
    time.sleep(5)
    blog = driver.find_element(By.XPATH,"//a[@class='text-decoration-none text-light custom-hover'][normalize-space()='Blog']")
    blog.click()
    if driver.current_url == "https://ecommerce.sebs.asia/blogs":
        print("Blog page is opened")
    else:
        print("Blog page is not opened")
    time.sleep(2)

   