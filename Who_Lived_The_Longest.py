# python file used to answer question 1: (SQL) Which artist in this data set lived the longest?
from SQL_Helper import *

conn = get_connection() # get connection
c = conn.cursor()       # get cursor

# SQL query to retrieve the oldest artist
sql_query=('SELECT '
            'Name, Nationality, MAX(\"Death Year\"-\"Birth Year\")' # get the age the artist died at  
          'FROM '
            'artists '
          'WHERE '
            'NOT ( \"Death Year\" is null'
            ' OR \"Birth Year\" is null)'
            ' AND \"Death Year\"-\"Birth Year\"<125 '
           'ORDER by \"Death Year\"-\"Birth Year\" DESC')


c.execute(sql_query)           # execute SQL query
select_return = c.fetchall()   # save all returned rows
c.close()                      # close the connection

# generate submission
def question_one():

    print('     Question 1: (SQL) Which artist in this data set lived the longest?')
    print('')
    answer = get_entry(select_return, 0, 0)
    age = get_entry(select_return, 0, 2)
    print(answer, 'is the artist who lived the longest, she managed to reach',age, 'years old.')

