import psycopg2


def insertData(insertQuery):
     conn = psycopg2.connect(database="mydb", user="aman")
     print "Opened database successfully."

     cur = conn.cursor()

     cur.execute(insertQuery);
      
      
     conn.commit()
     print "Records created successfully.";
     conn.close()
     
insertData("INSERT INTO company VALUES (2, 'Sateesh', 30, 'Mumbai', 53000.00 )")
