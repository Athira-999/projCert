
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import subprocess

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def seltest():

    driver = webdriver.Chrome(executable_path='/usr/lib64/chromium-browser/chromedriver',chrome_options=chrome_options)
    url = "http://104.198.138.81:8080/"
    try:
        driver.get(url)
        driver.maximize_window()
        about_text1 = ''
        about_text2 = ''
        about_text = ''
        try:
            #Navigating to About Us
            driver.find_element_by_xpath("//a[@id = 'About Us']").click()
            time.sleep(5)
            #Fetching the text
            about_text1=driver.find_element_by_xpath("//p[@id = 'PID-ab2-pg']").text
            about_text2 = driver.find_element_by_xpath("//p[@id = 'PID-ab2-pg']//following::p").text
        except NoSuchElementException:
            print("Element not found")
        about_text = about_text1 + "\n" + about_text2
    except Exception as e:
        print("Exception occured <> {}".format(str(e)))
    driver.close()
    return about_text
