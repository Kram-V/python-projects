import quopri
import re
from bs4 import BeautifulSoup

# The page was saved as "Webpage, Single File", so it's encoded.
# quopri decodes it back into normal HTML.
with open("6-100-movies-webscraping/website.html", mode="rb") as file:
    empireonline_webpage = quopri.decodestring(file.read()).decode("utf-8", errors="ignore")

soup = BeautifulSoup(empireonline_webpage, "html.parser")

# 1. Movie titles are <h2> tags like "100) Avatar (2009)".
#    Keep only the h2s that start with a number and ")".
all_titles = [h2.getText(strip=True) for h2 in soup.find_all(name="h2")]
movie_titles = [title for title in all_titles if re.match(r"^\d+\)", title)]

# 2. Flip the list so it goes 1 -> 100
movies = movie_titles[::-1]

# 3. Write them into a text file, one per line
with open("6-100-movies-webscraping/movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")