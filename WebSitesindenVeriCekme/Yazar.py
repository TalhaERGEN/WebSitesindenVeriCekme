import requests
from bs4 import BeautifulSoup

url=requests.get("https://quotes.toscrape.com/")
if url.status_code == 200:
    print("siteden veri çekilebilir")
else:
    print("siteden veri çekilemez")
    
soup=BeautifulSoup(url.content,"html.parser")


for i in soup.find_all("div",{"class": "quote"}):
    text=i.find("span",{"class":"text"}).text
    author=i.find("small",{"class":"author"}).text
    print(f"Text: {text} \n Author: {author}")