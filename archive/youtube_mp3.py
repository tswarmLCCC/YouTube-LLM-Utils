#https://pytubefix.readthedocs.io/en/latest/index.html

from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input("URL >")
#nightwish:  https://www.youtube.com/watch?v=pvkYwOJZONU


yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)

ys = yt.streams.get_audio_only()
ys.download(mp3=True)



