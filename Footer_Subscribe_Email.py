from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time , pytest, faker

faker = faker.Faker()
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    time.sleep(5)
    yield driver
    driver.quit()

def test_Footer_Subscribe_Email_Valid(driver):
    driver.get("https://ecommerce.sebs.asia/")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 1000);") 
    time.sleep(2)
    Email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Your email address']")))
    Email_input.send_keys(faker.email())
    time.sleep(2)
    Subscribe_Btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    Subscribe_Btn.click()
    time.sleep(2)
    success_msg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@role='status']")))
    assert "Thank you for subscribing. You will receive our newsletters and updates." in success_msg.text

def test_Footer_Subscribe_Email_Invalid(driver):
    driver.get("https://ecommerce.sebs.asia/")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 1000);") 
    time.sleep(2)
    Email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Your email address']")))
    Email_input.send_keys(faker.email())
    time.sleep(2)
    Subscribe_Btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    Subscribe_Btn.click()
    time.sleep(2)
    failure_msg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='text-danger']")))
    assert "Invalid email address" in failure_msg.text