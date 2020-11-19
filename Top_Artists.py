# python file used to answer Question 2 : (SQL)  Who are the top 10 artists by the number of artworks??
from SQL_Helper import *

conn = get_connection() # retrieve connection to database
c = conn.cursor()       # get the cursor to execute SQL queries

#sql query to return the top artists
sql_top_artists=(
    'SELECT '
        'artists.Name, '
        'artists.Nationality, '
        'Count(artworks.\"Artwork ID\") AS artworkCount ' #  get the amount of art acquired by MoMa
    'FROM '
        'artworks JOIN artists on artworks.\"artist ID\" = artists.\"artist ID\" '
    'GROUP BY artists.\"artist ID\"'
    'ORDER BY artworkCount DESC'
    )


c.execute(sql_top_artists)    # execute SQL query
select_return = c.fetchall()  # save all returned rows
c.close()                     # close the connection

#  generates the submission
def question_two():
    print('     Question 2 : (SQL)  Who are the top 10 artists by the number of artworks?')
    print('')
    print(' The top artists are;')
    for i in range(0, 10):
        name = get_entry(select_return, i, 0)
        art_in_moma = get_entry(select_return, i, 2)
        print('   The number',i+1,'artist is',name,'with',art_in_moma,'artworks')