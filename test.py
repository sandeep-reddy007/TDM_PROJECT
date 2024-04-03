import cx_Oracle
import pandas as pd
def db_conn():
    try:
        connection=cx_Oracle.connect('c##admin/sandeep@localhost:1521/xe')
        print("Connection is successfull")
        return connection
    except:
        print("issue with db connection and something was happend") 

db_conn()



def load_data():
    conn=db_conn()
    query='select *from emp'
    sql_data=pd.read_sql(query,con=conn)
    csv_data=sql_data.to_csv('next_data.csv')
    #print(sql_data)
    data=pd.read_csv('next_data.csv')
    print(data)

load_data()

def file_load():
    file_data=pd.read_csv('C:/Users/sandeepreddy/Documents/filter_data.csv')
    print(file_data)

file_load()






