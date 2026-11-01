from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.amazon.com/dp/B0GCTZPQ5N/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B0GCTZPQ5N&pd_rd_w=T762m&content-id=amzn1.sym.9bd45040-31dd-4792-bd5a-341290ebe305&pf_rd_p=9bd45040-31dd-4792-bd5a-341290ebe305&pf_rd_r=CHTGP18EAVEPQ7H10TEZ&pd_rd_wg=Pky1G&pd_rd_r=d67758e2-5b50-4223-968f-b40ceef30ea0&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM')


symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol").get_attribute("textContent").strip()
price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole").get_attribute("textContent").replace(".", "").replace(",", "").strip()
price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction").get_attribute("textContent").strip()

price = float(f"{price_whole}.{price_fraction}")

print(f"The current price is {symbol}{price}")

driver.quit()