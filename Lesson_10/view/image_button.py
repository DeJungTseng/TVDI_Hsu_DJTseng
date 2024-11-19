from tkinter import ttk
from PIL import Image, ImageTk

class ImageButton(ttk.Button):
    # command is the arg 
    def __init__(self, master=None,**kwargs):
        # parent class define image
        # the image put in the project's root index in Lesson8 (where terminal execute)
        # relative route: the root is where the terminal runs on
        self.icon_image=Image.open("refresh.png")
        self.icon_photo=ImageTk.PhotoImage(self.icon_image)
        # super the image
        super().__init__(master=master,image=self.icon_photo,**kwargs)