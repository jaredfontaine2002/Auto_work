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

# <input class="_18X13 absolute bottom-0 UQ_InG9v text-center" id="text-field-20414844" placeholder="0" type="number" size="1" min="0" max="9" autocomplete="one-time-code" value="">
# Enter your password

# click dropdown menu

# driver.find_element(By.CSS_SELECTOR, '.fOSQg52W').click()

# click archives

# click first element of the list

# href = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div[1]/ul/li[1]/a")

# href.click()

# Create go down the list of links then click on the lead neames count all the links click and insert a message

ul_list = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div[1]/ul')

ul_list2 =driver.find_element(By.XPATH, '/html/body')

while True:
    driver.execute_script(window.scrollTo(0, document.body.scrollHeight);
    time.sleep(1)

    # Check if there are more elements to load
    if not ul_list.is_displayed():
        break
# Wait for the new elements to load
# WebDriverWait(driver, 10).until(lambda: driver.find_elements(By.TAG_NAME, "li"))

counter = 1
#   for li in ul_list.find_elements(By.TAG_NAME, "li"):
#   href = li.find_element(By.TAG_NAME, "a")
#   href.click()
#   print(f"Href {counter} was clicked")
#   counter += 1
#   time.sleep(2)

# print("The ul list has been clicked")

try:
    for li in ul_list.find_elements(By.TAG_NAME, "li"):
        href = li.find_element(By.TAG_NAME, "a")
        href.click()
        print("Href {counter} was clicked")
        counter += 1
        # time.sleep(2)

except:
    # time.sleep(3)
    more_elements_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div[1]/ul/div/button').click()
    driver.execute_script("arguments[0].scrollIntoView();", more_elements_button)
    more_elements_button.click()
    # Wait for the new elements to load
    # WebDriverWait(driver, 10).until(lambda: driver.find_elements(By.TAG_NAME, "li"))

    # Print the number of new elements that were loaded
    # print(len(driver.find_elements(By.TAG_NAME, "li")))

    li_elements = ul_list.find_elements(By.TAG_NAME, "li")
    for li in li_elements:
        href = li.find_element(By.TAG_NAME, "a")
        href.click()
        print(f"Href {counter} was clicked")
        counter += 1
        # time.sleep(2)

print("The ul list has been clicked 2")

# click lead mail
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div/ul/li[1]/a/div[2]/div/div/div/div[1]').click()

# Insert message to lead
driver.find_element(By.XPATH, "//*[@id='deal']/div[3]/main/div[2]/div[2]/div[1]/div/div/form/div/div[1]/textarea[1]")

Last_day_message = "Hey {{customerFirstName}}, Unfortunately, We just got word that the Curated.com cycling division " \
                   "will be closing down on June 1.  If you need something tires, jerseys, a bike computer, etc contact " \
                   "me ASAP.  We also have a sale going on too.  If you want to keep in touch my personal email address " \
                   "is jaredfontaine2002@yahoo.com if you have any questions about bikes🚲🚵‍♂️ etc.  I am also on " \
                   "Instagram jaredfontaine2002.  Good luck and keep the wheels the right side up!"

driver.find_element(By.XPATH,
                    "//*[@id='deal']/div[3]/main/div[2]/div[2]/div[1]/div/div/form/div/div[1]/textarea[1]").send_keys(
    Last_day_message)

time.sleep(500)
# password = "Veganboy22!"
# driver.find_element("password").send_keys(password)

# Click the Next button
# driver.find_element_by_id("next").click()

# Wait for the 2-step verification prompt to appear
time.sleep(5)

# Enter the 2-step verification code


# Click the Verify button

# <div class="Sty3MQ0X">Archived</div>

# You should now be logged into your work website
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('hello')
