# python file used to answer question 4: (Python, R or SQL) Did any artists have artwork acquired during their lifetime?
from SQL_Helper import *

conn = get_connection()  # retrieve connection to database
c = conn.cursor()        # get the cursor to execute SQL queries

# sql select statement to retrieve artwork acquired whilst the artist was still alive
sql_table_with_acquired_artwork = (
    'SELECT '
        'COUNT(*) as acquired_artwork,'  # get the amount of artwork acquired (no use for assignment but useful 
        # information) 
        'artists.Name, '
        'substr(artworks."Acquisition Date",1,4) as acquisition_year, '  # selects only the year from acquisition date
        'artists."Birth Year", '
        'artists."Death Year" '
        'FROM '
        'artworks LEFT JOIN artists on artworks."artist ID" = artists."artist ID" '  # join artist table to artworks 
    'WHERE (artists."Death Year" is not null AND '  # select entries where death year is not null and the acquisition 
        # was made before the artists death 
        'acquisition_year < artists."Death Year" AND '
        'artworks."Acquisition Date" is not null) OR  '
        '(artists."Birth Year" > 1942 AND '  # select entries where the artist is born after 1945 and does no have a 
        # "death Date" 
        'artists."Death Year" is null) '
    'GROUP BY artists."artist ID"'  # group by artist since we are only interested in them
)

# get the number of rows returned by sql_table_with_acquired_artwork
sql_table_count_of_aquired_artwork = (
        'SELECT '
        'COUNT(*) '
        'FROM '
        '(' + sql_table_with_acquired_artwork + ')'
)

c.execute(sql_table_count_of_aquired_artwork)  # execute the SQL query
result_table = c.fetchall()                    # fetch all results
c.close()                                      # close connection


# function to print results (called by main)
def question_four():
    print('     Question 4: (Python, R or SQL) Did any artists have artwork acquired during their lifetime?')
    print('')
    print(get_entry(result_table, 0, 0),
          'artists had their artwork acquired during their lifetime. Two assumptions where\n'
          'made, since we do have access to the exact day of death of artists it is assumed they dies on the first of\n'
          'January. The second assumption is for artist who have no death date however are born fairly recently, since\n'
          'the average life expectancy is 78 years, it is assumed that any artist born after 1942 and do not have a \n'
          'death year, are still alive today.')
