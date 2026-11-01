"""
Laptop Price Tracker
Scrapes every laptop from the webscraper.io practice store,
saves them to a CSV, and prints a quick analysis.
"""

import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException

START_URL = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

# Save the CSV next to this script, no matter which folder you run it from
CSV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "laptops.csv")

MAX_RETRIES = 3


# ---------- helpers ----------

def get_text(card, selector):
    """Text of a child element, or '' if it's missing."""
    try:
        return card.find_element(By.CSS_SELECTOR, selector).text.strip()
    except NoSuchElementException:
        return ""


def to_price(text):
    """'$1,299.99' -> 1299.99"""
    try:
        return float(text.replace("$", "").replace(",", ""))
    except ValueError:
        return None


def to_int(text):
    """'14 reviews' -> 14"""
    digits = "".join(ch for ch in text if ch.isdigit())
    return int(digits) if digits else 0


def get_rating(card):
    """Star rating (0-5). Uses data-rating if present, otherwise counts star icons."""
    try:
        return int(card.find_element(By.CSS_SELECTOR, "[data-rating]").get_attribute("data-rating"))
    except (NoSuchElementException, TypeError, ValueError):
        return len(card.find_elements(By.CSS_SELECTOR, ".ratings .ws-icon-star"))


# ---------- browser ----------

def make_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # remove this line to watch the browser
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    return webdriver.Chrome(options=options)


def safe_quit(driver):
    try:
        driver.quit()
    except Exception:
        pass  # Chrome may already be gone


# ---------- scraping ----------

def scrape_page(driver):
    laptops = []
    for card in driver.find_elements(By.CSS_SELECTOR, "div.thumbnail"):
        try:
            title_link = card.find_element(By.CSS_SELECTOR, "a.title")
        except NoSuchElementException:
            continue

        laptops.append({
            # the title attribute has the full name; the visible text is shortened
            "name": title_link.get_attribute("title") or title_link.text.strip(),
            "price": to_price(get_text(card, ".price")),
            "description": get_text(card, ".description"),
            "reviews": to_int(get_text(card, ".review-count")),
            "rating": get_rating(card),
            "link": title_link.get_attribute("href"),
        })
    return laptops


def scrape_all():
    all_laptops = []
    driver = make_driver()
    url = START_URL
    page = 1

    try:
        while url:
            for attempt in range(1, MAX_RETRIES + 1):
                try:
                    driver.get(url)
                    WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "div.thumbnail"))
                    )
                    laptops = scrape_page(driver)

                    next_links = driver.find_elements(By.CSS_SELECTOR, 'a.page-link[rel="next"]')
                    next_url = next_links[0].get_attribute("href") if next_links else None
                    break  # page succeeded

                except WebDriverException as error:
                    print(f"Page {page} failed (attempt {attempt}/{MAX_RETRIES}): "
                          f"{type(error).__name__}. Restarting Chrome...")
                    safe_quit(driver)
                    driver = make_driver()
            else:
                print(f"Giving up on page {page}. Keeping what was collected so far.")
                break

            all_laptops.extend(laptops)
            print(f"Page {page}: {len(laptops)} laptops (total {len(all_laptops)})")

            url = next_url  # None on the last page, which ends the loop
            page += 1

    except KeyboardInterrupt:
        print("\nStopped by user. Keeping what was collected so far.")
    finally:
        safe_quit(driver)

    return all_laptops


# ---------- saving & analysis ----------

def save_csv(laptops):
    fields = ["name", "price", "description", "reviews", "rating", "link"]
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(laptops)
    print(f"\nSaved {len(laptops)} laptops to {CSV_FILE}")


def analyze(laptops):
    priced = [l for l in laptops if l["price"] is not None]
    if not priced:
        print("No prices found - check the selectors.")
        return

    cheapest = min(priced, key=lambda l: l["price"])
    priciest = max(priced, key=lambda l: l["price"])
    average = sum(l["price"] for l in priced) / len(priced)
    best_rated = max(priced, key=lambda l: (l["rating"], l["reviews"]))
    best_value = max(priced, key=lambda l: l["rating"] / l["price"])

    print("\n===== Laptop Analysis =====")
    print(f"Total laptops : {len(priced)}")
    print(f"Average price : ${average:,.2f}")
    print(f"Cheapest      : {cheapest['name']} - ${cheapest['price']:,.2f}")
    print(f"Most expensive: {priciest['name']} - ${priciest['price']:,.2f}")
    print(f"Best rated    : {best_rated['name']} - {best_rated['rating']} stars "
          f"({best_rated['reviews']} reviews)")
    print(f"Best value    : {best_value['name']} - ${best_value['price']:,.2f}, "
          f"{best_value['rating']} stars")

    budget = 1000
    under_budget = sorted(
        (l for l in priced if l["price"] <= budget),
        key=lambda l: (-l["rating"], l["price"]),
    )[:5]
    print(f"\nTop 5 under ${budget}:")
    for l in under_budget:
        print(f"  {l['rating']} stars  ${l['price']:>8,.2f}  {l['name']}")


# ---------- main ----------

def main():
    laptops = scrape_all()
    if laptops:
        save_csv(laptops)
        analyze(laptops)
    else:
        print("No laptops collected.")


if __name__ == "__main__":
    main()