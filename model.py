import os
import subprocess
from tkinter import filedialog
from pytube import YouTube

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
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        fileName = video.download(output_path = self.folderName)

        source = fileName

        if " " in fileName:
            os.rename(source, source.replace(" ", "_"))
            fileName = source.replace(" ", "_")

        fileNoExt = os.path.splitext(fileName)[0]
        subprocess.run(f"ffmpeg -i {fileName} {fileNoExt}.mp3", shell = True)
        os.remove(fileName)

        #base, ext = os.path.splitext(fileName)
        #mp3File = base + '.mp3'
        #os.rename(fileName, mp3File)

        #command = f"ffmpeg -i {file_name} {file_without_ext}.mp3"

        print("done")

    def Mp4Logic(self, url):
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path = self.folderName)

        print("done")