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

        ttk.Label(TopFrame,text='選擇你的唯一可愛',style='TopFrame.TLabel').pack()
        TopFrame.pack(padx=20,pady=20)
        #===End of Top Frame====

        #===Bottom Frame===
        BottomFrame=ttk.Frame(self)
        #if the selected_size must be used other than __init__, make it an attribute
        self.selected_size = tk.StringVar()
        sizes = (('Small', 'S'),
                ('Medium', 'M'),
                ('Large', 'L'),
                ('Extra Large', 'XL'),
                ('Extra Extra Large', 'XXL'))
        label = ttk.Label(BottomFrame,text="What's your t-shirt size?")
        label.pack(fill='x', padx=5, pady=5)
        #run for 5 times, get the value in the index of tuple of 'size'
        for size in sizes:
            r = ttk.Radiobutton(
                BottomFrame,
                text=size[0],
                value=size[1],
                variable=self.selected_size
                )
            r.pack(fill='x', padx=5, pady=5)
        #Button
        button = ttk.Button(
            BottomFrame,
            text="Get Selected Size",
            command=self.show_selected_size)

        button.pack(fill='x', padx=5, pady=5)
        BottomFrame.pack(expand=True,fill='x',ipadx=10,ipady=10,padx=20,pady=(0,20))
        #===End of Bottom Frame===

        #end laypot here

    #define instance function below
    # if click cancel, clear the content
    def show_selected_size(self):
        showinfo(
            title='Result',
            message=self.selected_size.get()
        )

# create function of the document
def main():

    window=Window(theme='arc')

    window.mainloop()
if __name__=='__main__':
    main()
