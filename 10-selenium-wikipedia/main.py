from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

wait = WebDriverWait(driver, 10)

# articles = driver.find_element(By.CSS_SELECTOR, '#mwDw').text
# article_anchor_tag = driver.find_element(By.CSS_SELECTOR, '#mwDg')

# article_anchor_tag.click()


search = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'input.cdx-text-input__input[name="search"]')
    )
)

search_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.cdx-search-input__end-button"))
)

search.send_keys("Hi")
search_button.click()

