from ttkthemes import ThemedTk #現成的css
from tkinter import ttk 

class Window(ThemedTk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title()
        self.title("有夠可愛")
        style=ttk.Style(self)
        topFrame=ttk.Frame(self,width=300,height=100,borderwidth=1,relief='groove')
        btn1=ttk.Button(topFrame,text='CLICK ME!')#在topFrame放進btn1，原本設定的frame寬高就沒了
        btn1.pack(side='left',expand=True)#從左向右排
        btn2=ttk.Button(topFrame,text='CLICK ME twice!')
        btn2.pack(side='left',expand=True)
        btn3=ttk.Button(topFrame,text='CLICK ME triple times!')#
        btn3.pack(side='left',expand=True)
        topFrame.pack(ipadx=10,expand=True,fill='x')#空間定位下在frame pack裡面
        buttomFrame=ttk.Frame(self,width=300,height=100)
        buttomFrameL=ttk.Frame()
        buttomFrameL.pack(side='left')

        buttomFrame.pack(ipadx=10,ipady=30)

def main():
    root=Window(theme='breeze')
    root.mainloop()

if __name__=='__main__':
    main()