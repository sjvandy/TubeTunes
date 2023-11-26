import os
from pytube import exceptions
from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *
from urllib.request import urlretrieve

#Declaring User's Download Folder
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

is_running = True

# Download Youtube Audio
def download_youtube_audio(link):
    try:
        yt = YouTube(link)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video.download(filename="movie.mp4")
        get_album_art(yt.thumbnail_url)
        convert_to_mp3(yt.title)        
    except Exception:
        pass
    try:
        p = Playlist(link)
        got_thumbnail = False
        get_album_art(p)
        for video in p.videos:
            current_video = video.streams.filter(progressive=True, file_extension='mp4').first()
            print('found video stream successfully')
            current_video.download(filename="movie.mp4")
            print('downloaded video')
            convert_to_mp3(video.title, p.title)
            if not got_thumbnail:
                print('grabbing thumbnail')
                get_album_art(video.thumbnail_url, p.title)
                got_thumbnail = True
                print('retrieved thumbnail')
            print('converting video to mp3')            
    except Exception:
        pass
    
# Convert MP4 video to MP3 format
def convert_to_mp3(title, playlist_title=None):
    # If link is a single Youtube video
    if playlist_title is None:
        print('no playlist name detected')
        try:
            video = VideoFileClip('movie.mp4')
            video.audio.write_audiofile(f"{downloads_folder}/{title}.mp3")
        except Exception as e:
            print(e)
    # If link is a Youtube Playlist
    else:
        print('playlist name detected')
        playlist_folder = os.path.join(downloads_folder, playlist_title)
        if not os.path.exists(playlist_folder):            
            os.mkdir(playlist_folder)
        try:
            video = VideoFileClip('movie.mp4')
            video.audio.write_audiofile(f"{playlist_folder}/{title}.mp3")
        except Exception as e:
            print(e)

    os.remove(f"{os.curdir}/movie.mp4")

#Download Thumbnail
def get_album_art(link, playlist_title=None):
    download_dir = downloads_folder
    if not playlist_title is None:
        download_dir = os.path.join(downloads_folder,playlist_title)        
    try:
        urlretrieve(link, f'{download_dir}/Thumbnail.jpg')
    except Exception as e:
        print(e)
    
    

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
            print(f"Error: {e}")                       