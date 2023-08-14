import pyodbc

#print(dir(pyodbc))

for func in dir(pyodbc):
    print(func, '\t', end='')

# pip install pyodbc
# https://pypi.org/project/pyodbc/
# https://github.com/mkleehammer/pyodbc/wiki