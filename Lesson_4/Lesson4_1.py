import requests
from requests import Response #Import Class=Response，讓response實體建立在response class下



def main():
    url='https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=5481753E-52AF-40DA-9A8A-9E192B245E13'
    

    try:#避免執行錯誤時程式閃退
        res:Response=requests.request('GET',url)
        res.raise_for_status()#用raise_for_status()方法知道res物件的status是如何
        res.encoding='UTF-8'
        content:str=res.text 
        with open('a1.csv','w',newline='',encoding='UTF-8') as file: 
            file.write(content)
    #若try模塊出現執行錯誤時，不會閃退，會執行exception
    except Exception as e:
        print(e)
    #若try模塊成功，執行else
    else:
        print("下載，存檔成功")
    
if __name__=='__main__':
    main()