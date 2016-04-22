import psycopg2


def writeDBquery(query):
     conn = psycopg2.connect(database="mydb", user="aman")
     print "Opened database successfully."

     cur = conn.cursor()

     cur.execute(query);
      
      
     conn.commit()
     print "Records created successfully.";
     conn.close()
     
