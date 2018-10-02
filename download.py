# Target URL:
# https://www.youtube.com/watch?v=hoEbaFmWeYs
# https://www.youtube.com/watch?v=0T2x8H5PXFU
# https://www.youtube.com/watch?v=62rWou_tTz4

# import required packages
import ssl
from pytube import YouTube
import time

# solved the SSL issue
ssl._create_default_https_context = ssl._create_unverified_context

# get all links from page


# Download videos using pytube
def ytDownloader(link_lists):
    for i in link_lists:
        yt = YouTube(i)
        yt.streams.filter(progressive=True, file_extension='mp4').first().download()
        print('success Download!')
        time.sleep(10) # Sleep to avoid get banned
        print('WakeUp!')

link_lists=['https://www.youtube.com/watch?v=hoEbaFmWeYs','https://www.youtube.com/watch?v=0T2x8H5PXFU']
ytDownloader(link_lists)
