from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:5173/register")
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    email_field = driver.find_element(By.ID, "email")
    button=driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/form/div/button")

    username_field.send_keys("kooks")

    email_field.send_keys("kooks@gmail.com")

    password_field.send_keys("K00ks@12")
    button.click()

    time.sleep(30)
    print("Registration successful")
    

except AssertionError as e:
    print("Failed:", e)

finally:
    driver.close()
