import psycopg2

def retrieveData(retrievingQuery):

    conn = psycopg2.connect(database="mydb", user="aman")
    print "Opened database successfully."


    cur = conn.cursor()

    cur.execute(retrievingQuery)
    rows = cur.fetchall()
    for row in rows:
       print row
       
    conn.commit()
    print "Operation done successfully";
    conn.close()
    
retrieveData("SELECT * from company")
