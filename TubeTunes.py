import os
from pytube import exceptions
from pytube import YouTube
from moviepy.editor import *

#Declaring User's Download Folder
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

is_running = True

# Download Youtube Audio
def download_youtube_audio(link):
    yt = YouTube(link)    
    video = yt.streams.filter(progressive=True, file_extension='mp4').first()
    video.download(filename="movie.mp4")
    convert_to_mp3(yt.title)

def convert_to_mp3(title):
    try:
        video = VideoFileClip('movie.mp4')
        video.audio.write_audiofile(f"{downloads_folder}/{title}.mp3")
    except Exception as e:
        print(e)
    os.remove(f"{os.curdir}/movie.mp4")

# Define Button Click
print('Youtube to MP3 Converter')
while is_running:   
    user_input = input("Enter the Youtube Link: ")
    try:
        print('Downloading...')
        download_youtube_audio(user_input)            
        print('Download Successful')               
    except Exception as e:
        if isinstance(e, exceptions.RegexMatchError):            
            print("Link is not a valid Youtube link. Try Again.")         
        else:            
            print(f"Error: {type(e)}")                       