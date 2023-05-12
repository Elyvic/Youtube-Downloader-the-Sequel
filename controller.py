from model import Model
from view import View
import tkinter as tk

class Controller(tk.Tk):
    #constructor
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def first(self):

        self.view.GUI()

    def Mp3Control(self):
        urlString = self.view.urlEntry.get()
        self.model.Mp3Logic(urlString)

        self.view.modifyURLEntry()


    def Mp4Control(self):
        urlString = self.view.urlEntry.get()
        self.model.Mp4Logic(urlString)

        self.view.modifyURLEntry()

    def OpenFolder(self):
        self.model.OpenFolderLogic()

    def SaveFolder(self):
        self.model.SaveFolderLogic()
        print(self.model.folderName)