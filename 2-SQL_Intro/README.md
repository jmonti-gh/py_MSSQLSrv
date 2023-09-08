# Kaggle - Intro to SQL (with SQL Server)

## 1- pyodbc module and DBs connection

## 2- Select, From & Where
``` python:
query = ''' SELECT -cols_names sep by ,- 
			FROM -table_name-
			WHERE -conditions sep by logical operators- '''
```
- WHERE is an optional capability

## 3- Group By, Having & Count
``` python:
query = ''' SELECT -col_name1-, COUNT(-col_name-)
			FROM -table_name-
			WHERE -conditions sep by logical operators-
			GROUP BY -col_name1-
			HAVING -COUNT(-col_name-)_condition- '''
```
- WHERE and HAVING are optional capabilities
- COUNT is an aggregate function as many others like SUM, AVG
- https://learn.microsoft.com/en-us/sql/t-sql/functions/aggregate-functions-transact-sql?view=sql-server-ver16

## 4- Order By

## 5- As & With

## 6- Joining Data

SELECT -cols_names sep by ,- 