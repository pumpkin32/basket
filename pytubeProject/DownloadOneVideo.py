from pytube import YouTube

yt = YouTube("URL_YouTube")

yt.streams.filter(progressive=True, file_extension="mp4", res="720p").get_by_resolution("720p").download("./source")
