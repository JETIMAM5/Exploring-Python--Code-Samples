from bs4 import BeautifulSoup
import requests

# Scraping a live website

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

news = [(heading.find(name="a").get("href"), heading.find(name="a").getText())
        for heading in soup.find_all(class_="titleline")]

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(class_="score")]

# for i in range(len(news)):
#     link, text = news[i]
#     try:
#         score = article_upvotes[i]
#     except IndexError:
#         score = "No score available"
#     print(f"Title: {text}, Link: {link}, Score: {score}")

max_upvote_index = (article_upvotes.index(max(article_upvotes)))
print(news[max_upvote_index])







# ----------------------------------------------------------------------------------------------------------------
# with open("website.html", 'r', encoding='utf8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')  # This entire soup object represents our HTML code.
# # print(soup.title) --> Whole tag with the text inside of it
# # print(soup.title.name) --> Name of the tag
# # print(soup.title.string) --> Text inside the tag
# # print(soup.prettify())  # indents the html code
# # print(soup.a) --> First anchor tag
#
# all_anchor_tags = soup.find_all(name="a")  # --> Finds all the anchor tags in the HTML code
#
# for tag in all_anchor_tags:
#     # print(tag.get_text())  # --> Prints the texts inside the anchor tags.
#     print(tag.get("href"))  # --> We can get the value of an attribute with the method get() --> returns all the links
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")  # class is reserved keyword for creating classes (!)
# print(section_heading.get("class"))
#
#
# # How to get first link of a website ? (Using CSS Selectors)
# company_url = soup.select_one(selector="p a")  # Give us first matching item (in this particular case ,
# # our company url sits in an anchor tag which sits in a p tag)
#
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)

