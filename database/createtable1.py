import psycopg2

def createTable():

      conn = psycopg2.connect(database="mydb", user="aman")
      print "Opened database successfully"

      cur = conn.cursor()
      cur.execute('''CREATE TABLE company
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
      print "Table created successfully"

      conn.commit()
      conn.close()
      
      
