from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path='/usr/lib64/chromium-browser/chromedriver',chrome_options=chrome_options)
url = "http://104.198.138.81:8080/"
try:
    driver.get(url)
    driver.maximize_window()
    about_text= ''
    try:
        #Navigating to About Us
        driver.find_element_by_xpath("//a[@id = 'About Us']").click()
        time.sleep(5)
        #Fetching the text
        about_text=driver.find_element_by_xpath("//p[@id = 'PID-ab2-pg']").text
    except NoSuchElementException:
        print("Element not found")
    #Reading expected text from source file
    readFile = open("phpapp.txt",'r')
    expected_text = readFile.read()
    readFile.close()
    # Check if the texts match
    if expected_text == about_text:
        print("matching")
    else:
        print("no match")

except Exception as e:
    print("Exception occured <> {}".format(str(e)))
driver.close()
