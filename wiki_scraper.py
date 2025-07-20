import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import json

url = "https://en.wikipedia.org/wiki/List_of_dates_predicted_for_apocalyptic_events"

def connect_to_wikipedia(url):

    # Send a GET request to the URL
    response = requests.get(url)  

    # Check if the request was successful
    if response.status_code == 200:
        return BeautifulSoup(response.text, "html.parser")  # Parse and return the HTML
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None  # Return None if the request fails

# target_headings = ["Future predictions", "Scientific predictions"]

def find_h2(soup):

    tables = []
    target_headings = ["Future predictions", "Scientific far future predictions"]

    # Loop through h2
    for h2 in soup.find_all("h2"):
        
        # If h2 is target value, find next element
        if h2.text.strip() in target_headings:
            next_el = h2.find_next("table", {"class": "wikitable"})
            table_html = StringIO(str(next_el))  # Convert table HTML to string
            df = pd.read_html(table_html)[0]  # Read the HTML table into a DataFrame
            tables.append(df)

            #print(next_el.prettify())

    return tables

def get_data():
    soup = connect_to_wikipedia(url)
    prophesies = find_h2(soup)
    return prophesies

# for table in prophesies:
#     print("="*20)
#     print(table)
