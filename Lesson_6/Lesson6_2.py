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
        # BIND the selected_site attribute as an input of the combobox
        # cb input the textvariable and store the value in the att self.selected_site
        sitenames_cb.configure(values=sitenames,textvariable=self.selected_site,state='readonly')
        self.selected_site.set("請選擇站點")
        # make the sitenames_cb to pack to the left and anchor on the top
        sitenames_cb.bind('<<ComboboxSelected>>', self.sitename_selected)
        sitenames_cb.pack(side='left',expand=True,anchor='n')

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

        self.tree.insert("","end",values=("2024-10-28 13:00","屏東縣","17","10","良好",120.651472,22.260899))
        # create data
        # contacts = []
        # for n in range(1, 100):
        #     contacts.append((f'date {n}', f'count {n}', f'{n}@example.com',f'',f'',f''))

        # # add data to the treeview
        # for contact in contacts:
        #     tree.insert('', tk.END, values=contact)
        self.tree.pack(side='right')
        # ===end treeview



        BottomFrame.pack(padx=20,pady=20)


        #===end botton frame===
        #====end laypot here

    #define instance function below
    def sitename_selected(self,event):
        # get textvariable in the configure "self.selected_site" as a StringVar
        
        selected=self.selected_site.get()
        selected_data=datasource.get_selected_data(selected)
        for record in selected_data:
            self.tree.insert("","end",values=record)

# ===end of Window===


def main():

    window=Window(theme="breeze")
    window.mainloop()
    
if __name__=='__main__':
    main()

#====put the sitenames into window ===????


