from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By

print("test case started")  

# s = Service("C:/Users/mayur/Downloads/chromedriver.exe")
s = Service("C:/Users/mayur/Desktop/vs code/programs/Selenium-demo/chromedriver.exe")

driver = webdriver.Chrome(service=s)

print("test opened")
driver.maximize_window()  

driver.get("https://www.zee5.com/movies")  

elem = driver.find_element(By.ID, 'searchInput')  # Find the search box
elem.send_keys('Mom' + Keys.RETURN)


time.sleep(100)

driver.quit()