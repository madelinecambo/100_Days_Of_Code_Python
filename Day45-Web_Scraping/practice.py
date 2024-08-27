from bs4 import BeautifulSoup
import requests
import re

# Web Scraping from Live Website

URL = "https://news.ycombinator.com/news"

response = requests.get(URL)
# will print out the code that represents the webpage
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)

# Get first article title, link and upvotes
# Need to skip the first tag as it includes the webpage address and is not an article
articles = soup.find_all(name="a", attrs={'href': re.compile("https")})[1:]

article_texts = []
article_links = []

for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)
print(article_texts)
print(article_links)

article_upvotes = [int(upvote.getText().split(" ")[0]) for upvote in soup.find_all(name="span", class_="score")]
print(article_upvotes)

# find maximum number of upvotes
highest_upvotes = max(article_upvotes)

# return the index of the max number of upvotes
highest_article_index = article_upvotes.index(highest_upvotes)

print(article_texts[highest_article_index])
print(article_links[highest_article_index])
print(article_upvotes[highest_article_index])


# article_upvotes = soup.find_all(name="span", class_="score").getText()
# article_titles = []
# #to get all anchor tags
# article_tags = soup.find_all(name="a", attrs={'href':re.compile("https")})
# upvote = soup.find(name="span", class_ = "score").getText()
# print(upvote)
# print(article_tags)
#
# titles = []
# links = []
# for tag in article_tags[1:]:
#     print(tag)
    # titles.append(tag.getText())
    # links.append(tag['href'])

# print(titles)




# We want the titles and links to each news article: Goal is to get most upvoted

# articles = soup.select_one(selector="a href")
# for _ in articles:
#     print(_)

































# Practice
# # import lxml
#
# with open('website.html') as webpage:
#     content = webpage.read()
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.string)
#
# print(soup.prettify())
#
# print(soup.a)
# print(soup.li)
# print(soup.p)
#
#
# # to get all of the paragraph's - to get all the components we are looking for!
#
# #to get all anchor tags
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name = "h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.name)
# print(section_heading.get("class"))
#
# #can use the css selectors in beautiful soup
#
# # to select on elements/tags
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# # to select on an id
# name = soup.select_one("#name")
# print(name)
#
# #to select on a class
# headings = soup.select(".heading")
# print(headings)

#drill through using css selectors to get to any element you want on the page
