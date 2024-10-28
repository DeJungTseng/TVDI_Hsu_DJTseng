
from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo

class Window(ThemedTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('登入')
        #==============style===============
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Helvetica',20))
        #============end style===============
        
        #==============top Frame===============

        topFrame = ttk.Frame(self)
        ttk.Label(topFrame,text='check_box多選鈕',style='TopFrame.TLabel').pack()
        topFrame.pack(padx=20,pady=20)
        
        #==============end topFrame===============

        #==============bottomFrame===============
        bottomFrame = ttk.Frame(self)
        # calalble range of self.attribute is all part in the class.
        # if not self, restricted in __init__
        # self.aggrement is built from the StringVar() class
        self.agreement = tk.StringVar()

        # ceaate an instance of Checknotton but do not assign to a var
        ttk.Checkbutton(bottomFrame,
                text='I agree',
                # give a method()
                command=self.agreement_changed,
                variable=self.agreement,
                onvalue='agree',
                offvalue='disagree').pack()
        
        bottomFrame.pack(expand=True,fill='x',padx=20,pady=(0,20),ipadx=10,ipady=10)
        #==============end bottomFrame===============

    # instance method ,the same status of __init__
    # call this function with "self"
    def agreement_changed(self):
        showinfo(
            title='Agreement',
            message= self.agreement.get()

        )
    
        

def main():
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()
