from model import Model
from view import View
import tkinter as tk
import pyperclip as py

class Controller(tk.Tk):
    #constructor
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def first(self):

        self.view.GUI()

    #will be removed/modified
    #def Mp3Control(self):
    #    urlString = self.view.urlEntry.get()
    #    self.model.Mp3Logic(urlString)
    #    self.view.modifyURLEntry()

    #will be removed/modified
    #def Mp4Control(self):
    #    urlString = self.view.urlEntry.get()
    #    self.model.Mp4Logic(urlString)
    #    self.view.modifyURLEntry()


    def download(self):
        urlString = self.view.urlEntry.get()

        if self.view.menu.get() == "mp3":
            self.model.Mp3Logic(urlString)
            self.view.modifyURLEntry()
        elif self.view.menu.get() == "mp4":
            self.model.Mp4Logic(urlString)
            self.view.modifyURLEntry()

    def OpenFolder(self):
        self.model.OpenFolderLogic()

    def SaveFolder(self):
        self.model.SaveFolderLogic()
        self.view.folderEntry.delete(0, tk.END)
        self.view.folderEntry.insert(0, self.model.folderName)
        print(self.model.folderName)

    def PasteLink(self):
        #using a 3rd party module pyperclip to do the pasting function
        self.view.urlEntry.insert(0, py.paste())