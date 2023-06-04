from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=lI1-_jyv45g&ab_channel=KorAngar")

yt.streams.filter(progressive=True, file_extension="mp4", res="720p").get_by_resolution("720p").download("./source")
