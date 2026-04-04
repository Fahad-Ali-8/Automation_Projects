from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")

# checking if the home page loads or not
assert "Automation Exercise" in driver.title
print("Home page title is visible")

# clicking on signup/login button
wait = WebDriverWait(driver,10)
login_signup_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/login']")))
login_signup_btn.click()

# checking if the login to account text visible or not
login_to_account_text = wait.until(EC.visibility_of_element_located((By.XPATH,"//h2[text()='Login to your account']")))
assert login_to_account_text.is_displayed()
print("Login to account text is visible")

# typing email and password
email = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@data-qa='login-email']")))
email.send_keys("assassin41@gmail.com")

password = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@data-qa='login-password']")))
password.send_keys("Assassin_888")

# clicking on login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@data-qa='login-button']")))
login_btn.click()

# clicking on logout button
logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Logout']")))
logout_btn.click()

# Verify user is navigated to login page
wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Login to your account']")))
print("User navigated to login page")


time.sleep(5)
