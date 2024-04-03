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

def get_data():
    connection=db_conn()
    cursor=connection.cursor()
    sql_ferch_data='select *from emp'
    cursor.execute(sql_ferch_data)
    print(cursor)
    data=pd.DataFrame(cursor)
    writer=pd.ExcelWriter('emp_data.xlsx')
    data.to_excel('emp_data.xlsx',sheet_name='Sheet_name_1')
    print(type(data))
    print(data)
    connection.commit()
    connection.close()

get_data()