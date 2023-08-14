# InstallSQLSrv
Install, and make operative MS SQL Server 2019 development edition

## Install MS SQL Server 2019 development edition
- https://dba.stackexchange.com/questions/322065/how-do-i-download-sql-server-2019-developer-edition
- Change Instance Properties -> Security -> Server authentication to SQL Server and Windows Authentication mode (in order to create and use new SQL Server logins)

## Install SQL Srv Management Studio (SSMS)
- https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16
- This installs ODBC Driver 17 for SQL Server

## Download DBs Samples: BikeStores, AdventureWorks
#### BikeStores
- https://www.sqlservertutorial.net/sql-server-sample-database/
- Build operational BikeStores DB running sql scripts.
#### AdventureWorks
- https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms
- Restore AdventureWorks2019 DB using:
	- Copy AdventureWorks2019.bak to C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\Backup
	- Databases -> Restore Database -> Device -> [File] Add -> OK -> OK
	
## Install Python SQL Driver pyodbc (a Python module)
- https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-ver16
- pip install pyodbc