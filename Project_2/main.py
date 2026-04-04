from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import random
import time
import os

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")

# Checking if the websites loads or not
assert "Automation Exercise" in driver.title
print("Home page is visible successfully")

# Clicking on login and signup button
wait = WebDriverWait(driver, 10)
login_signup_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Signup / Login']")))
login_signup_btn.click()


# # Checking if the new user Signup loads or not
login_to_account_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Login to your account']")))
assert login_to_account_text.is_displayed()
print("login text is visible")

# Typing email and password
email = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-qa='login-email']")))
email.send_keys("fahadali45621@gmail.com")

password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-qa='login-password']")))
password.send_keys("03239198902")

login_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@data-qa='login-button']")))
login_btn.click()

logged_in_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(., 'Logged in as')]")))
assert logged_in_text.is_displayed()
print("logged text is visible")


# Clicking on delete account button
delete_account_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/delete_account']")))
delete_account_btn.click()


# Checking if the account deleted text appears or not
account_deleted_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[@data-qa='account-deleted']")))
assert account_deleted_text.is_displayed()
print("Account deleted")

time.sleep(5)