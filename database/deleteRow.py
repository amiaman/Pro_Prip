import psycopg2

def deleteRow(deleteQuery):

   conn = psycopg2.connect(database="mydb", user="aman")
   print "Opened database successfully."
   cur = conn.cursor()

   cur.execute(deleteQuery)
   conn.commit
   print "Operation done successfully"

   conn.close()
   
deleteRow("DELETE from company where ID=2;")
