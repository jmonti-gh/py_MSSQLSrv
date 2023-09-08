import pyodbc
import pandas as pd

## Do not display UserWarnings when use pd.read_sql w/pyodbc conns
import warnings
warnings.filterwarnings('ignore')
# pandas only supports SQLAlchemy conns or DB string URI or DBAPI2

## Connection String Values:
driver = '{ODBC Driver 17 for SQL Server}'
srv = '(local)'
dbname = 'BikeStores'
usr = 'user1'      # SQL Server Authentication 
passwd = 'pass1'

conn_str = f'DRIVER={driver};SERVER={srv};\
    DATABASE={dbname};UID={usr};PWD={passwd}'

# Establish the connection and create cursor
try:
    cnx = pyodbc.connect(conn_str)
    cur = cnx.cursor()
except Exception as e:
    print(f'ERROR: {e}')
else:
    print(f'SUCCESS: Connection Established')

# Query to show all tables of 'dbname' database
q_1 = ''' SELECT *
        FROM INFORMATION_SCHEMA.TABLES;'''

df = pd.read_sql(q_1, cnx)
print(df)

## Show only tables of first schema listed
print(df['TABLE_SCHEMA'][0])
# print(df.loc[0, 'TABLE_SCHEMA'])
# print(df.iloc[0, 1])
print(df.index[0])
print(df.loc[df.index[0], 'TABLE_SCHEMA'])
cols_to_show = ['TABLE_CATALOG', 'TABLE_SCHEMA', 'TABLE_NAME']
#print(df[cols_to_show].loc[df.TABLE_SCHEMA == df.TABLE_SCHEMA[0]])
print(df[cols_to_show].query(f"TABLE_SCHEMA == '{df.TABLE_SCHEMA[0]}'"))

# q_2 = ''' SELECT @@SERVERNAME'''
# cur.execute(q_1)
# rows = cur.fetchall()
# print(cur.description, type(cur.description))
# for d in cur.description:
#     print(d)

# for row in rows:
#     print(row)



