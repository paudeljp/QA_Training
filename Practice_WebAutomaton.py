# from selenium import webdriver
# import time
# driver = webdriver.Chrome('./chromedriver')
# driver.maximize_window()
# driver.get('https://yahoo.com')
# driver.execute_script("window.open('');")
# driver.switch_to.window(driver.window_handles[1])
# driver.get('https://amazon.com')
# driver.switch_to.window(driver.window_handles[0])
# driver.get('https://facebook.com')
# driver.quit()


# from selenium import webdriver
# import time
# driver = webdriver.Chrome('./chromedriver')
# driver.maximize_window()
# driver.get('https://yahoo.com')
# news_link_xpath = driver.find_element_by_xpath("//a[@data-rapid_p='27']")
# news_link_xpath.click()
# time.sleep(2)
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import time
# driver = webdriver.Chrome('./chromedriver')
# driver.maximize_window()
# driver.get('https://yahoo.com')
# news_link_xpath = driver.find_element_by_xpath("//a[@data-rapid_p='28']")
# action = ActionChains(driver)
# action.key_down(Keys.CONTROL).click(news_link_xpath).key_up(Keys.CONTROL).perform()
#
# driver.switch_to.window(driver.window_handles[0])
#
# time.sleep(5)
# driver.quit()


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get('https://keystoneglobalnetwork.com/apply-now/')
time.sleep(3)
full_name_xpath = driver.find_element_by_xpath("//input[@name='text-765']")
full_name_xpath.send_keys("Ramesh Pandey")

email_xpath = driver.find_element_by_xpath("//input[@name = 'email-931']")
email_xpath.send_keys("test@gmail.com")

contact_xpath = driver.find_element_by_xpath("//input[@name = 'text-631']")
contact_xpath.send_keys("0123456789")

destination_dropdown = driver.find_element_by_xpath("//select[@name='menu-104']")
menu = Select(destination_dropdown)
menu.select_by_visible_text('Canada')

education_dropdown = driver.find_element_by_xpath("//select[@name='menu-105']")
menu = Select(education_dropdown)
menu.select_by_visible_text('Master')

submit_button = driver.find_element_by_xpath("//input[@value='Submit']")
submit_button.click()
time.sleep(10)

message_text = driver.find_element_by_xpath("//div[text()='Thank you for your message. It has been sent.']")
message = message_text.text

expected_message = 'Thank you for your message. It has been sent.'
print(expected_message)

try:
    assert expected_message == message
except AssertionError:
    print("Form didn't submit")
else:
    print("Form has been submitted successfully. Test passed")
time.sleep(10)
driver.quit()


