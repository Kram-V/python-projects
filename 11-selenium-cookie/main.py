from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://ozh.github.io/cookieclicker/")

wait = WebDriverWait(driver, 20)

# Pick English, then wait for the page to reload
english = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
english.click()
wait.until(EC.staleness_of(english))  # waits until the old page is gone

# Click for 10 seconds
cookie = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))
end_time = time.time() + 10
while time.time() < end_time:
    try:
        cookie.click()
    except StaleElementReferenceException:
        cookie = driver.find_element(By.ID, "bigCookie")  # find the new one