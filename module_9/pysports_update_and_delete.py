import mysql.connector as mysql

db = mysql.connect(
    host ="localhost",
    user = "root",
    password = "bob345345",
    database = "py_sports")


cursor = db.cursor()

query_one = "SELECT player_id, first_name, last_name, team_name FROM py_sports.player INNER JOIN team ON player.team_id = team.id_team;";

cursor.execute(query_one)

records = cursor.fetchall()

for record in records:
    print(record)