from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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

# Checking if the new user Signup loads or not
new_user_signup = wait.until(EC.element_to_be_clickable((By.XPATH, "//h2[text()='New User Signup!']")))
assert new_user_signup.is_displayed()
print("New user signup is visible")

# Typing name and email in new user
name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text']")))
name.send_keys("assassin")
email = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-qa='signup-email']")))
email.send_keys("assassin@gmail.com")

# Clicking on signup button
signup_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='signup-button']")))
signup_btn.click()

# Checking if the "Enter Account Information" text is visible or not
enter_acc_info_text = wait.until(EC.element_to_be_clickable((By.XPATH, "//b[normalize-space()='Enter Account Information']")))
assert enter_acc_info_text.is_displayed()
print("Enter Account Information is visible")

# FILLING ACCOUNT INFORMATION

## Title
title = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Mr']")))
title.click()
## Password
password = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
password.send_keys("Assassin_888")

## Date of birth
dob_day = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@data-qa='days']")))
select = Select(dob_day)
select.select_by_visible_text("9")

dob_month = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@data-qa='months']")))
select = Select(dob_month)
select.select_by_visible_text("March")

dob_year = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@data-qa='years']")))
select = Select(dob_year)
select.select_by_visible_text("2005")

# Clicking Checkboxs
check_box_1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='newsletter']")))
check_box_1.click()
check_box_2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='optin']")))
check_box_2.click()

# ADDRESS INFORMATION
## first and last name
add_first_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='first_name']")))
add_first_name.send_keys("Fahad")
add_last_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='last_name']")))
add_last_name.send_keys("Ali")

add_compnay_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='company']")))
add_compnay_name.send_keys("Assassin Lmtd")

address_1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='address1']")))
address_1.send_keys("central area ,Singapore")
address_2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='address2']")))
address_2.send_keys("central area ,Singapore")

# Selecting country
country = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='country']")))
select = Select(country)
select.select_by_visible_text("Singapore")

# Typing state
state = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='state']")))
state.send_keys("Central Area")

# Typing city
city = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='city']")))
city.send_keys("Central Area")

# typing zipcode
zipcode = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='zipcode']")))
zipcode.send_keys("43769")

# typing Phone Number
phone_number = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='mobile_number']")))
phone_number.send_keys("03239198902")

# Clicking on create account button
create_account_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-qa='create-account']")))
create_account_btn.click()

# Checking if the Account Created text appers or not
account_created_text = wait.until(EC.element_to_be_clickable((By.XPATH, "//h2[@data-qa='account-created']")))
assert account_created_text.is_displayed()
print("Account Created Succesfully")

# Clicking on Continue button
continue_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Continue']")))
continue_btn.click()

# Checking if the Logged in as username text appears or not
logged_in_text = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Logged in as')]")))
assert logged_in_text.is_displayed()
print("Logged in text is visible")

# Clicking on delete account button
delete_account_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/delete_account']")))
delete_account_btn.click()


# Checking if the account deleted text appears or not
account_deleted_text = wait.until(EC.element_to_be_clickable((By.XPATH, "//h2[@data-qa='account-deleted']")))
assert account_deleted_text.is_displayed()
print("Account deleted")

# Clicking on continue button
Continue_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-qa='continue-button']")))
Continue_btn.click()

time.sleep(5)   