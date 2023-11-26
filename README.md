# TubeTunes 🎶
Youtube to MP3 Converter ( Edition)

I got tired of using those websites with tons of ads and misleading download links, so I made a script myself. Enjoy!

# Requirements
- [HomeBrew for Mac](https://brew.sh)
> Ensure you paste the echo path link prompted by Brew after installation
- Install FFmpeg with `brew install ffmpeg`
> Verify that you have FFmpeg installed by typing `ffmpeg -h`

## Updates
#### Issues with Tkinter and FFmpeg
* Due to issues with ffmpeg not working with pyinstaller, converted app back into command prompt version since prerequisites need to be installed prior to application use.

#### Playlists are now downloadable!
* You read that right! You can now download entire playlists at once! They will be installed in their own folder called the playlist title in your Downloads folder along side a temporary albumn thumbnail.
___
### Roadmap
Eventually I will find a way to get ffmpeg instaled directly into the program without taking too much space, from there I will then bring back the UI with Tkinter once it is resolved.

