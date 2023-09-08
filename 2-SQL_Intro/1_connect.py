import pyodbc

def try_conn(conn_str, notes):
    ''' To try different Connections Strings'''
    try:
        # Establish the connection
        print('\nUsing:', conn_str)
        connection = pyodbc.connect(conn_str)
        cursor = connection.cursor()
        print('SQL Server Connection Established -', notes)

    # Close the cursor and connection
        cursor.close()
        connection.close()
        print('--> SQL Server Connection Closed')
    
    except pyodbc.Error as e:
        print("An error occurred:", e)

## Replace these values w/your actual ones
driver = '{ODBC Driver 17 for SQL Server}'  # (1)
server = '(local)'                          # (2)
dbname = 'BikeStores'                       # (3)
# for SQL Server Authentication
user = 'user1'                              # (4)
passwd = 'pass1'                            # (5)
# for Windows Authentication
trust_conn = 'yes'

# Construct connection_string using SQL Server Auth           # (6)
conn_str_sqlauth= f'DRIVER={driver};SERVER={server};DATABASE={dbname};UID={user};PWD={passwd}'

# Conn_string for Windows Auth              # (6)
conn_str_winauth = f'DRIVER={driver};SERVER={server};DATABASE={dbname};Trusted_Connection={trust_conn}'
            
# Proofs
try_conn(conn_str_sqlauth, 'SQL Server Authentication')
try_conn(conn_str_winauth, 'Windows Authentication')

# (1) https://www.connectionstrings.com/ - 
# https://learn.microsoft.com/en-us/sql/relational-databases/security/choose-an-authentication-mode?view=sql-server-ver16

# (2) https://www.analyticsvidhya.com/blog/2021/06/how-to-access-use-sql-database-with-pyodbc-in-python/
# https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver16

# (3) dbname - 

# (4) 

# (6) # https://learn.microsoft.com/en-us/sql/tools/configuration-manager/creating-a-valid-connection-string-using-tcp-ip?view=sql-server-ver16
# https://docs.driveworkspro.com/topic/howtoconfigurewindowsfirewallforsqlserver
# https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-remote-access-server-configuration-option?view=sql-server-ver16
# https://learn.microsoft.com/en-us/sql/tools/configuration-manager/sql-server-browser-service?view=sql-server-ver16

# Using a DSN, but providing a password as well
#cnxn = pyodbc.connect('DSN=test;PWD=password')
# Data Source Name: data structure containing information about a specific
# database to which an Open Database Connectivity (ODBC) driver needs to
# connect. Also stands for Deep Space Network.
# https://learn.microsoft.com/en-us/sql/integration-services/import-export-data/connect-to-an-odbc-data-source-sql-server-import-and-export-wizard?view=sql-server-ver16

# (7) Remote connections: 1. Enable Remote in the Instance, 2. Enable ports in Firewall!
# https://learn.microsoft.com/en-us/sql/tools/configuration-manager/creating-a-valid-connection-string-using-tcp-ip?view=sql-server-ver16
# https://docs.driveworkspro.com/topic/HowToConfigureWindowsFirewallForSQLServer
# https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-remote-access-server-configuration-option?view=sql-server-ver16

# https://stackoverflow.com/questions/44520229/connection-string-to-sql-server-with-python-pypyodbc

# https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/connect/network-related-or-instance-specific-error-occurred-while-establishing-connection
# SQL Browser Running
# https://www.mssqltips.com/sqlservertip/2340/resolving-could-not-open-a-connection-to-sql-server-errors/