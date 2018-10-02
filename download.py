# Target URL:
# https://www.youtube.com/watch?v=hoEbaFmWeYs
# https://www.youtube.com/watch?v=0T2x8H5PXFU
# https://www.youtube.com/watch?v=62rWou_tTz4
# Youtube Result page
# https://www.youtube.com/results?search_query=turkce+ask+siir

# import required packages
import ssl
from pytube import YouTube
import time

# Page Crawler
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import datetime as dt

# solved the SSL issue
# ssl._create_default_https_context = ssl._create_unverified_context

# get all links from page
response = requests.get('https://www.youtube.com/results?search_query=turkce+ask+siir')
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# title = soup.find_all(attrs={"class": "yt-lockup-content"})
# print(title)

# links = title.find_all(attrs={"class": "spf-link"})
# print('link: '+link)

all_titles = []
all_links = []
for link in soup.find(role="main").find_all(attrs={"class": "yt-uix-tile-link"}):
    all_links.append(link.get('href'))
    all_titles.append(link.get_text())
print(all_links)

'''
<div class="yt-lockup-content">
<h3 class="yt-lockup-title ">
<a aria-describedby="description-id-101000"
class="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "
data-sessionlink="itct=CDIQ3DAYEyITCITkp67J590CFUt-WAodgEIHYSj0JFIPdHVya2NlIGFzayBzaWly"
dir="ltr" href="/watch?v=Evklercmrxs" rel="spf-prefetch"
title="En güzel ASK Sözleri (Kürtce ve Türkce)  Damar">En güzel ASK Sözleri (Kürtce ve Türkce)  Damar</a>
<span class="accessible-description" id="description-id-101000"> - 片長：2:32。</span></h3>
<div class="yt-lockup-byline ">
<a class="yt-uix-sessionlink spf-link " data-sessionlink="itct=CDIQ3DAYEyITCITkp67J590CFUt-WAodgEIHYSj0JA" href="/user/GuLaNeWroZan">Gula Newrozan</a>
</div><div class="yt-lockup-meta "><ul class="yt-lockup-meta-info"><li>6 年前</li>
<li>收看次數：104,975</li>
</ul>
</div>

<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">En güzel <b>ASK</b> Sözleri (Kürtce ve <b>Türkce</b>) (Gula min -Gülüm benim)</div></div>
'''

# Download videos using pytube
# def ytDownloader(link_lists):
#     for i in link_lists:
#         yt = YouTube(i)
#         yt.streams.filter(progressive=True, file_extension='mp4').first().download()
#         print('success Download!')
#         print('Start to sleep!')
#         time.sleep(10) # Sleep to avoid get banned
#         print('WakeUp!')

link_lists=['https://www.youtube.com/watch?v=hoEbaFmWeYs','https://www.youtube.com/watch?v=0T2x8H5PXFU']
# ytDownloader(link_lists)
