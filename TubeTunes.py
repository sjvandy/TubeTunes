import os
from pytube import exceptions
from pytube import YouTube

# Allows user to download multiple audio clips without restarting program
isRunning = True

downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

# Download Youtube Audio
def Download_Youtube_Audio(link):
    yt = YouTube(link)
    print("Downloading...")
    audio = yt.streams.filter(only_audio=True).first()
    audio.download(filename=f"{yt.title}.mp3", output_path=downloads_folder)

#Program Welcome Prompt
print("TubeTunes")
print("Youtube to mp3 converter")
print('To close program, hit option C or type "quit"')

while isRunning:
    responce = input('Enter Youtube Link: ')
    if responce == 'quit':
        isRunning = False
        break
    else:
        try:
            Download_Youtube_Audio(responce)    
            print("Youtube Audio Downloaded Successfully")
        except Exception as e:
            if isinstance(e, exceptions.RegexMatchError):
                print('Error: Link is not a valid Youtube link. Try Again.')
            else:
                print(f"Error: {type(e)}")            