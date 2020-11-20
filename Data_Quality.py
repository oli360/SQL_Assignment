# python file used to answer Question 5:  Please review the quality of the data, and present any issues
def question_five():
    print('     Question 5:  Please review the quality of the data, and present any issues')
    print('')
    print('No database is absolutely perfect, the MoMa database contains a few issues:\n'
          '1) Column names with gaps, this is very unconventional and makes the sql queries very clunky having to \n'
          'surround all column names with quotation marks.\n'
          '2) Dates, most SQL server have a special data type for dates however "SQLite does not have a storage \n'
          'class set aside for storing dates and/or times. Instead, the built-in Date And Time Functions of SQLite\n'
          'are capable of storing dates and times as TEXT, REAL, or INTEGER values."[from https://www.sqlite.org/datatype3.html]\n'
          'This means it is possible to store dates as long as they are formatted correctly (ex:YYYY-MM-DD) the MoMa \n'
          'database does this correctly in the "Acquisition Date" column of artworks table however only uses the year in \n'
          'the artists "Death Year" and "Birth Year".\n'
          '3) The column "Dimensions" in the table artworks is formatted in a multiple of different ways, sometimes containing\n'
          'letters and sometimes numbers, making it very hard to use.\n'
          '4) The column "Classification" in the table artworks contains "Mies van der Rohe Archive" and "Frank Lloyd Wright Archive"\n'
          'these could be combined into one "archives" categorie.\n'
          '5) Some artworks have multiple "artist ID" this makes joining tables very complicated, these artworks where ignored \n'
          'in this assignment, a better practise would be to duplicate them.\n'
          '6) Some artwork titles seem to be bugs or mistakes (ex:"5 x 5 = 25: Vystavka zhivopisi" (5 x 5 = 25: An Exhibition of Painting))\n'
          '7) Some artworks have a circumference but no diameter it would seem logical that artwork with a circumference have a\n'
          'diameter. It is understandable however that some pieces may have a diameter and no circumference (ex: vase or glass)\n'
          '8) Some information is missing, some artists have passed away and no death year is present in database \n'
          'ex:Poul Cadovius or Arthur Fauser'
          '9) Some artists in the artist table are not artists ex: DAS INSTITUT, DIS, "Lerival, New York" ')
