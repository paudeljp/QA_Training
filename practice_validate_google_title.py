from selenium import webdriver
import time
driver = webdriver.Chrome(r'C:\Users\jeeva\PycharmProjects\softwareqaclass\chromedriver')
driver.get('https://google.com')
driver.maximize_window()
time.sleep(2)
search_field = driver.find_element_by_xpath("//input[@name='q']")
search_field_text = search_field.send_keys('Nepal')
search_button = driver.find_element_by_xpath("//input[@name = 'btnK']")
search_button.submit()
actual_result = driver.title
print(actual_result)
expected_result = "Nepal - Google खोजी"
try:
    assert actual_result == expected_result
except AssertionError:
    print("Title not matched")
else:
    print("Title matched")
time.sleep(2)
driver.quit()

