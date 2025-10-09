import requests
from flask import Flask
from bs4 import BeautifulSoup
from urllib.parse import urljoin, quote

# BASE = "https://forecast.weather.gov/"
# URL = "https://forecast.weather.gov/product.php?site=NWS&issuedby=OUN&product=AFD"


# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                   "AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/120.0.0.0 Safari/537.36",
# }

# session = requests.Session()
# session.headers.update(HEADERS)

# res = session.get(URL)
# soup = BeautifulSoup(res.text, "html.parser")

# # Find all nearby locations
# cards = soup.select("pre.glossaryProduct")

# def parse_names(a):
#     name = a.select_one("pre.glossaryProduct").get_text(strip=True)
#     return {"Name": name}

# results = parse_names("pre.glossaryProduct")
# print(results)

#specific word in the tag 
#array of sources to scrape from
#name them under an API path
#deploy them 

app = Flask(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
}

session = requests.Session()
session.headers.update(HEADERS)


    
res = session.get("https://www.weather.gov/dlh")
soup = BeautifulSoup(res.content, "html.parser")

content_div = soup.find('div', id = "wfomap_rtcol_bot")

if content_div:

    entries = content_div.find_all("div", class_="wwamap-legend-entry")

    for e in entries:

        alert_name = e.find("a").text.strip()
        alert_url = e.find("a")["href"]

        if " " in alert_url:    
            base, _, query = alert_url.partition('?')
            alert_url = f"{base}?{quote(query, safe='=&')}"
            
        full_url = urljoin("https://forecast.weather.gov/", alert_url)

        res1 = session.get(full_url)
        soup1 = BeautifulSoup(res1.content, "html.parser")

        content_div1 = soup1.find('div', id = "content")

        desc = content_div1.find_all("pre")

        print({
            "Alert" : alert_name,
            "Descriptions" : desc
        })

else:
    print({
        "Error" : ValueError
})











    