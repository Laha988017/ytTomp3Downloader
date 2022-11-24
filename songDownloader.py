import os
import re
from pytube import YouTube

from mp4tomp3 import convertmp4tomp3
file1 = open('playlistURLs.txt', 'r')
Lines = file1.readlines()
links = list()
for line in Lines:
    links.append(line.strip())
print("============Recieved from txt file================")
for link in links:
    try:
        print("Getting the URL "+link)
        youtube_1 = YouTube(link)
        title1 = youtube_1.title
        title = re.sub('[^a-zA-Z0-9 \n\.]', '', title1)
        youtube_1.title = title
        print(title)
        videos = youtube_1.streams.filter(
            progressive=True).order_by('resolution').desc().first()

        videos.download("video")
        print("Download Successful")
        convertmp4tomp3(title, os.getcwd()+"\\video\\"+title+".mp4")
    except Exception:
        continue
