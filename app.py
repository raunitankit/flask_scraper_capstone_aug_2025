# save this as app.py
from flask import Flask, render_template
from scraper import scrape_quotes, quotes_to_df


app = Flask(__name__) # is the most important line in Flask

# __name__  is a special built-in Python variable. 
'''
In Each python file, __name__ contains the name of the current module - whcih happens to be the file itself in here it is app.py 

'''

@app.route("/") # decorating the function that we will create. / enter
# def hello():
#     return "Hello, World!"
def dashboard():
    quotes = scrape_quotes(limit=10)
    #convert into panadas dataframe
    df = quotes_to_df(quotes)
    #print(df)   - note remove this
    return render_template("dashboard.html", tables=[df.to_html(classes='data')], titles=df.columns.values)



# @app.route("/about")
# def about_poage():
#     pass

'''
"/" - Dashboard
"/about" - about_page()
"/api/data" - api_data()
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)
