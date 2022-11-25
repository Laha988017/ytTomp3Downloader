import os
import moviepy.editor as mp
from tkinter.filedialog import *


def convertmp4tomp3(title, url):
    try:
        path = url
        # askopenfilename()
        output = "audio//"+title+".mp3"
        video = mp.VideoFileClip(path)
        video.audio.write_audiofile(output)
        print("====END====")
    except Exception as e:
        print(e)
        print("=====Problem occured while converting=======")
        file1 = open("notConverted.txt", "a")  # append mode
        file1.write(title+" \n")
        file1.close()
