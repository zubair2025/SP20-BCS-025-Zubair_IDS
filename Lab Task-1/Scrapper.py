import requests 
from bs4 import BeautifulSoup

# Get the HTML 
req = requests.get("https://en.wikipedia.org/wiki/Empower_Field_at_Mile_High")

#Prettify Code
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())

#Only Text
print(soup.get_text())

#Fetching Titles
res = soup.title
print(res.prettify())
print(res.get_text())

#Getting the Title
title = soup.title
print(title)

#Getting Paragraphs
paras = soup.find_all('p')
print(paras)
