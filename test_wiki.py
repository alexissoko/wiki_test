"""
 
SDET Technical Test
 
Task 1 - Automated web testing 
With a test automation framework of selenium with java, test Wikipedia's search feature by searching for "Voyager 1" and add assertions for the same.
 
Task 2 - Automation 
How to switch from frame to main window? With syntax.
 
Task 3 - There are 10 pages in same window, an image is present in any page out of ten pages in same window. How will you validate this scenario with example?
 
Task 4 - Can we call parent class constructor in sub class constructor i.e constructor chaining by using super keyword?
 
Task 5 - DB Connection
How would you write a code for DB connection?
 
Task 6 - Automate API 
Given the REST API: https://developers.giphy.com/docs/api/endpoint#search
And this call to retrieve a list of GIFs: http://api.giphy.com/v1/gifs/search?q=funny+dog&api_key=dc6zaTOxFJmzC
Your task is to extensively Automate that API endpoint with assertions using java programming language. You can use the provided api_key: it's a public key for testing out that API.
 
Task 7 -Given a string say "CODE". Now create a new string with duplicates of each character in the original string and to it append the reverse of the same string (with duplicates) excluding the last character.
ex: step: CCOODDEE > Step: EEDDOOCC > finalResult: EEDDOOC
 
Task 8 -We have 10 numbers 1-10 and one button. I want to delete those numbers but should delete only even numbers – what should be the best ways to delete by clicking on the button.
For eg: if i click on button then alternate number should be deleted.
 
Task 9 -How to read Excel data through hash map?
 
Task 10 -While running script, you have observed "NoSuchElementException". But you have taken the correct locator(ID, XPATh or CSS). Still, you are facing the same issue. What might be the reason?
Deliverable
Please, provide a GitHub repo/cloud folder with the solutions to the tasks and instructions on how to run the tests.
 
"""
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
Yes you can refer to parent class methods from whitin the child one <super> command
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
