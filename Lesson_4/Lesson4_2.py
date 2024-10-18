import tkinter as tk
def main():
    root=tk.Tk()#建立tk套件中Tk class的實體root
    #root為視窗容器
    root.title("喵咪喵咪喵咪")
    root.geometry('400x333')#內容為字串，並且用小寫x代表乘法
    message=tk.Label(root,text="我是超可愛鷹鷹")#傳出class Label的實體，需要接收
    message.pack()#將message pack到root視窗中
    root.mainloop()#執行時主程式循環。放在最後

if __name__=='__main__':
       main() 

