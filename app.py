from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import pandas as pd
import os
import time
from bs4 import BeautifulSoup
URL = 'https://www.ticketleap.com/'


def check_element_exists(driver, value):
    elements = driver.find_element(By.XPATH, value)
    if elements:
        print("ELEMENT EXISTS!")
        return True
    else:
        return False

def login_and_click(url, username, password):
    driver = webdriver.Chrome()
    driver.get(url)
    sign_in = driver.find_element(By.XPATH, "//*[text()='Sign In']")    
    sign_in.click()
    email_text_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_username")))
    email_text_box.send_keys(username)
    time.sleep(2)
    email_text_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email_login_button")))
    email_text_box.click()
    time.sleep(2)
    password_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    password_box.send_keys(password)
    time.sleep(3)
    sign_in = driver.find_element(By.XPATH, "//button[normalize-space(text())='Sign in']")    
    sign_in.click()
    time.sleep(5)
    driver.get('https://admin.ticketleap.events/reports/attendees?event=49721')
    time.sleep(5)


    #get the html page source
    time.sleep(10)
    html = driver.page_source  # get the HTML of the page
    soup = BeautifulSoup(html, 'html.parser')
    # with open('sample.html', 'w') as file:
    #     file.write(html)

    #loop for every page here.
    
    # [indent] Now get the attendees


    attendees_and_tables = []
    
    exists = check_element_exists(driver, "//i[@class='icon-navigate_next']")
    while exists:        
        html = driver.page_source  # get the HTML of the page
        soup = BeautifulSoup(html, 'html.parser')
        ten_attendees_on_current_page  = soup.find_all("div", class_="list-group")
        for attendee in ten_attendees_on_current_page:
            attendee_name = attendee.find('div', class_='TicketsCell-module__tickets-cell__ticket-button-name_HCNTP').text
            attendee_table_host = attendee.find('div', class_='TicketsCell-module__tickets-cell__block_g094r').text
            attendees_and_tables.append((attendee_name, attendee_table_host))
        time.sleep(10)
        print(attendees_and_tables)
        exists = check_element_exists(driver, "//i[@class='icon-navigate_next']")
        if exists:
            navigate_button = driver.find_element(By.XPATH, "//i[@class='icon-navigate_next']")    
            navigate_button.click()
            time.sleep(10)
        else:
            break
        
    print(attendees_and_tables)




load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

login_and_click(URL, USERNAME, PASSWORD)



    
