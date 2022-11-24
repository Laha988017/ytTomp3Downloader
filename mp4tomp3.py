import os
import moviepy.editor as mp
from tkinter.filedialog import *


def convertmp4tomp3(title, url):
    path = url
    # askopenfilename()
    output = "audio//"+title+".mp3"
    video = mp.VideoFileClip(path)
    video.audio.write_audiofile(output)
    print("====END====")
