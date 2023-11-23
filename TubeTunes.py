import os
from pytube import exceptions
from pytube import YouTube
import tkinter as tk
from moviepy.editor import *

#Declaring User's Download Folder
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

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
def button_pushed():   
    user_input = textbox.get()
    try:
        download_youtube_audio(user_input)            
        result_label.config(text='Download Successful!')                
    except Exception as e:
        if isinstance(e, exceptions.RegexMatchError):            
            result_label.config(text="Link is not a valid Youtube link. Try Again.") 
            print('Error Occured with Link')                
        else:            
            result_label.config(text=f"Error: {type(e)}")
            print('Error Occured')               
    
def key_input(event):    
    button_pushed()    


#GUI User Interface
root = tk.Tk()

root.geometry("500x300")
root.title("TubeTunes")

title = tk.Label(root, text="Youtube to MP3 Converter", font=('Helvetica', 18))
title.pack(padx=20, pady=30)

label = tk.Label(root, text="Enter a Youtube Link", font=('Helvetica', 14))
label.pack(padx=20, pady=15)
root.bind('<Return>', key_input)

textbox = tk.Entry(root, width=40)
textbox.pack(padx=10)

button = tk.Button(root, text='Download MP3', font=('Helvetica', 18), height=3, command=button_pushed)
button.pack(padx=20, pady=10)

global result_label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()