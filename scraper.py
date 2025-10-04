# Scraping functions
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import logging 

# Ankit - fix the debug to info
logging.basicConfig(level=logging.DEBUG)

def scrape_quotes(limit=5):
    url =  "https://quotes.toscrape.com/"
    #url = "https://books.toscrape.com/"
    #fetches the page
    response=requests.get(url)
    if response.status_code !=200:
        logging.error("Failed to fetch the website")
        return []
    soup = BeautifulSoup(response.text,"html.parser") # parsing the HTML - using the inbuilt HTML parser
    quotes = [q.text for q in soup.find_all("span", class_="text")] # finds all the <span> tags with class="text"
    return quotes[:limit] # returns only the first limit number of quotes (5)

def quotes_to_df(quotes):
    df=pd.DataFrame(quotes, columns=["Quote"])
    return df 

    
'''
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
by Albert Einstein (about)
Tags: change deep-thoughts thinking world
“It is our choices, Harry, that show what we truly are, far more than our abilities.”
by J.K. Rowling (about)
Tags: abilities choices
“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
by Albert Einstein (about)
Tags: inspirational life live miracle miracles
“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”
by Jane Austen (about)
Tags: aliteracy books classic humor
“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
by Marilyn Monroe (about)
Tags: be-yourself inspirational
'''



