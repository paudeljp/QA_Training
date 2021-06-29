from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.google.com')
driver.maximize_window()
time.sleep(2)
search_box = driver.find_element_by_xpath("//input[@name = 'q']")
search_box.send_keys('Nepal')
search_button = driver.find_element_by_xpath("//input[@name = 'btnK']")
search_button.submit()
actual_result = driver.title
print(actual_result)
expected_result = "Nepal - Google खोजी"
try:
    assert expected_result == actual_result
except AssertionError:
    print("Tittle didn't match")
else:
    print("Tittle matched")
time.sleep(2)
driver.quit()




