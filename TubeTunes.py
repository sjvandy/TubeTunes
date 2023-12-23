import os
from pytube import exceptions
from pytube import YouTube
from urllib.request import urlretrieve

#Declaring User's Download Folder
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

is_running = True

# Download Youtube Audio
def download_youtube_audio(link):
    yt = YouTube(link)

    # extract only audio 
    video = yt.streams.filter(only_audio=True).first() 

    # download the file 
    out_file = video.download(output_path=downloads_folder) 

    # save the file 
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 
    
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
