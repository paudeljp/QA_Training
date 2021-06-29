from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver')
driver.get('https://merolagani.com/ContactUs.aspx')
driver.maximize_window()
time.sleep(2)
contact_us_path = driver.find_element_by_xpath("//div[@class='panel-body text-center']")
contact_us_text = contact_us_path.text
print(contact_us_text)
time.sleep(2)
driver.quit()