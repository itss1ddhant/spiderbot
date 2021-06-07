# If you want to scrape a website:
# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4

# Step 0: Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
import pymongo
import concurrent.futures
url = "https://flinkhub.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 3: HTML Tree traversal
#
# Commonly used types of objects:
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# # 4. Comment
# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))


# Get the title of the HTML page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)

# print(anchors)

# Get first element in the HTML page
# print(soup.find('p') )

# Get classes of any element in the HTML page
# print(soup.find('p')['class'])

# find all the elements with class lead
# print(soup.find_all("p", class_="lead"))

# Get the text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())

# Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://flinkhub.com" + link.get('href')
        all_links.add(link)
        print(linkText)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(anchors)

navbarSupportedContent = soup.find(id='navbarSupportedContent')

client = pymongo.MongoClient('mongodb://itss1ddhant:<Siddhant-860>@cluster0-shard-00-00.inbce.mongodb.net:27017,cluster0-shard-00-01.inbce.mongodb.net:27017,cluster0-shard-00-02.inbce.mongodb.net:27017/flinkhub?ssl=true&replicaSet=atlas-r1p9pc-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.db.linkText
try:
    db.insert_many(linkText)
    print('inserted {len(linkText)} scraped web links')
except:
    print('an error occurred and links were not stored to db')

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
# for elem in navbarSupportedContent.contents:
#     print(elem)

# for item in navbarSupportedContent.strings:
#     print(item)

# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents:
#     print(item.name)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# elem = soup.select('.modal-footer')
# print(elem)
