from pytube import Playlist
from tqdm import tqdm

yt = Playlist("URL_YouTube")


for video in tqdm(yt.videos):
	try:
		video.streams.filter(progressive=True, file_extension="mp4", res="720p").get_by_resolution("720p").download("./source")		
	except:
		print(video.watch_url)
		with open("log.txt", "a") as f:
			f.write(video.watch_url)
			f.close()
