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

def get_rating_for_professor(driver: webdriver.Chrome, professor: str, first_last: str):

    if first_last == "first":
        change_to_prof_xpath = r'//*[contains(text(), "I' + "'" + 'd like")]'
        print(change_to_prof_xpath)
        change_to_prof = driver.find_element_by_xpath(change_to_prof_xpath)
        change_to_prof.click()

    search_bar_xpath = r"//input[@type='text']"
    searchBar = driver.find_element_by_xpath(search_bar_xpath)

    a3 = webdriver.ActionChains(driver)
    a3.move_to_element(searchBar).click().send_keys(professor, Keys.ENTER).perform()

def verify_school(driver: webdriver.Chrome, desired_school_name: str) -> bool:

    school_card_xpath = r"//div[contains(@class, 'CardSchool__School')]"

    school_name = driver.find_element_by_xpath(school_card_xpath).text()

    return (school_name == desired_school_name)

def get_rating(driver: webdriver.Chrome) -> float:

    rating_xpath =  r"//div[contains(@class,'CardNumRating')][1]//div[contains(@class,'Number')]"   

    return driver.find_element_by_xpath(rating_xpath).text()


        
    