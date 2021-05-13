
# after installing all the prerequisites as mentioned in the blog.

import requests
from bs4 import BeautifulSoup
url = "https://flinkhub.com"

# Chaper 1: GET the Html

r = requests.get(url)
htmlContent = r.content
#print (htmlContent)

# Chaper 2: parse the Html

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)
# or print(soup.prettify)

# Chaper 3: traverse the tree of the Html
# types of objects commonly put into use
title = soup.title
#print (title)
# print(type(title)) #1.tag
# print(type(title.string)) #2.navigable string
# print (type(soup)) #3.soup
#
# markup = "<p><!--this is a comment --></p>"
# soup2=BeautifulSoup(markup)
# print(soup2) -> prints entire within quotes material
# print(soup2.p.string) ->prints this is a comment
# print(type(soup2))4.comment ->bs4.element.Comment


paras = soup.find_all('p')  # gives all the paras
paras = soup.find('p')  # gives the first para
#print (paras)
# print (paras, ['class'])  # -> gives classes of the para
# print (paras , ['class_=text-white']) -> finds para with specific class name


# anchors = soup.find('a')  # gives the first anchor

# get text from the para
# print (soup.find('p').get_text())  # finds para and prints text contained in it
# print(soup.get_text())  # -> prints text of the entire soup i.e. webpage. **

# Now I want anchor tags from the page
# anchors = soup.find_all('a')  # gives all the anchors
# for link in anchors:
# print(link.get('href'))

# I found that some links had only / and blank after it and repetitive links also might come. So I use set DS to avoid repetition and see if we can use a loop to avoid blank space or else, we use an infinite loop
anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if (link.get('href') != ' '):
        linkText = "https://flinkhub.com"+link.get('href')
        all_links.add(link)
        # print(linkText)

footer = soup.find(id='footer')
# print(footer)
# print(footer.children) #tags children available as a generator ->takes less time in case of big websites
# print(footer.contets) #tags children available as a list
# for elem in footer.contents:
# print (elem) #i get paras, rows , columns etc

# for item in footer.strings:
# print (item) #all the contents in string form are shown

# for item in footer.stripped_strings:
# print (item) #brings together all the types and shows together

# print(footer.parent)

# but if we write parents then we get a generator so we iterate over that generator
# eg for item in footer.parents:
# print (item.name) -> gives name of all file types in that branch of tree that it traversed to reach its parent eg. nav,body,html,document
