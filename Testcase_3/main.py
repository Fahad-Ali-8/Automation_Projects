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
email.send_keys("randomemail@gmail.com")

password = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@data-qa='login-password']")))
password.send_keys("random password")

# clicking on login button
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@data-qa='login-button']")))
login_btn.click()

# checking if the email and password incorrect text is visible or not
email_password_incorrect = wait.until(EC.element_to_be_clickable((By.XPATH,"//p[text()='Your email or password is incorrect!']")))
assert email_password_incorrect.is_displayed()
print("email password incorrect text is visible")

time.sleep(5)
