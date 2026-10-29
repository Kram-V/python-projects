from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_tags = soup.select(".titleline > a")
article_scores = soup.select(".subline > .score")

article_texts = [article.getText() for article in article_tags]
article_links = [article.get('href') for article in article_tags]
all_article_scores = [int(score.getText().split()[0]) for score in article_scores]

largest_number = max(all_article_scores)
largest_index = all_article_scores.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(all_article_scores[largest_index])





# with open('5-bs4/website.html') as file:
#   contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# all_anchor_tags = soup.find_all('li')

# for tag in all_anchor_tags:
#   print(tag.getText())