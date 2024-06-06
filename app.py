from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException
import time
import re


def perform_search():
    # Path to the chromedriver executable
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
  

# Initialize the WebDriver with the specified options
    

    
    driver_path = r'C:\Users\Admin\Desktop\email_extract\chromedriver'

    # Initialize the WebDriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    #driver = webdriver.Chrome(driver_path)
   
    
        # Open Google
    driver.get('https://www.justiz-dolmetscher.de/Recherche/de/Suchen')
        
        # Find the search box
    search_box = driver.find_element(By.NAME, 'Sprache1')
        
        # Enter the search query
    search_box.send_keys('Ukrainisch')
    driver.find_element(By.NAME, 'IstUebersetzer').click()
    search_box.send_keys(Keys.RETURN)

    dropdown_element = driver.find_element(By.NAME, 'suchergebnisse_length')
    Select(dropdown_element).select_by_visible_text('100')
    search_box.send_keys(Keys.RETURN)

    dropdown_element2 = driver.find_element(By.ID, 'sort')
    Select(dropdown_element2).select_by_visible_text('Nachname')
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)
    pattern = re.compile(r'.*mail.*')    
    anchors = driver.find_elements(By.CSS_SELECTOR, 'td.spalte-sprache')    
    

    for anchor in anchors:
        
        # Example: Print the text of each element before clicking
        #print(f"Clicking on element {index} with text: {element.text}")
        
        time.sleep(2)
        emails=driver.find_elements(By.CSS_SELECTOR, 'a[href]')   
        for email in emails:
            href = email.get_attribute('href')
            if pattern.search(href):                
                    print(f'{email.text}\n')
                    
        driver.switch_to.window(driver.window_handles[0])
        # Wait for the results to load
    

       
    
        
        
perform_search()


