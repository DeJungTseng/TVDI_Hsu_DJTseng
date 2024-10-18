import tkinter as tk
from tkinter import ttk #themed tk module，類似CSS

class Window(tk.Tk):#Window繼承於tk模組中的Tk類別
    def __init__(self,**kwargs):
        super().__init__(**kwargs)#繼承為呼叫父類別所以不用self
        self.title()
        self.geometry('300x500')#self.attribute=內容
        self.title("有夠可愛")
        style=ttk.Style(self)#ttk module的Style class傳出實體，指派給style變數
        '''
        style.configure('TLabel',font=('Arial',11))#設定style要改變的標的物，設定內容
        #background是背景色，foreground為字的顏色
        style.configure('Title.TLabel',font=('Arial',30),background='Yellow',foreground='Green')#自訂格式("自訂格式名稱",自訂格式)
        message=ttk.Label(self,text="Eagles are cute!",style='Title.TLabel')#style="自訂格式名稱"
        #詢問一個ttk style的winfo_class就能知道這個實體要改變style呼叫的標的物。
        #print出來的結果丟進style.configure()中作為呼叫標的物
        print(message.winfo_class())
        message.pack()
        '''
        style.configure('Main.TButton',font=('Arial',18))
        btn1=ttk.Button(self,text="Click Me!")#Button類別(父類別)
        btn1.pack(ipadx=10,ipady=10,padx=10,pady=100)#ipad=inner padding距離,pad=外面的padding

def main():
    root=Window()
    root.mainloop()

if __name__=='__main__':
    main()