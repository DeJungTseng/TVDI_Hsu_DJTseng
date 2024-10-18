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
        btn2=ttk.Button(topFrame,text='CLICK ME 2!')
        btn2.pack(side='left',expand=True)
        btn3=ttk.Button(topFrame,text='CLICK ME 3!')
        btn3.pack(side='left',expand=True)
        topFrame.pack(ipadx=10,expand=True,fill='x')#空間定位下在frame pack裡面

        buttomFrame=ttk.Frame(self,width=300,height=100)

        buttomFrameL=ttk.Frame(self)
        btn4=ttk.Button(buttomFrameL,text='button4')
        btn4.pack(side='top',ipady=30)
        btn5=ttk.Button(buttomFrameL,text='button5')
        btn5.pack(side='top')
        btn6=ttk.Button(buttomFrameL,text='button6')
        btn6.pack(side='top')
        buttomFrameL.pack(side='left',expand=True,padx=10)

        buttomFrameC=ttk.Frame(self)
        btn7=ttk.Button(buttomFrameC,text='button7')
        btn7.pack(side='top',ipady=30)
        btn8=ttk.Button(buttomFrameC,text='button8')
        btn8.pack(side='top')
        btn9=ttk.Button(buttomFrameC,text='button9')
        btn9.pack(side='top',ipady=30)
        buttomFrameC.pack(side='left',expand=True,padx=10)

        buttomFrameR=ttk.Frame(self)
        btn10=ttk.Button(buttomFrameR,text='button9')
        btn10.pack(side='top',ipady=10)
        btn11=ttk.Button(buttomFrameR,text='button10')
        btn11.pack(side='top',ipady=10)
        btn12=ttk.Button(buttomFrameR,text='button11')
        btn12.pack(side='top',ipady=10)
        buttomFrameR.pack(side='left',expand=True,padx=10)
        buttomFrame.pack(expand=True)

def main():
    root=Window(theme='breeze')
    root.mainloop()

if __name__=='__main__':
    main()