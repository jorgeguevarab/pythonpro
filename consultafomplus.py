import pyodbc
from datetime import date

today = date.today()

server = 'CORSA-SRV\CORSADB'
database = 'CORSA'
user = 'saint'
password = 'Clave.Saint'
connectionstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+user+';PWD=' + password

# print(connectionstr)

try:
    conn = pyodbc.connect(connectionstr)
    print('Connected successfully')
except:
    print('Unknow connection error')

cur = conn.cursor()


cur.execute("DECLARE @FECHA NVARCHAR(50); SET @FECHA = FORMAT(GETDATE(),'yyyyMMdd'); SELECT * FROM visMAEINV_Adv4(@FECHA, 0, @FECHA, @FECHA,'','',0,1);")
row = cur.fetchone()

print(list(row))

