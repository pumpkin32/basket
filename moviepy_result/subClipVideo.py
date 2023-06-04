from moviepy.editor import *
import datetime

#указываем начала сегмента который надо вырезать
startTime = datetime.timedelta(minutes = 0, seconds = 0)
#указываем конец егмента который нужно вырезать
endTime = datetime.timedelta(minutes = 0, seconds = 0)


INPUT = VideoFileClip("video.mp4")

result = INPUT.subclip(startTime.seconds, endTime.seconds)

result.write_videofile("result.mp4")
