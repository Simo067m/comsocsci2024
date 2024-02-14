import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def get_researcher_names():
    # Define variables and collect content
    LINK = "https://ic2s2-2023.org/program"
    r = requests.get(LINK)
    soup = BeautifulSoup(r.content)
    # Find all the names from the top table
    names = []
    # Find all the table rows
    table = soup.find("table", class_="summary")
    table_rows = soup.find_all("tr")
    for tr in table_rows:
        tds = tr.find_all("td")
        for row in tds:
            a = row.find_all("a")
            for text in a:
                text_content = text.text
                if ("Keynote" in text_content):
                    text_split = text_content.split("-")
                    stripped = text_split[1].strip()
                    if (stripped not in names):
                        names.append(stripped)
    
    # Find all the names from the bottom lists
    # Find all the unordered lists
    ul = soup.find_all("ul", class_="nav_list")
    # Find all the list elements
    for list in ul:
        found_names = list.find_all("i")
        # For every found name line, seperate into individual names
        for name in found_names:
            found_names_seperated = name.text.split(", ")
            for seperated_name in found_names_seperated:
                if (seperated_name.strip() not in names):
                    names.append(seperated_name.strip())
    
    # Find all the names of the chairs
    headers = soup.find_all("h2")
    for header in headers:
        text = header.find("i")
        if (text is not None):
            seperated_name = text.text.split(": ")
            if (seperated_name[1].strip() not in names):
                names.append(seperated_name[1].strip())
    
    return names