# define a module to define function()
# the main function would call this module and function
import requests
# def funcName()->傳出資料類型
def get_sitenames()->list[str]:
# raise for status to get the request status 
    url="https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON"
    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()

    # except Exception to give anothe route to get error code 
    except Exception as e:
        print(e)

    # else: excecute without error
    # main process put in else
    else:
        sitenames=set()

        for items in data['records']:
        # add sitenames  value by add function to set class 
            sitenames.add(items['sitename'])
        sitenames=list(sitenames)
        return sitenames
    
def get_selected_data(selected:str)->list[list]:
    url="https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON"
    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()

    except Exception as e:
        print(e)

    else:
        outerlist=[]
        for items in data['records']:
            if items['sitename'] == selected:
                innerlist=[items['datacreationdate'],items['county'],items['aqi'],items['pm2.5'],items['status'],items['longitude'],items['latitude']]
                outerlist.append(innerlist)

        return outerlist
