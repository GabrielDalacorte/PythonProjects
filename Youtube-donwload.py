
# pip install pytube

from pytube import YouTube

# Link do video

get_link = input()

yt = YouTube(get_link)

yt.streams.all()

stream = yt.streams.get_highest_resolution()
stream.download()




