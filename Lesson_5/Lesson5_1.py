from  tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo

# define a class Window inherited from Themedtk
class Window(ThemedTk):
    #initialize this class
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #start laypot from here!
        self.title('登入你的可愛')
        # ====Style===
        # create an instance named "style" in the Style class in ttk package
        style=ttk.Style(self)
        # configure the attribute of font of the TLabel class of TopFrame
        style.configure('TopFrame.TLabel',font=('Arial',20))
        #====End of Style=====

        #=====Top Frame=====
        TopFrame=ttk.Frame(self)
        # create Label instance in Label class and pack
        # if there's not a variation gave to represent Label, it cannot be edited
        ttk.Label(TopFrame,text='你是哪隻可愛',style='TopFrame.TLabel').pack()
        TopFrame.pack(padx=20,pady=20)
        #===End of Top Frame====

        #===Bottom Frame===
        BottomFrame=ttk.Frame(self)
        # create an instance of Label in bOTTON fRAME and make it in memory by pack()
        # if you don't have a need to modify it , no var needed to represent it.
        # var stands for a instance is required when we have to call it in other where in the program

        # create Label to fill text in the window
        ttk.Label(BottomFrame,text='User Name').grid(row=0,column=0,pady=10)
        ttk.Label(BottomFrame,text='Password').grid(row=1,column=0,pady=10)
        # The weight determines how wide the column will occupy, which is relative to other columns.
        BottomFrame.columnconfigure(index=0,weight=1)
        BottomFrame.columnconfigure(index=0,weight=9)

        # create an attribute username and bind to Entry by assign to textvariable
        # username=stringVar=input()
        self.username=tk.StringVar()
        ttk.Entry(BottomFrame,textvariable=self.username).grid(row=0,column=1,sticky='E')

        self.password=tk.StringVar()
        ttk.Entry(BottomFrame,textvariable=self.password,show='*').grid(row=1,column=1,sticky='E')

        #=======row2==========
        radioFrame=ttk.Frame(BottomFrame).grid(row=2,column=0,columnspan=2)
        sizes = (('Small', 'S'),
                ('Medium', 'M'),
                ('Large', 'L'),
                ('Extra Large', 'XL'),
                ('Extra Extra Large', 'XXL'))
        label = ttk.Label(radioFrame,text="What's your t-shirt size?")
        label.pack(fill='x', padx=5, pady=5)
        #=======end row2=======

        # ===create 2 buttons====
        cancel_btn=ttk.Button(BottomFrame,text='今晚可愛',command=self.cancel_click)
        cancel_btn.grid(row=3,column=0)
        # sticky attribute, to the East direction
        ok_btn=ttk.Button(BottomFrame,text='馬上可愛',command=self.ok_click)
        ok_btn.grid(row=3,column=1,sticky='E')
        #===========================

        BottomFrame.pack(expand=True,fill='x',ipadx=10,ipady=10,padx=20,pady=(0,20))
        #===End of Bottom Frame===

        #end laypot here

    #define instance function below
    # if click cancel, clear the content
    def cancel_click(self):
        self.username.set("")
        self.password.set("")
    def ok_click(self):
        username=self.username.get()
        password=self.password.get()
        # messagebox popout messagebox
        showinfo(title="可愛的你是",message=f"可愛的名字是:{username}\n通關密語是:{password}")

# create function of the document
def main():
    # create an instance in class Window, named "window"
    #give a theme style to this window
    window=Window(theme='arc')
    # call attribute string variation 
    # window.username.set('在這裡輸入可愛的名字')
    # window.password.set('在這裡輸入通關密語')
    window.mainloop()
if __name__=='__main__':
    main()
