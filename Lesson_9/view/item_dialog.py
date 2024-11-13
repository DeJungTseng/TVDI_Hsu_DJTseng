import tkinter as tk
from tkinter.simpledialog import Dialog
from tkinter import ttk
from tkinter import Tk, Canvas, Frame, BOTH
from PIL import Image, ImageTk

class MyCustomDialog(Dialog):
    # arg with default value put in  the last
    # record is the necessary argument to initialize this Class

    def __init__(self, parent, record:list, title = None):
        print(f"今天空氣是{record}")
        self.date=record[0]
        self.county=record[1]
        self.sitename=record[2]
        self.aqi=record[3]
        self.pm25=record[4]
        self.status=record[5]
        self.lon=float(record[6])
        self.lat=float(record[7])
        # if the calss directly super().__init__, end after execute super().__init__
        super().__init__(parent=parent, title=title)

    def body(self, master):
        main_frame=ttk.Frame(master,borderwidth=1,relief='groove')
        ttk.Label(main_frame,text=self.status).pack()

        # =====Canvas Left=====
        canvas_left=tk.Canvas(main_frame,width=200,height=200)
        # get color from "https://nipponcolors.com/"
        # canvas_left.create_rectangle(10,10,190,190,outline="#60373E", width=2)
        canvas_left.create_text(100,150,text=f'AQI:{self.aqi}\n{self.status}',font=("Arial",18,"bold"),fill='#0089A7')

        if self.aqi<=50:
            self.image=Image.open("green.png")
            self.green=ImageTk.PhotoImage(self.image)
            canvas_left.create_image(100, 50, image=self.green)
        elif 50<self.aqi<=100:
            self.image=Image.open("yellow.png")
            self.yellow=ImageTk.PhotoImage(self.image)
            canvas_left.create_image(100, 50, image=self.yellow)
        else :
            self.image=Image.open("red.png")
            self.red=ImageTk.PhotoImage(self.image)
            canvas_left.create_image(100, 50, image=self.red)
        canvas_left.pack(side='left')
        # =====end Canvas_left

        canvas_right=tk.Canvas(main_frame,width=200, height=200)
        canvas_right.create_oval(10, 10, 80, 80, outline="#000",fill="#4fe", width=2)
        canvas_right.create_text(200,150,text="Good",font=("Arial",24,"bold"),fill='blue')
        canvas_right.pack(side='right')




        
        main_frame.pack(expand=True,fill='x')


        
    def apply(self):
        # 當用戶按下確定時處理數據
        print("我被按了!!!")


    def buttonbox(self):
        # Add custom buttons (overriding the default buttonbox)
        box = tk.Frame(self)
        self.ok_button = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        self.ok_button.pack(side=tk.LEFT, padx=5, pady=5)
        # the button bind to klick and do command =self.cancel function
        self.cancel_button = tk.Button(box, text="Cancel", width=10, command=self.cancel)
        self.cancel_button.pack(side=tk.LEFT, padx=5, pady=5)
        # the window self bind('<keyboard>'event, do self.ok)
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        box.pack()
    
    def ok(self, event=None):
        # Override the ok method
        print("OKㄌ!")
        # execute the ok() function of parent Class 
        super().ok()
        
    def cancel(self, event=None):
        # Override the ok method
        print("鼻要!")
        # execute the ok() function of parent Class 
        super().cancel()