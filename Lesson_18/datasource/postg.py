import psycopg2
from dotenv import load_dotenv
load_dotenv()
import os

def get_cites()->list[dict]:
    # manage the elements that should be closed by with ... as
    with psycopg2.connect(database=os.environ['postgres_db'],
                        user=os.environ['postgres_user'],
                        password=os.environ['postgres_password'],
                        host=os.environ['postgres_host']) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM city")
            data:list[tuple] = cursor.fetchall()

    #  make the data into list[dict] by for in  loop
    convert_data:list[dict]=[{'_id':item[0],
                                'city_name':item[1],
                                'continent':item[2],
                                'country':item[3],
                                'image':item[4]} 
                                for item in data]
    return convert_data

def is_email_duplicate(email:str) -> bool:
    with psycopg2.connect(database=os.environ['Postgres_DB'],
                      user=os.environ['Postgres_user'],
                      host=os.environ['Postgres_HOST'],
                      password=os.environ['Postgres_password']) as conn:
        with conn.cursor() as cursor:
            sql = '''
                SELECT count(*) 
                FROM  public.user
                WHERE user_email = %s;
            '''
            cursor.execute(sql,(email,))
            nums:tuple = cursor.fetchone()
            return False if nums[0]==0 else True
        
def add_user(name:str, email:str, password:str) -> bool:
    with psycopg2.connect(database=os.environ['Postgres_DB'],
                      user=os.environ['Postgres_user'],
                      host=os.environ['Postgres_HOST'],
                      password=os.environ['Postgres_password']) as conn:
        with conn.cursor() as cursor:
            sql = '''
                INSERT INTO public.USER(user_name,user_email,password)
                VALUES (%s,%s,%s); 
            '''
            try:
                cursor.execute(sql,(name,email,password))
            except Exception:
                return False
            return True
