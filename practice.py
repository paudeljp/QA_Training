import pandas as pd
from selenium import webdriver

def read_excel():
    reader = pd.read_excel('test_case/TestCase.xlsx')
    for row,column in reader.iterrows():
        sn = column['SN']
        execute_flag = column['Execute_FLAG']
        test_summery = column['Test Summary']
        xpath = column['Xpath']
        action = column['Action']
        value = column['Value']
        if execute_flag != 'N':
            action_defination(sn,test_summery,xpath,action,value)
        else:
            result = "NOT TESTED"
            remarks = "Test was skipped due to N flag"
            print(result,remarks)

def action_defination(sn,test_summary,xpath,action,value):
    try:
        if action == 'open_browser':
            open_browser(value)
            result = "PASS"
            remarks = ""
        elif action == 'open_url':
            result,remarks = open_url(driver,value)
        elif action == 'click':
            result,remarks = click_function(driver,xpath)

        else:
            result = 'FAIL'
            remarks = 'Action definition not found'
            print(result,remarks)
    except Exception as ex:
        print("Exception has occured")
        result = "FAIL"
        remarks = ex
        print(result,remarks)


def open_browser(value):
    global driver
    if value == 'Chrome':
        print("Chrome Browser Selected")
        driver = webdriver.Chrome('driver_path/chromedriver')
    elif value == 'Firefox':
        driver = webdriver.Firefox
    elif value == 'Safari':
        driver = webdriver.Safari
    else:
        print("Browser Not Supported")
    return driver

def open_url(driver,value):
    try:
        driver.get(value)
        result = "PASS"
        remarks = ""
    except Exception as ex:
        result = "FAIL"
        remarks = ex
    return result,remarks

def click_function(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath).click()
        result,remarks = "PASS",""
    except Exception as ex:
        result,remarks = "FAIL",ex
    return result,remarks


if __name__ == "__main__":
    read_excel()