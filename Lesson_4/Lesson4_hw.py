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
        btn1=ttk.Button(topFrame,text='button1')#在topFrame放進btn1，原本設定的frame寬高就沒了
        btn1.pack(side='left',padx=10,expand=True)#從左向右排
        btn2=ttk.Button(topFrame,text='button2')
        btn2.pack(side='left',padx=10,expand=True)
        btn3=ttk.Button(topFrame,text='button3')
        btn3.pack(side='left',padx=10,expand=True)
        topFrame.pack(ipadx=10,expand=True,fill='x')#空間定位下在frame pack裡面
        #==================End TOP FRAME====================================================#
        #===================BOTTOM FRAME===============================================================#
        buttomFrame=ttk.Frame(self,borderwidth=1,relief='groove')
        
        #===================BOTTOM FRAME LEFT===============================================================#
        buttomFrameL=ttk.Frame(self,borderwidth=1,relief='groove')
        btn4=ttk.Button(buttomFrameL,text='button4')
        btn4.pack(side='top',ipady=30,padx=5,pady=(10,5))
        btn5=ttk.Button(buttomFrameL,text='button5')
        btn5.pack(side='top',ipady=10,padx=5,pady=5)
        btn6=ttk.Button(buttomFrameL,text='button6')
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

def main():
    root=Window(theme='breeze')
    root.mainloop()

if __name__=='__main__':
    main()