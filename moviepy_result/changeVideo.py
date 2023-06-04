from moviepy.editor import *

video = VideoFileClip("video.mp4")

print(video.w, video.h)

result = video.resize(width = 1920, height = 1080)

result.write_videofile("result.mp4")
