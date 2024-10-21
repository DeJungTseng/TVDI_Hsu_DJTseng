from  tkinter import ttk
from ttkthemes import ThemedTk

# define a class Window inherited from Themedtk
class Window(ThemedTk):
    #initialize this class
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #start laypot from here!
        #end laypot here

    #define instance function below
    def instancefunction():
        pass

# create function of the document
def main():
    # create an instance in class Window, named "window"
    #give a theme style to this window
    window=Window(theme="breeze")
    window.mainloop()
if __name__=='__main__':
    main()
