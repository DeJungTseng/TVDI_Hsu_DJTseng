from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo

# define a class Window inherited from Themedtk
class Window(ThemedTk):
    #initialize this class
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #start laypot from here!
        self.title('Marry Me!')
        #===Style===
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Arial',20))
        #===End of Style===

        #==Top Frame=====
        topFrame = ttk.Frame(self)
        ttk.Label(topFrame,text='Marry me!',style='TopFrame.TLabel').pack()
        topFrame.pack(padx=20,pady=20)
        #==End top Frame====

        #=====Button Frame=====
        BottonFrame=ttk.Frame(self)
        #===Checkbox=====
        self.agreement = tk.StringVar()
        ttk.Checkbutton(
                BottonFrame,
                text='Yes',
                command=self.agreement_changed,
                variable=self.agreement,
                onvalue='Yes',
                offvalue='No').pack()
        #===End of Checkbox===

        
        BottonFrame.pack(expand=True,fill='x',padx=20,pady=(0,20),ipadx=10,ipady=10)

        #====End of Button Frame====
        #end laypot here

    #define instance function below
    def agreement_changed(self):
        message=self.agreement.get()
        showinfo(title="Proposal Result",message=f"He said{message}")


# create function of the document
def main():
    # create an instance in class Window, named "window"
    #give a theme style to this window
    window=Window(theme="breeze")
    window.mainloop()
if __name__=='__main__':
    main()
