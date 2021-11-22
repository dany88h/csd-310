config={
"database":"pysports",
"raise_on_warnings": True
}

import mysql.connector
from mysql.connector import errorcode

try:
    db =mysql.connector.connect(**config)
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
    