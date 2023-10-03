from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import os

driver = 0

def get_chrome_driver_path():
   
    # Get the current working directory
    cwd = os.getcwd()
    
    # Create the path to 'dep' within the current working directory
    path_to_driver = os.path.join(cwd, 'dep')
    
    # Create the path to 'folderx' within 'dep'
    path_to_driver = os.path.join(path_to_driver, 'chrome-win64')

    path_to_driver = os.path.join(path_to_driver, 'chrome-win64')

    path_to_driver = os.path.join(path_to_driver, 'chrome.exe')

    return path_to_driver

def open_browser() -> webdriver.Chrome:
    global driver

    p = get_chrome_driver_path()

    # chrome_options = Options()
    # chrome_options.add_experimental_option("detach", True)

    # driver = webdriver.Chrome(executable_path=p, chrome_options=chrome_options)

    driver = webdriver.Chrome()

    driver.get("https://uaccess.arizona.edu/");

    return driver

def go_to_student_center(driver: webdriver.Chrome):
     
	driver.find_element(By.ID,"ua-service-status-uaccessstudent").click()

