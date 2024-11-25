import os
import subprocess
from tkinter import filedialog
#from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress

#pytube doesn't seem to work now. pytubefix temp fix. might need change to different module in the future
class Model:
    def __init__(self):
        self.folderName = " "

    def OpenFolderLogic(self):
        path = self.folderName
        path = os.path.realpath(path)
        os.startfile(path)

    def SaveFolderLogic(self):
        self.folderName = filedialog.askdirectory()



    def Mp3Logic(self, url):
        # test with the link below:
        #             https://www.youtube.com/watch?v=hW4Hi_zG79M          -       as we fade away
        #             https://www.youtube.com/watch?v=3eq-qUy-a-A          -       apex of the world


        # added the authentication stuff for the download to work
        yt = YouTube(url, use_oauth = True, allow_oauth_cache = True, on_progress_callback = on_progress)
        video = yt.streams.filter(only_audio=True).first()
        fileName = video.download(output_path = self.folderName)

        source = fileName

        #this doesn't work when a folder name has space in the directory
        if " " in fileName:
            os.rename(source, source.replace(" ", "_"))
            fileName = source.replace(" ", "_")
            print(fileName)


        fileNoExt = os.path.splitext(fileName)[0]
        subprocess.run(f"ffmpeg -i {fileName} {fileNoExt}.mp3", shell = True)
        os.remove(fileName)

        #base, ext = os.path.splitext(fileName)
        #mp3File = base + '.mp3'
        #os.rename(fileName, mp3File)

        #command = f"ffmpeg -i {file_name} {file_without_ext}.mp3"

        print("done")

    def Mp4Logic(self, url):
        #  test for video download
        #            https://www.youtube.com/watch?v=aEmQbRCWjfQ      -          community end credit puppet rap
        #            https://www.youtube.com/watch?v=9Jxw_NAKUn0      -          simple and clean mree cover


        # added the authentication stuff for the download to work
        yt = YouTube(url, use_oauth = True, allow_oauth_cache = True)
        video = yt.streams.get_highest_resolution()
        video.download(output_path = self.folderName)

        print("done")