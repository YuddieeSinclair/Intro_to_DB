import mysql.connector


my_db = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "@Eminemshady16",
    auth_plugin = "mysql_native_password", 
    database = "test"
)

# if my_db.is_connected():
#     print("success!")
# else:
#     print("fail")

my_cursor = my_db.cursor()

library =  """
CREATE TABLE IF NOT EXISTS library(
id INT PRIMARY KEY AUTO_INCREMENT,
genre VARCHAR(50) UNIQUE,
authors VARCHAR(50)
)
"""

my_cursor.execute(library)