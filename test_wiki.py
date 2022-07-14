from tracemalloc import start
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
url = "https://www.wikipedia.org"
search_text = "Voyager 1"
# import conf

def test_happy_wiki():
    driver = webdriver.Chrome("./chromedriver")
    #driver = selenium.webdriver.Chrome("./chromedriver")

    driver.get(url)

    search = driver.find_element(By.XPATH, '//*[@id="searchInput"]') # <a class='gb_1 gb_2 gb_8d gb_8c' sadfasdfsadf=asdfasdf> </a>

    #search = driver.find_element_by_id("searchInput")
    search.send_keys(search_text)
    driver.find_element(By.XPATH, '//*[@id="mp-tfa-img"]/div/a/img').click()
    assert "Voyager 1" in driver.title
    input("Fine up until here")
    """
    # Task 2
    alert = driver.switch_to.alert
    driver.switch_to.default_content()
    driver.switch_to.frame('frame_name')
    """
    """
# Task 3
one way to do it will be. Assuming we have 10 tabs
"""
for i in range(10):
    window_after = driver.window_handles[i]
    driver.switch_to_window(window_after)
    try:
        element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mp-tfa-img"]/div/a/img'))) #image xpath
        print("IAMGE found")
        break
    except: pass

# Task 4
"""
Yes you can refer to parent class methods from whitin 
"""

# Task 5
import mysql.connector

def mySql_api_start(host, user, password):
    mydb = mysql.connector.connect(
        host = host
        user = user,
        password = password
        )
    return mydb

# Task 6
import requests

response = requests.get("http://api.giphy.com/v1/gifs/search?q=funny+dog&api_key=dc6zaTOxFJmzC")
# couldn't further validate endpoint since I got 403 error on the Key provided. 

# Task 7
def duplicator(string):
    result = ""
    for letter in string[::-1]:
        result += letter * 2
    return result[:-1]

# Task 8
def button(start_pos):
    while True:
        yield start_pos
        start_pos += 2
        
test_button = button(0)
for i in range(5):
    next(test_button)
    
# Task 9
# pip install openpyxl

from openpyxl import load_workbook

wb = load_workbook("Excel.xlsx")
sheet = wb.active

# Task 10

# could be that the Selenium module is deprecated or aslo there can be connectivity errors. Just thinkin out of the box.
