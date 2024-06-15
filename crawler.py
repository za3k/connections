#!/bin/python3
"""
Crawl the NYTimes Connections word game.
"""

import datetime
import pathlib
import requests
import os

first_day = datetime.date(2023, 6, 12)
today = datetime.date.today()

def open_with_paths(path, *args, **kwargs):
    pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
    return open(path, *args, **kwargs)

def crawl_date(date):
    url = date.strftime("https://www.nytimes.com/svc/connections/v2/%Y-%m-%d.json")
    json = date.strftime("data/%Y/%Y-%m-%d.json")
    if os.path.exists(json):
        return
    response = requests.get(url)
    if response.status_code == 200:
        print(url, "->", json)
        with open_with_paths(json, 'wb') as f:
            f.write(response.content)
    else:
        print(url, "failed")

if __name__ == '__main__':
    for date in (first_day + datetime.timedelta(n) for n in range((today-first_day).days+1)):
        crawl_date(date)
