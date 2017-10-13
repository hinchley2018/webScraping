#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
def main():
    page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
    print page
    if (page.status_code == 200):
        print page.content
        soup = BeautifulSoup(page.content,'html.parser')
        print soup.find_all('p')

if __name__ == '__main__':
    main()
