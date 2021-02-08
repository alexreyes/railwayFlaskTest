from flask import Flask, jsonify
from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from book import Book

def simple_get(url): 
    try: 
        with closing(get(url, stream=True)) as resp: 
            if is_good_response(resp): 
                return resp.content
            else: 
                return None

    except RequestException as e: 
        log_error("Error using requests to {0} : {1}".format(url, str(e)))

def is_good_response(resp): 
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)
      
def get_books(year):
    
    if (isinstance(year, str) ):
        year = int(year)
    
    urls = {
        2019: 'https://www.goodreads.com/user_challenges/16171692', 
        2020: 'https://www.goodreads.com/user_challenges/20355287', 
        2021: 'https://www.goodreads.com/user_challenges/25240418'
    }

    bookList = []

    response = simple_get(urls[year])

    soup = BeautifulSoup(response, 'html.parser')

    if response is not None: 
        
        for li in soup.find_all('li', attrs={'class': 'bookCoverContainer'}):
            title = li.find('img', alt=True)
            link = li.find('a', attrs={'class': 'bookCoverTarget'})
            
            if title['alt'] != "":
                link = "https://www.goodreads.com" + link['href']
                bookList.append([title['alt'], link])

    return bookList  
