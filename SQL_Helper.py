# python script ot help with the SQL results
import sqlite3

# location of the database
# LINE TO CHANGE
db_location = 'artists.db'  # INSERT DATABASE LOCATION

# returns a connection do the database
def get_connection():
    conn = sqlite3.connect(db_location)
    return conn

# return the specified entries from a sql query result
def get_entry(select_return, row_number, column_number):
    i = 0
    for row in select_return:
        if i == row_number:
            return row[column_number]
        i += 1
    raise Exception("Entry not found")
