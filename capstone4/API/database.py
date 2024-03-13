import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('sql.db')
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# # Drop the GEEK table if already exists.
# # cursor_obj.execute("DROP TABLE IF EXISTS GEEK")
 
# Creating table
# table = """ CREATE TABLE Patients (
#             id  INTEGER PRIMARY KEY AUTOINCREMENT,
#             firstname VARCHAR(255) NOT NULL,
#             lastname VARCHAR(255) NOT NULL,
#             phone VARCHAR(20) NOT NULL,
#             record VARCHAR(255) NOT NULL 
#         ); """
 
# cursor_obj.execute(table)
 
# print("Table is Ready")
 
# # Close the connection
# connection_obj.close()

# Import module 
# import sqlite3 


# # # Connecting to sqlite 
# conn = sqlite3.connect('sql.db') 

# # # Creating a cursor object using the 
# # # cursor() method 
# cursor = conn.cursor() 


# # # Queries to INSERT records. 
# cursor_obj.execute('''INSERT INTO Patients VALUES (NULL, 'Patrick', 'Bartholomew', '425-555-5678','Slight Cold')''') 
data = cursor_obj.execute('''select * from Patients''') 
# for i in data:
#     print(i)

# # # Display data inserted 
# # print("Data Inserted in the table: ") 
# # data=cursor.execute('''SELECT * FROM Patients''') 
for row in data: 
	print(row) 

# # # Commit your changes in the database	 
connection_obj.commit() 

# # # Closing the connection 
connection_obj.close()
