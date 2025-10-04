'''
pytest -> the testing framework. Lets you write tests as simple functions.
we import out 2 functions from scraper.py so that we can test them.
test the quotes
call quotes_to_df
it will give us a dataframe
TC1: df.shape[2] ---> confirms 2 rows exist  
TC2: "quote" in the columns - confirms that the Dataframe has a coulmn called Quote.
TC3: quote should not be empty
If either tc fails, then the whole test suite fails.
webpage is down - we need to confirm.
'''

from scraper import scrape_quotes, quotes_to_df

# Python function that we are going to use just to test our code

def test_scrape_quotes():
    quotes=scrape_quotes(limit=2)
    assert len(quotes) == 2

def test_quotes_to_df():
    df = quotes_to_df(["Hello", "World"])
    assert df.shape[0] == 2
    assert "Quote" in df.columns







