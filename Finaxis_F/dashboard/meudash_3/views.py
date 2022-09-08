from django.shortcuts import render
from django.apps import apps
import pyodbc

def connection():
    s = 'DESKTOP-RI0H11C\SQLEXPRESS' #Your server name 
    d = 'Finaxis_F' 
    #u = '' #Your login
    #p = '' #Your login password
    #cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+ p
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';trusted_connection=yes'
    conn = pyodbc.connect(cstr)
    return conn

def dash_3(request):
    cars = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM (TAB_IV_A_VL_PL) * 0.0000000001 AS TAB_IV_A_VL_PL,  MES_ANO FROM Fidics_F GROUP BY MES_ANO",)
    for row in cursor.fetchall():
        cars.append({ "tab_vl_pl": row[0], "mes_ano":row[1]})
    conn.close()
    return render(request, 'dash_3.html', {'cars':cars})
