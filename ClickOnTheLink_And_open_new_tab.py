from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://yahoo.com')
driver.maximize_window()

news_xpath = driver.find_element_by_xpath("//a[@data-rapid_p='30']")
action = ActionChains(driver)

action.key_down(Keys.CONTROL).click(news_xpath).key_up(Keys.CONTROL).perform()

time.sleep(6)
driver.quit()

