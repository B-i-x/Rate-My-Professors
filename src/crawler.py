from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 

def open_browser() -> webdriver.Chrome:
    p = r"C:\Users\alexr\Documents\Projects\ChromeDrivers\chromedriver_win32_106\chromedriver.exe"

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(executable_path=p, chrome_options=chrome_options)

    driver.get("https://www.ratemyprofessors.com/")

    return driver

def close_popup(driver: webdriver.Chrome):

    button_xpath = "/html/body/div[5]/div/div/button"

    button_present = EC.presence_of_element_located((By.XPATH,button_xpath))

    WebDriverWait(driver, timeout=9999).until(button_present)

    close_button = driver.find_element_by_xpath(button_xpath)

    close_button.click()

def switch_to_school(driver: webdriver.Chrome, school: str):

    search_bar_xpath = r"//input[@type='text']"
    searchBar = driver.find_element_by_xpath(search_bar_xpath)
    searchBar.clear()

    a3 = webdriver.ActionChains(driver)
    a3.move_to_element(searchBar).click().send_keys(school).perform()

    driver.implicitly_wait(5)

    a2 = webdriver.ActionChains(driver)
    a2.move_to_element_with_offset(searchBar, 35, 82).perform()

def lookup_professor(driver: webdriver.Chrome, professor: str, first_last: str = "normal"):

    search_bar_xpath = r"//input[@type='text']"
    searchBar = driver.find_element_by_xpath(search_bar_xpath)
    searchBar.clear()

    a3 = webdriver.ActionChains(driver)
    a3.move_to_element(searchBar).click().send_keys(professor, Keys.ENTER).perform()

def verify_school(driver: webdriver.Chrome, desired_school_name: str) -> bool:

    school_card_xpath = r'//div/div/div[4]/div[1]/div[1]/div[3]/a/div/div[2]/div[2]//div[2]'

    school_card = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH,school_card_xpath))

    print(f"found element is {school_card.text}")

    return (str(school_card.text) == desired_school_name)



def get_rating(driver: webdriver.Chrome) -> float:

    rating_xpath =  r'//div[contains(@class,"CardNumRating")][1]//div[contains(@class,"Number")]'  

    return driver.find_element_by_xpath(rating_xpath).text


        
    
