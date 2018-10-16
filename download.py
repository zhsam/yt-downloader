# Target URL:
# https://www.youtube.com/watch?v=hoEbaFmWeYs
# https://www.youtube.com/watch?v=0T2x8H5PXFU
# https://www.youtube.com/watch?v=62rWou_tTz4

# Youtube Result page
# https://www.youtube.com/results?search_query=turkce+ask+siir

# import packages for Youtube Page Crawler
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import datetime as dt

# import packages for downloading video
import ssl
from pytube import YouTube
import time

# solved the SSL issue
ssl._create_default_https_context = ssl._create_unverified_context

# get all links from page
response = requests.get('https://www.youtube.com/results?search_query=turkce+ask+siir')
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# obtain all the links to all_links
all_titles = []
all_links = []
for link in soup.find(role="main").find_all(attrs={"class": "yt-uix-tile-link"}):
    all_links.append(link.get('href'))
    all_titles.append(link.get_text())
print(all_links)

# Download videos using pytube
def ytDownloader(link_lists):
    for i in link_lists:
        yt = YouTube(i)
        yt.streams.filter(progressive=True, file_extension='mp4').first().download()
        print('success Download!')
        print('Start to sleep!')
        time.sleep(10) # Sleep to avoid get banned
        print('WakeUp!')

link_lists=['https://www.youtube.com/watch?v=hoEbaFmWeYs','https://www.youtube.com/watch?v=0T2x8H5PXFU']
# ytDownloader(link_lists)
