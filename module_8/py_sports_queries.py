config={"user" : "root",
"password":"Bob345345",
"host" : "localhost",
"database":"py_ sports",
"raise_on_warnings": True
}

import mysql.connector
from mysql.connector import errorcode

try:
    db =mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n press any key to continue...")

except mysql.connector.Error as err:
    if err.errno ==errorcode.ER_ACCESS_DENIED_ERROR:
        print("     the supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" the specified database does not exist")
    else:
        print(err)

finally:
    db.close()


SELECT team_id, team_name, mascot FROM team;


cursor = db.cursor()

cursor.execute(“SELECT team_id, team_name, mascot FROM team”)

teams = cursor.fetchall()

for team in teams:
print(“Team Name: {}”.format(team[1]))

    