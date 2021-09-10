import pyodbc
import pandas as pd
import json
import os

def read_config(config_file):
    with open(config_file, "r") as json_file:
        configs = json.load(json_file)
    return configs
    

def db_connection(server, database, user, password):
    connectionstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ server +';DATABASE='+database+';UID='+user+';PWD=' + password
    try:
        conn = pyodbc.connect(connectionstr)
        connected = True
    except:
        connected = False
    return connected, conn

def generate_xls():
    pass

def run():
    conf = read_config('config.json')
    
    conn = db_connection(database=conf['database'], server=conf['server'], user=conf['user'], password=os.environ['myAccessToken'])
    print(conn[0])
    if (conn[0]):
        
        fechaini = input('Escriba la fecha de inicio en formato AAAAMMDD ')
        fechafin = input('Escriba la fecha final en formato AAAAMMDD ')
        filepath = f'c:\output\POS_AMPLIFY_AM60791_{fechaini}_{fechafin}.xlsx'

        df = pd.read_sql(f'EXEC hpsalesreport {fechaini}, {fechafin}', conn[1])
        df.to_excel(filepath, sheet_name='sales', index = False, header = True)

        print('Reporte generado: ' + filepath)
    else:
        print('Error de conexión')


if __name__=='__main__':
    run()
