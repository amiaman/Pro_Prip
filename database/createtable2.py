import psycopg2

def createTable(createTableQuery):

      conn = psycopg2.connect(database="mydb", user="aman")
      print "Opened database successfully"

      cur = conn.cursor()
      cur.execute( createTableQuery )
      print "Table created successfully"

      conn.commit()
      conn.close()
      
      
createTable("CREATE TABLE company (ID INT NOT NULL, NAME TEXT NOT NULL,AGE INT NOT NULL,ADDRESS CHAR NOT NULL,SALARY REAL NOT NULL);")
