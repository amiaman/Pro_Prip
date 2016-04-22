import psycopg2

def dbConnection(dbname, uName):

   conn = psycopg2.connect(database = dbname, user = uName)

print "Opened database successfully"
  


dbConnection("mydb", "aman")
