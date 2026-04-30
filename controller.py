from model import Model
from view import View
#import tkinter as tk

#put tk.TK in parenthesis after "class Controller" if using tkinter in controller again
class Controller:
    #constructor
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def startHere(self):
        self.view.GUI()

    def download(self):
        urlString = self.view.urlEntry.get()

        if self.view.menu.get() == "Legacy":       #convert using powershell. no special characters allowed
            self.model.Mp3PowershellLogic(urlString)
            self.view.modifyURLEntry()
        elif self.view.menu.get() == "mp4":
            self.model.Mp4Logic(urlString)
            self.view.modifyURLEntry()
        elif self.view.menu.get() == "mp3":
            self.model.mp3MoviePyLogic(urlString)  #convert using moviepy module. can use special characters
            self.view.modifyURLEntry()

    def OpenFolder(self):
        self.model.OpenFolderLogic()

    def SaveFolder(self):
        folderName = self.view.modifySaveFolder()

        self.model.SaveFolderLogic(folderName)
        self.view.modifyFolderEntry(self.model.folderName)
        print(self.model.folderName)

    def PasteLink(self):
        #using a 3rd party module pyperclip to do the pasting functionality
        #self.view.urlEntry.insert(0, py.paste())
        self.view.pasteURLEntry()