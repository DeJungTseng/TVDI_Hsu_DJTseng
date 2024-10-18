

import tkinter as tk
#先設定window class的內容
class Window(tk.Tk):#class 初始化時就設定實體視窗的特性。
      def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.title("喵咪喵咪喵咪")
            self.geometry('400x333')
            message=tk.Label(self,text="我是超可愛鷹鷹")
            message.pack()
#再設定主程式如何執行視窗
def main():
    root=Window()
    root.mainloop()

if __name__=='__main__':
       main() 

