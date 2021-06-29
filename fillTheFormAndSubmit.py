from selenium import webdriver
import time
driver = webdriver.Chrome(r'C:\Users\jeeva\PycharmProjects\softwareqaclass\chromedriver')
driver.get('https://merolagani.com/ContactUs.aspx')
driver.maximize_window()
time.sleep(2)

#finding full name field path
full_name = driver.find_element_by_xpath("//input[@id = 'ctl00_ContentPlaceHolder1_txtFullName']")
full_name.send_keys('Jeevan Paudel')
time.sleep(2)
full_name_text = full_name.text

#finding mobile number field path
mobile_number = driver.find_element_by_xpath("//input[@id = 'ctl00_ContentPlaceHolder1_txtMobileNo']")
mobile_number.send_keys('9849935243')
time.sleep(2)
mobile_number_text = mobile_number.text

#finding email field path
email = driver.find_element_by_xpath("//input[@id = 'ctl00_ContentPlaceHolder1_txtEmail']")
email.send_keys('jeevanpaudel77@gmail.com')
time.sleep(2)
email_text = email.text

#finding contact us field path
contact_us_path = driver.find_element_by_xpath("//div[@class='panel-body text-center']")
contact_us_text = contact_us_path.text

#finding message fild path and sending varaiable
message = driver.find_element_by_xpath("//textarea[@id = 'ctl00_ContentPlaceHolder1_txtMessage']")
message.send_keys(contact_us_text)

#finding reset button path and clicking button
reset = driver.find_element_by_xpath("//button[@class = 'btn btn-default']")
time.sleep(2)
reset.click()

# submit = driver.find_element_by_xpath("//a[@id = 'ctl00_ContentPlaceHolder1_lbtnSubmit']")
time.sleep(2)
driver.quit()
