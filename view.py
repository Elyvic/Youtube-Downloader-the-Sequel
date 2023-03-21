import tkinter as tk

class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.savePhoto = tk.PhotoImage(file=r"resources/SaveButton.png")
        self.folderPhoto = tk.PhotoImage(file=r"resources/folderButton.png")

        self.title("Youtube Downloader the Sequel")
        self.geometry("400x120")
        self.resizable(False, False)

        self.GuiStuff()
        self.Buttons()
        self.Placements()

    def GuiStuff(self):
        self.urlLabel = tk.Label(self, text="URL:")
        self.urlEntry = tk.Entry(self, textvariable=" ", width=50)


    def Buttons(self):
        #note to self: don't put parenthesis on the command section of the button or they'll run automatically
        self.mp3Button = tk.Button(self, text="Mp3", command=self.controller.Mp3Control)
        self.mp4Button = tk.Button(self, text="Mp4", command=self.controller.Mp4Control)
        self.folderButton = tk.Button(self, command=self.controller.OpenFolder, image=self.folderPhoto)
        self.fileButton = tk.Button(self, command=self.controller.SaveFolder, image=self.savePhoto)

    def Placements(self):
        self.urlLabel.place(x=30, y=30)
        self.urlEntry.place(x=60, y=30)
        self.mp3Button.place(x=160, y=60)
        self.mp4Button.place(x=195, y=60)
        self.folderButton.place(x=375, y=95)
        self.fileButton.place(x=366, y=28)

    def modifyURLEntry(self):
        self.urlEntry.delete(0, tk.END)
        self.urlEntry.insert(0, "")

    def GUI(self):
        print("victor sucks")
        self.mainloop()