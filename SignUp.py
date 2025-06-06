from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time , pytest
import faker


faker = faker.Faker()
Pwd = faker.password()
@pytest.fixture(scope="module")

def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    time.sleep(5)
    yield driver
    driver.quit()

def test_signup(driver):
    driver.get("https://ecommerce.sebs.asia/user-register")
    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    print("Page fully loaded.")
    time.sleep(2)
    First_Name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='firstName']")))
    First_Name.send_keys(faker.first_name())
    time.sleep(2)
    Last_Name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='lastName']")))                                        
    Last_Name.send_keys(faker.last_name())
    time.sleep(2)
    Phone_Number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='phoneNo']")))
    Phone_Number.send_keys("9823456782")
    time.sleep(2)
    Email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='email']")))
    Email.send_keys(faker.email())
    time.sleep(2)
    Password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='password']")))
    Password.send_keys(Pwd)
    time.sleep(2)
    Confirm_Password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@id='confirmPassword']")))
    Confirm_Password.send_keys(Pwd)
    time.sleep(2)
    Sign_Up_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='p-3']")))
    Sign_Up_Button.click()
    time.sleep(2)
    if driver.current_url == "https://ecommerce.sebs.asia/verify-email":
        print("when signup is clicked it goes to email verify page")
    else:
        print("Error ! ")