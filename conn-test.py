import pypyodbc as odbc
import pandas

conn_string = ""
conn = odbc.connect(conn_string)

sql = '''
SELECT TOP 5 * FROM Album;
'''

cursor = conn.cursor()
cursor.execute(sql)
dataset = cursor.fetchall()
print(dataset)