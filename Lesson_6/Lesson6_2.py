import datasource
# call the function of get_sitenames
# ===Class:Window=====
import tkinter as tk
from  tkinter import ttk
from ttkthemes import ThemedTk


class Window(ThemedTk):
    #initialize this class
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #===start laypot from here!
        self.title('AQI')
        # ====Style===
        # create an instance named "style" in the Style class in ttk package
        style=ttk.Style(self)
        # configure the attribute of font of the TLabel class of TopFrame
        style.configure('TopFrame.TLabel',font=('Arial',20))
        #====End of Style=====

        #=====Top Frame=====
        TopFrame=ttk.Frame(self)

        ttk.Label(TopFrame,text='AQI',style='TopFrame.TLabel').pack()
        TopFrame.pack(padx=20,pady=20)
        #===End of Top Frame====

        #===Botton Frame
        BottomFrame=ttk.Frame(self)
        sitenames=datasource.get_sitenames()

        # output data but not interface
        # if output data (regional var), delete form memory after __init__
        # packed item would exist after __init__ complete
        self.selected_site = tk.StringVar() 
        sitenames_cb = ttk.Combobox(BottomFrame)
        sitenames_cb.configure(values=sitenames,textvariable=self.selected_site,state='readonly')
        self.selected_site.set("請選擇站點")
        sitenames_cb.pack(padx=20,pady=20)
        BottomFrame.pack(padx=20,pady=20)


        #===end botton frame===
        #====end laypot here

    #define instance function below
    def instancefunction():
        pass
# ===end of Window===


def main():

    window=Window(theme="breeze")
    window.mainloop()
    
if __name__=='__main__':
    main()

#====put the sitenames into window ===????


