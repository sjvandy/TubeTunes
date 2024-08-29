import os
from pytubefix import exceptions
from pytubefix import YouTube
from pytubefix.cli import on_progress

#Declaring User's Download Folder
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

# Download Youtube Audio
def download_youtube_audio(url):
    yt = YouTube(url, on_progress_callback = on_progress)

    # extract only audio 
    stream = yt.streams.filter(only_audio=True).first() 

    # download the file 
    out_file = stream.download(output_path=downloads_folder, mp3=True)

    # save the file 
    base, _ = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 

    # Download Youtube Tumbnail
    filename_path = f"{downloads_folder}/{yt.title}.png"
    
    
os.system('clear')
print('Youtube to MP3 Converter')
print('Enter "quit" to exit')
while True:   
    user_input = input("Enter the Youtube Link: ")
    if user_input == 'quit': break
    else:
        try:
            print('Downloading...')
            download_youtube_audio(user_input)           
            print('Download Successful')               
        except Exception as e:
            if isinstance(e, exceptions.RegexMatchError):            
                print("Link is not a valid Youtube link. Try Again.")                     
            else:            
                print(f"Error: {e}")                       
