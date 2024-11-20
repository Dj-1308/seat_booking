# packages
from selenium import webdriver
from datetime import datetime, timedelta

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

import time



# Replace these with your actual username and password
username = "deept@synopsys.com"
password = "Deepanraj@13"

## Automation Start ##

# Optdesk Login page URL
website_url = "https://ifazility.com/Optdesk/Account/Login"


# Initialize the webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# Open the website
driver.get(website_url)

# Find the login form elements and fill them in
username_field = driver.find_element(By.ID, "txtUserName")
username_field.send_keys(username)
password_field = driver.find_element(By.ID,"txtPassword")
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for a few seconds to let the page load
time.sleep(2)

# Optdesk booking page URL
booking_url = "https://ifazility.com/optdesk/Admin/WorkStationBook"
driver.get(booking_url)

# Wait for a few seconds to let the page load
time.sleep(2)

# Find the date field element by its ID
start_date = driver.find_element(By.ID, 'searchfromdate')
# Calculate tomorrow's date
tomorrow = datetime.now() + timedelta(days=7)
tomorrow_date = tomorrow.strftime('%m/%d/%Y')  # Format as MM/DD/YYYY

# Update the value of the date field with tomorrow's date
driver.execute_script("arguments[0].setAttribute('value', arguments[1])", start_date, tomorrow_date)

# Find the date field element by its ID
end_date = driver.find_element(By.ID, 'searchtodate')

# Update the value of the date field with tomorrow's date
driver.execute_script("arguments[0].setAttribute('value', arguments[1])", end_date, tomorrow_date)

# Find the dropdown element by its ID
dropdown = driver.find_element(By.ID,"dtsearchfrom")

# Create a Select object from the dropdown element
select = Select(dropdown)

#Select by value
select.select_by_value("10:40:00")

#clicking the select button
submit_button = driver.find_element(By.ID, 'btnsearch')

##### debug #####
print("text_start_data:",start_date)
print("text_tomorrow_data:",tomorrow_date)
print("text_end_data:",end_date)

# Find the elements and get their values
starttime_element = driver.find_element(By.ID,"dtsearchfrom")
starttime = starttime_element.get_attribute("value")
endtime_element = driver.find_element(By.ID,"dtsearchto")
endtime = endtime_element.get_attribute("value")
date_element = driver.find_element(By.ID,"searchfromdate")
date = date_element.get_attribute("value")
enddate_element = driver.find_element(By.ID,"searchtodate")
enddate = enddate_element.get_attribute("value")
# Identify the JavaScript function and its parameters
#function_name = "myFunction"
# Execute the JavaScript function using Selenium
#driver.execute_script(f"{function_name}('{starttime}', '{endtime}', '{date}', '{enddate}')")
new_x2_value =0
new_y2_value =0
# Execute the JavaScript function using Selenium
driver.execute_script(f"{function_name}({new_x1_value},{new_x2_value}, {new_y1_value},{new_y2_value}, '{date}', '{enddate}', '{starttime}', '{endtime}')")
time.sleep(5)
# Find the dropdown element by its ID
dropdown_1 = driver.find_element(By.ID,"tmestart")
# Create a Select object from the dropdown element
select_1 = Select(dropdown_1)
#Select by value
select_1.select_by_value("10:40:00")
save_button = driver.find_element(By.XPATH, "//button[contains(@onclick, 'saveworkstation')]")
# Click the "Save" button
save_button.click()
time.sleep(10)
confirm_button = driver.find_element(By.XPATH, "//button[text()='Click to Confirm']")
# Click the "Click to Confirm" button
confirm_button.click()
error_message = "successfully booked the 158 cubical to you please cross check once."
#send_email("Cubical booking success Notification", error_message)
time.sleep(50)
