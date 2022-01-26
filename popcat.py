from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = 'D:/NTUST/Project/Others Program/Selenium&Web_Crawler/chromedriver.exe'

#get the chromedriver file
driver = webdriver.Chrome(PATH)

driver.get('https://popcat.click/')

#when detect the title name "title" in 10 secs then conduct the following code
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "title")))

# tap = driver.find_element_by_class_name('cat-img.op')
tap = driver.find_element_by_id('app')                      #find the label control the tap button
# tap_count = driver.find_element_by_xpath('//*[@id="app"]/div/div')
tap_count = driver.find_element_by_class_name('counter')    #this is means nothing for now

while True:
    tap.click()
    time.sleep(0.02)    #must delay a unit time to avoid detected as a robot by the web system
    # print(tap_count.text)
