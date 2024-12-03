
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from datetime import datetime, timedelta
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

############################################################
#driver.get("https://www.google.co.in/")

# Replace these with your actual username and password
username = "deept@synopsys.com"
password = "Deepanraj@13"

# Replace this with the URL of the website you want to login to
website_url = "https://ifazility.com/Optdesk/Account/Login"

#open the website
driver.get(website_url)
driver.implicitly_wait(5)

# Find the login form elements and fill them in
username_field = driver.find_element(By.ID, "txtUserName")
username_field.send_keys(username)

password_field = driver.find_element(By.ID,"txtPassword")
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for a few seconds to let the page load
time.sleep(10)
booking_url = "https://ifazility.com/optdesk/Admin/WorkStationBook"
driver.get(booking_url)

# Wait for a few seconds to let the page load
time.sleep(10)

############################################################

# Find the date field element by its ID
state_date = driver.find_element(By.ID, 'searchfromdate')
# Calculate tomorrow's date
tomorrow = datetime.now() + timedelta(days=7)
tomorrow_date = tomorrow.strftime('%m/%d/%Y')  # Format as MM/DD/YYYY
# Update the value of the date field with tomorrow's date
driver.execute_script("arguments[0].setAttribute('value', arguments[1])", state_date, tomorrow_date)
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
submit_button.click()

#1041 1437 cubicl ws-151
# Set the desired values for X1 and Y1
#cube no 158
new_x1_value = "1172"
new_y1_value = "1583"

#cube no 151
#new_x1_value = "1070"
#new_y1_value = "1429"

x1_values = driver.find_element(By.ID, 'X1')
y1_values = driver.find_element(By.ID, 'Y1')
driver.execute_script("document.getElementById('X1').value = '{}'".format(new_x1_value))
driver.execute_script("document.getElementById('Y1').value = '{}'".format(new_y1_value))

# Identify the JavaScript function and its parameters
function_name = "checkbookingstatus_greyred"
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
# Close the browser
driver.quit()
