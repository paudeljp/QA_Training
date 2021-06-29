from selenium import webdriver
import time
import pandas as pd
url_location = 'URLs.xlsx'

def read_excel():
    reader = pd.read_excel(url_location)
    for row,column in reader.iterrows():
        sn = column["S/N"]
        url = column["URL"]
        site = column["Site Name"]
        print(sn,url,site)
        driver = webdriver.Chrome('./chromedriver')
        driver.get(url)
        title = driver.title
        print(title)
        try:
            assert site == title
        except AssertionError:
            print("Title not matched")
        else:
            print("Title matched")
        time.sleep(2)
        driver.quit()
if __name__ == "__main__":
    read_excel()

