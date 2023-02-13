# For managing the database
import mysql.connector

# CREATING A CONNECTION
db = mysql.connector.connect(
    host="localhost", #can be found in mysqlworkbench, it's localhost by default
    user="root", # can be found in mysqlworkbench, it's root by default
    password="/**skandar1234**/", # your password here
    port="..." # can be found in mysqlworkbench, it's 3306 by default
)