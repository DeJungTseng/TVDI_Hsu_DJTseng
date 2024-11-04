# define a module to define function()
# the main function would call this module and function
import requests
import sqlite3
# def funcName()->傳出資料類型
def get_sitenames(county:str)->list[str]:
    '''
    parameter:
        county:縣市名稱
    output:
        sitenames:縣市的所有測站名稱
    '''
    conn = sqlite3.connect("aqi.db")

    with conn:
        cursor=conn.cursor()
        sql='''
            SELECT DISTINCT sitename
            FROM records 
            WHERE county=?
            '''
        cursor.execute(sql,(county,))
        sitenames=[items[0] for items in cursor.fetchall() ]
        return sitenames
    
def get_selected_data(selected:str)->list[list]:
    '''
    使用者選擇了sitename，將sitename傳入
    Parameters:
        sitename:站點的名稱
    Return:
        關於站點的所有資料
    '''
    conn = sqlite3.connect("aqi.db")
    with conn:
        cursor=conn.cursor()
        sql='''
            SELECT date,county,aqi,pm25,status,lat,lon 
            FROM records 
            WHERE sitename=?
            ORDER BY date DESC ;
            '''
        cursor.execute(sql,(selected,))
        sitename_list=[list(items) for items in cursor.fetchall()]
        return sitename_list

def download_data():
    conn = sqlite3.connect("aqi.db")
    url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(e)
    else:
        sitenames = set()
        with conn:
            cursor = conn.cursor()
            for items in data['records']:
                sitenames = items['sitename']
                county = items['county']
                aqi = int(items['aqi']) if items['aqi'] != '' else 0
                status = items['status']
                pm25 = float(items['pm2.5']) if items['pm2.5'] != '' else 0.0
                date = items['datacreationdate']
                lon = float(items['longitude']) if items['longitude'] != '' else 0.0
                lat = float(items['latitude']) if items['latitude'] != '' else 0.0
                sql = '''INSERT OR IGNORE INTO records(sitename,county,aqi,status,pm25,date,lat,lon)
                        values (?,?, ?, ?,?,?,?,?);
                    '''
                cursor.execute(sql,(sitenames, county, aqi, status,pm25,date,lat,lon))

def get_county()->list[str]:
    conn = sqlite3.connect("aqi.db")

    with conn:
        cursor=conn.cursor()
        sql='''
            SELECT DISTINCT county
            from records
            '''
        cursor.execute(sql)
        counties=[items[0] for items in cursor.fetchall() ]
        return counties

def get_selected_county(selected:str)->list[list]:
    '''
    使用者選擇了county，將county傳入
    Parameters:
        county:站點的名稱
    Return:
        關於鄉鎮的所有資料
    '''
    conn = sqlite3.connect("aqi.db")
    with conn:
        cursor=conn.cursor()
        sql='''
            SELECT date,aqi,pm25,status,lat,lon 
            FROM records 
            WHERE sitename=?
            ORDER BY date DESC ;
            '''
        cursor.execute(sql,(selected,))
        county_list=[list(items) for items in cursor.fetchall()]
        return county_list