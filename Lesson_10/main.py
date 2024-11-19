import datasource

from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo
import view
from view import MyCustomDialog



class Window(ThemedTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('登入')
        self.resizable(False, False)
        #==============style===============
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Helvetica',20))
        #============end style===============
        
        #==============top Frame===============

        topFrame = ttk.Frame(self)
        ttk.Label(topFrame,text='空氣品質指標(AQI)(歷史資料)',style='TopFrame.TLabel').pack()
        topFrame.pack(padx=20,pady=20)
        
        #==============end topFrame===============

        #==============bottomFrame===============
        bottomFrame = ttk.Frame(self,padding=[10,10,10,10])
            #==============SelectedFrame===============        
        self.selectedFrame= ttk.Frame(self,padding=[10,10,10,10])
        # adding refresh button

        # place the code of imagebutton in package and imported by view , class ImageButton
        icon_button=view.ImageButton(self.selectedFrame,
                                     # create an anonymus function()
                                     # function() do not need self
                              command=lambda:datasource.download_data()
                              )
        icon_button.pack()
        #combobox選擇城市      
        counties = datasource.get_county()
        #self.selected_site = tk.StringVar()
        self.selected_county = tk.StringVar()
        sitenames_cb = ttk.Combobox(self.selectedFrame, textvariable=self.selected_county,values=counties,state='readonly')
        self.selected_county.set('請選擇城市')
        sitenames_cb.bind('<<ComboboxSelected>>', self.county_selected)
        sitenames_cb.pack(anchor='n',pady=10)

        self.sitenameFrame = None 
        
        



        self.selectedFrame.pack(side='left',fill='y')
            #==============End SelectedFrame=============== 
    
            # ======Right Frame========================
        rightFrame = ttk.Labelframe(bottomFrame, text="站點資訊",padding=[10,10,10,10])
                # =====Treeview =====
                #define columns
        columns = ('date', 'county','sitename', 'aqi', 'pm25','status','lat','lon')

        self.tree = ttk.Treeview(rightFrame, columns=columns, show='headings')
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        # define headings
        self.tree.heading('date', text='日期')
        self.tree.heading('county', text='縣市')
        self.tree.heading('sitename', text='站點')
        self.tree.heading('aqi', text='AQI')
        self.tree.heading('pm25', text='PM25')
        self.tree.heading('status',text='狀態')
        self.tree.heading('lat', text='緯度')
        self.tree.heading('lon', text='經度')

        self.tree.column('date', width=150,anchor="center")
        self.tree.column('county', width=80,anchor="center")
        self.tree.column('sitename', width=80,anchor="center")
        self.tree.column('aqi', width=50,anchor="center")
        self.tree.column('pm25', width=50,anchor="center")
        self.tree.column('status', width=50,anchor="center")
        self.tree.column('lat', width=100,anchor="center")
        self.tree.column('lon', width=100,anchor="center")
        
        self.tree.pack(side='right')
        # ====End Treeview=====

        rightFrame.pack(side='right')
            # ======End of Right Frame=================


        bottomFrame.pack()

            #==============end bottomFrame===============
        
    def county_selected(self,event):
        selected = self.selected_county.get()
        sitenames = datasource.get_sitename(county=selected)
        #listbox選擇站點
        if self.sitenameFrame:
            self.sitenameFrame.destroy()
        var = tk.Variable(value=sitenames)
        self.sitenameFrame = view.SitenameFrame(master=self.selectedFrame, sitenames=sitenames) 
        # master= parent container
        # the first sitename is the argument of Class SitenameFrame, the second is the variation with value
        # define radio_control argument to be the radio_cotton_controller
        self.sitenameFrame=view.SitenameFrame(master=self.selectedFrame, sitenames=sitenames,radio_controller=self.radio_botton_clicked)
        self.sitenameFrame.pack()



    def radio_botton_clicked(self,selected_sitename:str):
        '''
        此method是傳遞給SitenameFrame實體
        當SitenameFrame中的radio_button被選取時會連動執行此method
        Parameter:
            selected_sitename:str -> 這是被選取的站點名稱
        '''
        for children in self.tree.get_children():
            self.tree.delete(children)
       
        selected_data = datasource.get_selected_data(selected_sitename)
        for record in selected_data:
            self.tree.insert("", "end", values=record)  
    
    def item_selected(self, event):
        # for treeview event binding
        for selected_item in self.tree.selection(): #選取的item
            record=self.tree.item(selected_item)
            
            # initial the Class for this .py here
            # create an instance named "dialog" in the Class of MyCustonDialog in view package
            # record['values'] is to filter the key and value of ['values'] in record
            # if the outer use '' the inner part should use "" to distinguish the different meaning of string.
            dialog = view.MyCustomDialog(parent=self, title=f'{record["values"][1]}-{record["values"][2]}',record=record['values'], )

        
 

def main():
    datasource.download_data() #下載至資料庫
    window = Window(theme="arc")
    window.mainloop()

if __name__ == '__main__':
    main()

    