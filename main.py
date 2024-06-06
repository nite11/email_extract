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
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
    #chrome_options.add_argument('--window-size=1920,1080')  # Set a fixed window size
    chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
    chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

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
     
    pattern = re.compile(r'.*mail.*')   

    filename="myfile4.txt"
    row_num=26
    
    anchors = []
    while (len(anchors)!=100):
        time.sleep(1)
        anchors = driver.find_elements(By.CSS_SELECTOR, 'td.spalte-sprache')
        print(len(anchors))
    
    page_button= driver.find_element(By.CSS_SELECTOR, '[data-dt-idx="4"]')
    page_button.click()

    for i in range(row_num):
        driver.execute_script("window.open('https://www.justiz-dolmetscher.de/Recherche/de/Suchen');")
        # Switch to the new window
        driver.switch_to.window(driver.window_handles[-1])
        anchors = []
        while (len(anchors)!=row_num):
            time.sleep(1)
            anchors = driver.find_elements(By.CSS_SELECTOR, 'td.spalte-sprache')
        anchors[i].click()        
        time.sleep(2)
        emails=driver.find_elements(By.CSS_SELECTOR, 'a[href]')   
        for email in emails:
            href = email.get_attribute('href')
            if pattern.search(href):
                with open(filename, 'a') as file1:
                    text1=f'{email.text}\n'
                    file1.write(text1)   
        
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
         

       
    driver.quit()
        
        
perform_search()

