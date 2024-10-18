from ttkthemes import ThemedTk #現成的css
from tkinter import ttk 

class Window(ThemedTk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title()
        self.geometry('300x500')
        self.title("有夠可愛")
        style=ttk.Style(self)
        style.configure('Main.TButton',font=('Arial',18))
        btn1=ttk.Button(self,text="Click Me!")#Button類別(父類別)
        btn1.pack(ipadx=10,ipady=10,padx=10,pady=100)#ipad=inner padding距離,pad=外面的padding

def main():
    root=Window(theme='black')
    root.mainloop()

if __name__=='__main__':
    main()