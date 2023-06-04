from moviepy.editor import *

clip0 = VideoFileClip("clip0.mp4")

clip1 = VideoFileClip("clip1.mp4")

result = concatenate_videoclips([clip0, clip1])

result.write_videofile("result.mp4")

