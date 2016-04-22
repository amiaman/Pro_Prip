import psycopg2

def update(updateQuery):

   conn = psycopg2.connect(database="mydb", user="aman")
   print "Opened database successfully."
   cur = conn.cursor()

   cur.execute(updateQuery)
   conn.commit
   print "Operation done successfully"

   conn.close()
   
update("UPDATE company set SALARY = 25000.00 where ID=1")
