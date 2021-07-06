import time 
from selenium import webdriver
#from selenium.common.keys import keys

while True:
    driver = webdriver.Chrome("C:/chromedriver.exe")
    driver.get('https://poll.fm/10863493')
    time.sleep(2)
    driver.find_element_by_id("PDI_answer50056528").click()
    time.sleep(1)
    driver.find_element_by_css_selector(".vote-button.css-vote-button.pds-vote-button").click()
    #driver.find_element_by_css_selector("").click()
    #driver.FindElement(By.XPath("//div[@class='option_enclosure_2']/span[@class='option_text']"));

    time.sleep(2)

    driver.refresh()
    driver.quit()
    time.sleep(3)
