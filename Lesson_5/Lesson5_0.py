from ttkthemes import ThemedTk #現成的css
from tkinter import ttk 

class Window(ThemedTk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title()
        self.title("有夠可愛")
        style=ttk.Style(self)
        #===================TOP FRAME==================================================================#
        topFrame=ttk.Frame(self,borderwidth=1,relief='groove')
        #change regional variation in __init__ to instance attribute to let the whole class use it 
        self.btn1=ttk.Button(topFrame,text='Say Yeah!',command=self.yeah)#bind an instance method to do upon this event
        self.btn1.pack(side='left',padx=10,expand=True)
        self.btn2=ttk.Button(topFrame,text='Say Meow',command=self.meow)#Click this botton , execute instance method bind
        self.btn2.pack(side='left',padx=10,expand=True)
        self.btn3=ttk.Button(topFrame,text='Wave Hello',command=self.hello)
        self.btn3.pack(side='left',padx=10,expand=True)
        topFrame.pack(ipadx=10,expand=True,fill='x')
        #==================End TOP FRAME====================================================#
        #===================BOTTOM FRAME===============================================================#
        buttomFrame=ttk.Frame(self,borderwidth=1,relief='groove')
        
        #===================BOTTOM FRAME LEFT===============================================================#
        buttomFrameL=ttk.Frame(self,borderwidth=1,relief='groove')
        #event binding
        btn4=ttk.Button(buttomFrameL,text='按我按我')
        #bind event to instance function self.click 
        btn4.bind('<Button>',self.click)
        btn4.pack(side='top',ipady=30,padx=5,pady=(10,5))
        btn5=ttk.Button(buttomFrameL,text='按他按他')
        btn5.bind('<Button>',self.click)
        btn5.pack(side='top',ipady=10,padx=5,pady=5)
        btn6=ttk.Button(buttomFrameL,text='摸摸他樓上')
        btn6.bind('<Button>',self.click)
        btn6.bind('<ButtonRelease>',self.release)
        btn6.pack(side='top',ipady=10,padx=5,pady=(5,10))
        buttomFrameL.pack(side='left',expand=True,fill='y',padx=10)
        #===================End BOTTOM FRAME LEFT===============================================================#
        #===================BOTTOM FRAME CENTER===============================================================#
        buttomFrameC=ttk.Frame(self,borderwidth=1,relief='groove')
        btn7=ttk.Button(buttomFrameC,text='button7')
        btn7.pack(side='top',ipady=22,padx=(5,8),pady=(5,10))
        btn8=ttk.Button(buttomFrameC,text='button8')
        btn8.pack(side='top',ipady=5,padx=(5,8),pady=5)
        btn9=ttk.Button(buttomFrameC,text='button9')
        btn9.pack(side='top',ipady=25,padx=(5,8),pady=5)
        buttomFrameC.pack(side='left',expand=True,fill='y',padx=10)
        #===================End BOTTOM FRAME CENTER===============================================================#
        #===================BOTTOM FRAME RIGHT===============================================================#
        buttomFrameR=ttk.Frame(self,borderwidth=1,relief='groove')
        btn10=ttk.Button(buttomFrameR,text='button9')
        btn10.pack(side='top',ipady=15,padx=5,pady=(0,10))
        btn11=ttk.Button(buttomFrameR,text='button10')
        btn11.pack(side='top',ipady=15,padx=5,pady=10)
        btn12=ttk.Button(buttomFrameR,text='button11')
        btn12.pack(side='top',ipady=15,padx=5,pady=10)
        buttomFrameR.pack(side='left',expand=True,fill='y',padx=10)
        #===================End BOTTOM FRAME Right===============================================================#
        buttomFrame.pack(expand=True,fill='x')
        #===================End BOTTOM FRAME===============================================================#
    def yeah(self):#define an instance method to bind
        self.btn1.configure(text='被按了>////<')
        print("Yaeh!")
    def meow(self):
        self.btn2.configure(text='我好喵喔')
        print("Meow~")
    def hello(self):
        self.btn3.configure(text='天線寶寶說:')
        print("尼豪")
    def click(self,event):
        #Always set to the widget that caused the event. 
        print(event.widget.configure(text="被按了")) 
    def release(self,event):
        #Always set to the widget that caused the event. 
        print(event.widget.configure(text="再按一次啦")) 

def main():
    root=Window(theme='breeze')
    root.mainloop()

if __name__=='__main__':
    main()