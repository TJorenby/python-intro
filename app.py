import psycopg2


#Connect to db
con = psycopg2.connect(
    host = "localhost",
    database="python_intro",
    user = "tylerjorenby",
    password = "postgres"
)

#cursor
cur = con.cursor()

cur.execute("insert into test (id, name) values (%s, %s)", (3, "Jared"))
#execute the query
cur.execute("select id, name from test")

rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]} name {r[1]}")

#commit changes (for Post)
con.commit() 

#close cursor
cur.close()

#close the connection
con.close()


