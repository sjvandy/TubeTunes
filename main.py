from pytube import YouTube
import os

downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

def Download_Youtube_Audio(link):
    yt = YouTube(link)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download(filename=f"{yt.title}.mp3", output_path=downloads_folder)

youtube_link = input('Enter Youtube Link: ')
try:
    Download_Youtube_Audio(youtube_link)
finally:
    print("Youtube Audio Downloaded Successfully")