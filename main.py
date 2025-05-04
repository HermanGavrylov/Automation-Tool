from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from psswd import USERNAME, PASSWORD

chrome_options = Options()
chrome_options.add_argument("--disable--search-engine-choice-screen")
service = Service('chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(options=chrome_options, service=service)

driver.get('https://demoqa.com/login')

username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
driver.execute_script("arguments[0].click();", login_button)



input("Press Enter to close the browser")
driver.quit()