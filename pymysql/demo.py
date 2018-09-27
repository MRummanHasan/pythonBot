import pymysql

conn = pymysql.connect(host='localhost', user='root', password='', db='doctor')

a = conn.cursor()

sql = 'SELECT * FROM `timings`;'
a.execute(sql)

countrow = a.execute(sql)
print("Number of rows: ", countrow)
data = a.fetchall()

print(data)
