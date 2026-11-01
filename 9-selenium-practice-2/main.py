from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget li time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}
for i in range(len(event_times)):
    events[i] = {
        "time": event_times[i].get_attribute("datetime").split("T")[0],
        "name": event_names[i].text,
    }

print(events)

driver.quit()