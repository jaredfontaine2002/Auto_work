from selenium import webdriver
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Set the path to the Chrome driver
service = Service('/path/to/chromedriver')
driver = webdriver.Chrome(service=service)

# Navigate to the work website login page
driver.get("https://business.curated.com")

# Enter your email address
email_address = "jaredfontaine2002@gmail.com"
driver.find_element(By.NAME, "emailOrPhone").send_keys(email_address)
driver.find_element(By.NAME, "emailOrPhone").send_keys(Keys.ENTER)

# Click the Next button
# driver.find_element(By.CSS_SELECTOR, "button[data-testid='auth-submit-login']").click()

time.sleep(5)

code = input("Enter the 2-step verification code: ")
driver.find_element(By.ID, "text-field-20414844").send_keys(code)

time.sleep(5)

driver.find_element(By.XPATH, '/html/body').click()

time.sleep(5)

ul_list4 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div[1]/ul')

print('You have 60 seconds to scroll down now to the end of the page')

time.sleep(30)

print('Starting your job NOW!')


ul_list = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div[1]/ul')


counter = 1

li_elements = ul_list.find_elements(By.TAG_NAME, "li")
for li in li_elements:
    href = li.find_element(By.TAG_NAME, "a")
    href.click()
    # find text box
    text_field = driver.find_element(by=By., value="styles_tray__cP9Xr")
    # Insert the text "last day" into the text field
    text_field.send_keys("last day")
    # Press Enter
    #text_field.send_keys(Keys.ENTER)
    print(f"Href {counter} was clicked")
    counter += 1
    #time.sleep(2)

print("The ul list has been clicked 2")

#/html/body/div[1]/div[3]/main/div[2]/div[2]/div[1]/div/div/form/div/div