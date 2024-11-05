from tkinter import ttk

class SitenameFrame(ttk.Frame):
    """

    """
    # class 引數 need type and default 
    def __init__(self, master=None, sitenames:list[str]=[],**kwargs):
        super().__init__(master=master, **kwargs)
        # set column width weight
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        # item=(idx,value)
        for idx,value in enumerate(sitenames):
            column=idx%2
            index=int(idx/2)
            print(idx,value)
            print(f"column={column}")
            print(f"index={index}")
            print("===========")
