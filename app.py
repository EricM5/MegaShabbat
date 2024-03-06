from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import pandas as pd
import os
import time
URL = 'https://www.ticketleap.com/'


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
    time.sleep(10)
    sign_in = driver.find_element(By.XPATH, "//button[normalize-space(text())='Sign in']")    
    sign_in.click()
    time.sleep(10)

load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

login_and_click(URL, USERNAME, PASSWORD)




    
