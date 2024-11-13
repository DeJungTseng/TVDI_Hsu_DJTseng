import tkinter as tk
from tkinter.simpledialog import Dialog

class MyCustomDialog(Dialog):
    # arg with default value put in  the last
    # record is the necessary argument to initialize this Class

    def __init__(self, parent, record:list, title = None):
        print(f"今天空氣是{record}")
        # if the calss directly super().__init__, end after execute super().__init__
        super().__init__(parent=parent, title=title)

    def body(self, master):
        # 創建對話框主體。返回應具有初始焦點的控件。
        tk.Label(master, text="請輸入你的名字:").grid(row=0)
        # self.name_entry get the entry
        # tk.Entry : upon initial the window, you can key in str
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)
        return self.name_entry
    
    def apply(self):
        # 當用戶按下確定時處理數據
        print("我被按了!!!")
        self.result = self.name_entry.get()

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