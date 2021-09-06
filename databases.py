"""
FOLLOWING THIS TUTORIAL:
https://www.tutorialspoint.com/python3/python_database_access.htm

MySQL Workbench

db = pymysql.connect("localhost","root","lost4815162342","testdb")
"""

#!/usr/bin/python3
import pymysql
db = pymysql.connect("localhost","root","lost4815162342","testdb")
cursor = db.cursor()

# Database Connection: FUNCIONA
"""
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)
"""

# Creating Database Table: FUNCIONA
'''
cursor.execute("DROP TABLE IF EXISTS EJEMPLO")
sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   SEX CHAR(1),
   INCOME FLOAT )"""
cursor.execute(sql)
'''

# CLOSE
db.close()