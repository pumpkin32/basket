import os

iter = 0

for i in os.listdir("folder"):
	os.rename("folder" + "/" + i, f"folder/picture{iter}.png")
	iter += 1

os.system("ffmpeg -r 1/1 -i folder/picture'%d'.png result.avi")
