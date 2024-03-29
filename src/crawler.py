from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 

def open_browser() -> webdriver.Chrome:
    p = r"C:\Users\alexr\Documents\Projects\ChromeDrivers\chromedriver_win32_108\chromedriver.exe"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.ratemyprofessors.com/")

    return driver

def close_popup_1(driver: webdriver.Chrome):

    button_xpath = "/html/body/div[5]/div/div/button"

    button_present = EC.presence_of_element_located((By.XPATH,button_xpath))

    WebDriverWait(driver, timeout=9999).until(button_present)

    close_button = driver.find_element("xpath",(button_xpath))

    close_button.click()

def close_popup_2(driver: webdriver.Chrome):

    button_xpath = '//*[@id="pendo-close-guide-f789ac0a"]'

    button_present = EC.presence_of_element_located((By.XPATH,button_xpath))

    WebDriverWait(driver, timeout=9999).until(button_present)

    close_button = driver.find_element("xpath",(button_xpath))

    close_button.click()
    
def switch_to_school(driver: webdriver.Chrome, school: str):

    search_bar_xpath = r"//input[@type='text']"
    searchBar = driver.find_element("xpath",search_bar_xpath)
    

    a3 = webdriver.ActionChains(driver)
    a3.move_to_element(searchBar).click().send_keys(school).perform()

    dropdown_xpath = r"//div[contains(@class, 'SearchTypeahead')]"

    WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH,dropdown_xpath))

    a2 = webdriver.ActionChains(driver)
    a2.move_by_offset(35, 90).click().perform()
    searchBar.clear()

def lookup_professor(driver: webdriver.Chrome, professor: str):

    search_bar_xpath = r"//input[@type='text']"
    searchBar = driver.find_element("xpath",search_bar_xpath)
    

    a3 = webdriver.ActionChains(driver)
    a3.move_to_element(searchBar).click().send_keys(professor, Keys.ENTER).perform()

    

def is_found(driver: webdriver.Chrome) -> bool:

    no_match_xpath = r'//div[contains(text(),"No professors with ")]'

    try:

        WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.XPATH,no_match_xpath))

        return False
    except:
        pass

    return True


def get_rating(driver: webdriver.Chrome) -> float:

    rating_xpath =  r'//div[contains(@class,"CardNumRating")][1]//div[contains(@class,"Number")]'  

    return driver.find_element("xpath",rating_xpath).text

def clear_input(driver: webdriver.Chrome):

    search_bar_xpath = r"//input[@type='text']"
    searchBar = driver.find_element("xpath",search_bar_xpath)

    a2 = webdriver.ActionChains(driver)
    a2.move_to_element(searchBar).click().key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()    
    
