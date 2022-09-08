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

def dash(request):
    dados_dash = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DENOM_SOCIAL, ADMIN, TAB_IV_A_VL_PL , MES_ANO FROM Fidics_F",)
    for row in cursor.fetchall():
        dados_dash.append({ "denom_social": row[0], "admin": row[1], "tab_vl_pl": row[2], "mes_ano":row[3]})
    conn.close()
    return render(request, 'dash.html', {'dados_dash':dados_dash})
