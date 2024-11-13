import tkinter as tk
from tkinter.simpledialog import Dialog
from tkinter import ttk
import tkintermapview as tkmap
from PIL import Image, ImageTk

class MyCustomDialog(Dialog):
    # arg with default value put in  the last
    # record is the necessary argument to initialize this Class

    def __init__(self, parent, record:list, title = None):
        # print(f"今天空氣是{record}")
        self.date=record[0]
        self.county=record[1]
        self.sitename=record[2]
        self.aqi=record[3]
        self.pm25=record[4]
        self.status=record[5]
        self.lat=float(record[6])
        self.lon=float(record[7])
        # if the calss directly super().__init__, end after execute super().__init__
        super().__init__(parent=parent, title=title)

    def body(self, master):
        ttk.Label(master, text=self.date,font=("Arial",18,"bold")).pack(pady=(0,20))
        main_frame=ttk.Frame(master,borderwidth=1)
        # ttk.Label(main_frame,text=self.status)
        main_frame.pack()

        # =====Canvas Left=====
        canvas_left=tk.Canvas(main_frame,width=200,height=200)
        # get color from "https://nipponcolors.com/"
        canvas_left.create_rectangle(10,10,190,190,outline="#B19693", width=2)

        if self.aqi<=50:
            path="green.png"
            self.status="良好"
        elif 50<self.aqi<=100:
            path="yellow.png"
            self.status="普通"
        else :
            path="red.png"
            self.status="不良"
        self.img=Image.open(path)
        self.image=ImageTk.PhotoImage(self.img)
        canvas_left.create_image(100, 50, image=self.image)
        canvas_left.create_text(100,150,text=f'AQI:{self.aqi}\n{self.status}',font=("Arial",18,"bold"),fill='#B19693')


        canvas_left.pack(side='left')
        # =====end Canvas_left======

        # =====Canvas Right=======
        canvas_right=tk.Canvas(main_frame,width=200,height=200)

        canvas_right.create_rectangle(10,10,190,190,outline="#B19693", width=2)

        if self.pm25<=15.4:
            path="green.png"
            self.pm25_status="良好"
        elif 15.<self.pm25<=35.4:
            path="yellow.png"
            self.pm25_status="普通"
        else :
            path="red.png"
            self.pm25_status="危險"
        self.img1=Image.open(path)
        self.image1=ImageTk.PhotoImage(self.img1)
        canvas_right.create_image(100, 50, image=self.image1)
        canvas_right.create_text(100,150,text=f'PM2.5:{self.pm25}\n{self.pm25_status}',font=("Arial",18,"bold"),fill='#B19693')


        canvas_right.pack(side='right')

        # =====End Canvas Right======

        # ======MapFrame========
        map_frame=ttk.Frame(master)
        map_widget = tkmap.TkinterMapView(map_frame,
                                         width=400,
                                         height=400,
                                         corner_radius=0
                                         )
        map_widget.set_position(self.lat, self.lon,marker=True)
        map_widget.set_zoom(15)
        map_widget.pack()
        map_frame.pack()
        # ======End Map Frame========




        
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