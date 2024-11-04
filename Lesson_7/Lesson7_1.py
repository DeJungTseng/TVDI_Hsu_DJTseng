import datasource
# call the function of get_sitenames
# ===Class:Window=====
import tkinter as tk
from  tkinter import ttk
from ttkthemes import ThemedTk
import sqlite3


class Window(ThemedTk):
    #initialize this class
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #===start laypot from here!
        self.title('AQI')
        self.resizable(False,False)
        # ====Style===

        style=ttk.Style(self)

        style.configure('TopFrame.TLabel',font=('Arial',20))
        #====End of Style=====

        #=====Top Frame=====
        TopFrame=ttk.Frame(self)

        ttk.Label(TopFrame,text='AQI',style='TopFrame.TLabel').pack()
        TopFrame.pack(padx=20,pady=20)
        #===End of Top Frame====

        #===Botton Frame===============
        BottomFrame=ttk.Frame(self)
            #===========SelectedFrame=======================
        selectedFrame=ttk.Frame(self,padding=[10,10,10,10])
        # combobox sclect county
        
        # sitenames=datasource.get_sitenames()
        
        county=datasource.get_county()
        self.selected_county = tk.StringVar() 
        counties_cb = ttk.Combobox(selectedFrame,textvariable=self.selected_county,state='readonly')

        counties_cb.configure(values=county,textvariable=self.selected_county,state='readonly')
        self.selected_county.set("請選擇城市")

        counties_cb.bind('<<ComboboxSelected>>', self.county_selected)
        counties_cb.pack(expand=True,anchor='n',pady=10)
        selectedFrame.pack(side='left',expand=True,fill='y',padx=(20,0))
            #===============End SelectedFrame================
        # ======ListBox=======
        langs = ('Java', 'C#', 'C', 'C++', 'Python',
         'Go', 'JavaScript', 'PHP', 'Swift')

        var = tk.Variable(value=langs)

        listbox = tk.Listbox(
            selectedFrame,
            listvariable=var,
            height=6,
            selectmode=tk.EXTENDED
        )

        listbox.pack(anchor='n')
        listbox.destroy()
        # ======End ListBox=====

        # ===treeview
        columns = ('date', 'county','aqi', 'pm25','status','longitude','latitude')

        self.tree = ttk.Treeview(BottomFrame, columns=columns, show='headings')
        # set the layout of self.treewiew
        self.tree.heading('date', text='日期')
        self.tree.heading('county', text='縣市')
        self.tree.heading('aqi', text='AQI')
        self.tree.heading('pm25', text='PM25')
        self.tree.heading('status', text='狀態')
        self.tree.heading('longitude', text='經度')
        self.tree.heading('latitude', text='緯度')

        self.tree.column('date', width=120,anchor='center')
        self.tree.column('county', width=80,anchor='center')
        self.tree.column('aqi', width=50,anchor='center')
        self.tree.column('pm25', width=50,anchor='center')
        self.tree.column('status', width=50,anchor='center')
        self.tree.column('longitude', width=120,anchor='center')
        self.tree.column('latitude', width=120,anchor='center')



        self.tree.pack(side='right')
        # ===end treeview



        BottomFrame.pack(padx=20,pady=20)


        #===end botton frame===
        #====end laypot here

    #define instance function below
    def county_selected(self,event):
        selected=self.selected_county.get()
        print(selected)

    def sitename_selected(self,event):
        for children in self.tree.get_children():
            self.tree.delete(children)
        
        
        selected=self.selected_county.get()
           
        selected_data = datasource.get_selected_county(selected)
        for record in selected_data:
            self.tree.insert("", "end", values=record)
# ===end of Window===



    
def main():
    datasource.download_data()
    # execute without windows and its mainloop, so it only execute once
    window=Window(theme="arc")
    window.mainloop()
    
if __name__=='__main__':
    main()

#====put the sitenames into window ===????


