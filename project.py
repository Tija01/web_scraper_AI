import requests
from bs4 import BeautifulSoup
import re


def main():
    #TODO: Also search the other 29 pages of news
    URL = "https://news.ycombinator.com/news"
    page = requests.get(URL)
    # with open("html.txt","w") as file:
        # file.write(page.txt) 
    keywords = {"AI", "artificial intelligence", "machine learning", "Internet"} # 'Internet' keyword added for testing purposes
    links = search(page, keywords)
    for link in links:
        print(link)
    
    
def search(page, keywords):
    # Search a page for AI related articles
    
    # Isolate article links with titles from the other data
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find(class_="itemlist")
    links = clean(data("a"))
    
    # Filter subject relevant to keywords
    selected_links = []
    for link in links:
        print(link)
        for keyword in keywords:
            if re.search(fr"\b{keyword}\b", link.text, re.IGNORECASE):
                selected_links.append(link.get('href'))
    return selected_links

def clean(links):
    # Keep only article links
    cleaned_links = []
    for link in links:
        if re.match(r"https?://", link['href'].strip()):
            cleaned_links.append(link)
    return cleaned_links
    


def send():
    # Send discord message with found link
    ...


if __name__ == "__main__":
    main()