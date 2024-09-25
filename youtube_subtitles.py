#https://pytubefix.readthedocs.io/en/latest/index.html
#https://pytubefix.readthedocs.io/en/latest/user/captions.html


from pytubefix import YouTube
from pytubefix.cli import on_progress

nightwish = 'https://www.youtube.com/watch?v=pvkYwOJZONU'
#nightwish:  https://www.youtube.com/watch?v=pvkYwOJZONU



yt = YouTube(nightwish)
subtitles = yt.captions

caption = yt.captions.get_by_language_code('en')
caption.save_captions("captions.txt")
