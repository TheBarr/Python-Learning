from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")

soup = BeautifulSoup(response.text, "html.parser")

article_titles = [title.get_text() for title in soup.find_all(name="span", class_="titleline")]
article_links = [link.a.get("href") for link in soup.find_all(name="span", class_="titleline")]
article_up_votes = [int(vote.get_text().split()[0]) for vote in soup.find_all(name="span", class_="score")]

max_up_vote = max(article_up_votes)
index = article_up_votes.index(max_up_vote)
print(article_titles[index] , article_links[index], article_up_votes[index])