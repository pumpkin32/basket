from moviepy.editor import *
import os

listFolder = os.listdir("source")

for i in listFolder:

	video = VideoFileClip(f"source/{i}")

	audio = video.audio

	audio.write_audiofile(f"source/{i}.mp3")

