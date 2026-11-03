from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import csv

URL = "https://soundcloud.com/search/sounds?q=parokya%20ni%20edgar"
CSV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "songs.csv")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")           # no browser window
chrome_options.add_argument("--window-size=1920,1080")  # act like a normal desktop screen

try:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)

    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sound__coverArt"))
    )

    anchor_tags = driver.find_elements(By.CSS_SELECTOR, ".sound__coverArt")[:10]
    song_links = [tag.get_attribute("href") for tag in anchor_tags]

    images = driver.find_elements(By.CSS_SELECTOR, ".sound__coverArt span.image__full")[:10]
    image_urls = []

    for img in images:
        # Scroll the song onto the screen so its picture loads
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", img)

        # Wait (up to 5 seconds) until the picture link is in the style
        try:
            WebDriverWait(driver, 5).until(lambda d: 'url("' in (img.get_attribute("style") or ""))
        except Exception:
            pass  # still not loaded after 5 seconds

        style = img.get_attribute("style") or ""
        if 'url("' in style:
            image_urls.append(style.split('url("')[1].split('")')[0])
        else:
            image_urls.append("")

    titles = driver.find_elements(By.CSS_SELECTOR, ".soundTitle__title span")[:10]
    song_titles = [title.text.replace('Parokya ni Edgar -', "").replace('Parokya Ni Edgar -', "").strip() for title in titles]

    likes = driver.find_elements(By.CSS_SELECTOR, ".sc-button-like span")[:10]
    all_likes = [like.text for like in likes]

    reposts = driver.find_elements(By.CSS_SELECTOR, ".sc-button-repost span")[:10]
    all_reposts = [repost.text for repost in reposts]

    plays = driver.find_elements(By.CSS_SELECTOR, '.sc-ministats-plays span[aria-hidden="true"]')[:10]
    all_plays = [play.text for play in plays]

    comments = driver.find_elements(By.CSS_SELECTOR, '.sc-ministats-comments span[aria-hidden="true"]')[:10]
    all_comments = [comment.text for comment in comments]

    time_uploads = driver.find_elements(By.CSS_SELECTOR, '.soundTitle__uploadTime time span[aria-hidden="true"]')[:10]
    all_time_uploads = [time_upload.text for time_upload in time_uploads]

    rows = zip(
        song_titles,
        all_plays,
        all_likes,
        all_reposts,
        all_comments,
        all_time_uploads,
        song_links,
        image_urls,
    )

    with open(CSV_FILE, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        # Header row
        writer.writerow(["Titles", "Plays", "Likes", "Reposts", "Comments", "Uploaded", "Links", "Image URLs"])

        # One row per song
        writer.writerows(rows)

    print(f"Saved to {CSV_FILE}")


finally:
    try:
        driver.quit()
    except Exception:
        pass  # closing failed, but the scraping is already done