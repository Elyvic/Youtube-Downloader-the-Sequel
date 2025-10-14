import tkinter as tk
from tkinter import filedialog
import pyperclip as py


class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        #all images
        self.savePhoto = tk.PhotoImage(file = r"resources/SaveButton.png")
        self.folderPhoto = tk.PhotoImage(file =r"resources/folderButton.png")
        self.pastePhoto = tk.PhotoImage(file = r"resources/pasteButton.png")

        self.title("Youtube Downloader the Sequel")
        self.geometry("400x190")
        self.resizable(False, False)

        self.GuiStuff()
        self.Buttons()
        self.DropDownMenu()
        self.Placements()

    def GuiStuff(self):
        self.urlLabel = tk.Label(self, text="URL:")
        self.urlEntry = tk.Entry(self, textvariable = "", width=50)

        self.folderEntry = tk.Entry(self, textvariable = '', width=40, justify = "center", state = "disabled")


    def Buttons(self):
        #note to self: don't put parenthesis on the command section of the button or they'll run automatically

        #self.mp3Button = tk.Button(self, text="Mp3", command=self.controller.Mp3Control) #will be removed in the future
        #self.mp4Button = tk.Button(self, text="Mp4", command=self.controller.Mp4Control) #will bbe removed in the future
        self.folderButton = tk.Button(self, command=self.controller.OpenFolder, image=self.folderPhoto, height = 21, width = 25)
        self.fileButton = tk.Button(self, command=self.controller.SaveFolder, image=self.savePhoto)
        self.pasteButton = tk.Button(self, command = self.controller.PasteLink, image = self.pastePhoto)
        self.downloadButton = tk.Button(self, command = self.controller.download, text= "Download", height = 3, width = 15)

    def DropDownMenu(self):
        self.menu = tk.StringVar()
        self.menu.set("mp3")

        self.drop = tk.OptionMenu(self, self.menu, "mp3", "mp4", "audio")

    def Placements(self):
        self.urlLabel.place(x=30, y=30)
        self.urlEntry.place(x=60, y=30)
        self.folderEntry.place(x=85, y=55)
        #self.mp3Button.place(x=0, y=95) #remove later
        #self.mp4Button.place(x=40, y=95) #remove later
        self.folderButton.place(x=220, y=82)
        self.fileButton.place(x=366, y=55)
        self.pasteButton.place(x =366 , y = 28)
        self.downloadButton.place(x=145, y = 115)
        self.drop.place(x = 150, y =80 )

    def modifyURLEntry(self):
        self.urlEntry.delete(0, tk.END)
        self.urlEntry.insert(0, "")

    def modifyFolderEntry(self, folderName):
        self.folderEntry.config(state = "normal")
        self.folderEntry.delete(0, tk.END)
        self.folderEntry.insert(0, folderName)
        self.folderEntry.config(state = "disabled")

    #figure the logic for this later
    def modifySaveFolder(self, folderName):
        folderName = filedialog.askdirectory()

        return folderName

    def pasteURLEntry(self):
        self.urlEntry.insert(0, py.paste())

    def GUI(self):
        print("victor sucks")
        self.mainloop()