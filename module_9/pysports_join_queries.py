import mysql.connector as mysql

db = mysql.connect(
    host ="localhost",
    user = "root",
    password = "bob345345",
    database = "py_sports")


cursor = db.cursor()

query_one = "SELECT id_team, team_name, mascot FROM team";

cursor.execute(query_one)

records = cursor.fetchall()

for record in records:
    print(record)
    

c = db.cursor()

query_2 = "SELECT * FROM player"

cursor.execute(query_2)

r = cursor.fetchall()

for re in r:
    print(re)
