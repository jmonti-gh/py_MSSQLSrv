# https://github.com/mkleehammer/pyodbc/wiki
# https://github.com/mkleehammer/pyodbc/wiki/Getting-started

import pyodbc

# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=\
                      localhost;DATABASE=BikeStores;UID=user1;PWD=pass1')
# i'm using SQL auth method

# Using a DSN, but providing a password as well
#cnxn = pyodbc.connect('DSN=test;PWD=password')
# Data Source Name: data structure containing information about a specific
# database to which an Open Database Connectivity (ODBC) driver needs to
# connect. Also stands for Deep Space Network.
# https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-an-odbc-data-source-sql-server-import-and-export-wizard?view=sql-server-ver16

# Create a cursor from the connection
cursor = cnxn.cursor()

cursor.execute("SELECT * FROM production.products")
rows = cursor.fetchall()
# for row in rows:
#     print(row)
# print(rows)

lines_quantity = 5
for i in range(lines_quantity):
    print(rows[i])



