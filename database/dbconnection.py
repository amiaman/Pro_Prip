import psycopg2

def dbConnection(dbname, uName):

   conn = psycopg2.connect(database = dbname, user = uName)

print "Database is successfully connected"
  


dbConnection("mydb", "aman")
