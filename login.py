from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:5173/login")
    
    wait = WebDriverWait(driver, 20)
    email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='email' or @placeholder='Email']")))
    email_field.send_keys("jebs6@gmail.com")
    
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password' or @placeholder='Password']")))
    password_field.send_keys("Jebs6@12")
    
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login') or @type='submit']")))
    button.click()
    
    time.sleep(30)
    print("Login successful")

except Exception as e:
    print("Failed:", e)

finally:
    driver.close()
