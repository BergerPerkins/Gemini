import sqlite3

#connect to sqllite
connection = sqlite3.connect("student.db")

#create a cursor object to record create table retrive
cursor=connection.cursor()

#create the table
table_info ="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT); 
"""

cursor.execute(table_info)

#insert some more records
cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Berger','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Anish','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Satheesh','DEVOPS','A',35)''')

#display all the records
print("The inserted records are")

data = cursor.execute('''select * from student''')

for row in data:
    print(row)

#close the connection
connection.commit()
connection.close()
