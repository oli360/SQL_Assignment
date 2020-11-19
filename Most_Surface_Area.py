# python used to answer Question 3: (SQL) Which artist is created the most artwork by total surface area?
from SQL_Helper import *

conn = get_connection()  # retrieve connection to database
c = conn.cursor()  # get the cursor to execute SQL queries

# relatively simple SQL select statement to retrieve the surface are of all rectangular objects
sql_select_only_rectangular_objects = (
    'Select artists.Name, artworks."artist ID", SUM(artworks."Height (cm)" * artworks."Width (cm)") as total_surface_area '
        'from artworks '
    'INNER JOIN artists on artworks."artist ID" = artists."artist ID" '  # join artists to get artist names
    'WHERE "Diameter (cm)" is  null '  # get only rows with "Height (cm)" and "Width (cm)"
        'AND "Height (cm)" is  not null '
        'AND "Length (cm)" is  null '
        'AND "Width (cm)" is  not null AND '
        '(Classification= "Print"  OR '  # get only rows  with the correct classification 
        'Classification= "Work on Paper" OR '
        'Classification= "Photography Research/Reference" OR '
        'Classification= "Painting" OR '
        'Classification= "Photograph" OR '
        'Classification= "Drawing") '
    'GROUP By artists.Name '
    'ORDER by total_surface_area DESC'  # get a ordered list with decreasing surface_area
)

# return table of all circular objects with surface area
sql_select_table_with_circular_objects = (
    'SELECT *, '
    'CASE'
        ' WHEN len == 0 AND circular ==1  THEN radius*radius*2*3.14159 '  # measure surface area  for 2d artwork
        ' WHEN len !=0  AND circular ==1  THEN radius*radius*2*3.14159 + 2*3.14159*radius*len ' # measure surface area for 3d artwork
        'ELSE 0 '
    'END surface_area '
    'FROM '
        '(Select ' # return table of all circular objects 
            ' "Artwork ID" as artwork_ID , "Artist ID" as artist_ID, "Diameter (cm)" as diameter, 1 as circular, '
            'CASE' # get highest value between "Height (cm)", "Length (cm)" and "Width (cm)"
                ' WHEN ifnull("Height (cm)",0) > ifnull("Length (cm)",0) AND ifnull("Height (cm)",0) >= ifnull("Width (cm)",0) THEN ifnull("Height (cm)",0) '
                ' WHEN ifnull("Length (cm)",0) > ifnull("Height (cm)",0) AND ifnull("Length (cm)",0) >= ifnull("Width (cm)",0) THEN ifnull("Length (cm)",0) '
                ' WHEN ifnull("Width (cm)",0)  > ifnull("Height (cm)",0) AND ifnull("Width (cm)",0)  >= ifnull("Length (cm)",0) THEN ifnull("Width (cm)",0) '
                'ELSE 0 '
            'END len, '
            '"Diameter (cm)"*0.5 AS radius ' # get the radius, to later use for surface area
        'FROM artworks  '
            'Where  "Diameter (cm)" is not null '
        'GROUP BY "Artwork ID") as diameter_table'
)
# return table of all rectangular objects with surface area
sql_select_table_with_rectangular_objects = (
    'Select '
        ' "Artwork ID" as artwork_ID , "Artist ID" as artist_ID,'
        'CASE' # two possible cases 1:the object is a 2d rectangle 2: the object is 3d rectangular prism
            ' WHEN ifnull("Height (cm)",0)*ifnull("Length (cm)",0)*ifnull("Width (cm)",0) > 0 THEN 2*"Height (cm)"*"Length (cm)"+2*"Width (cm)"*"Length (cm)"+2*"Height (cm)"*"Width (cm)"'
            'ELSE ifnull("Height (cm)",1)*ifnull("Length (cm)",1)*ifnull("Width (cm)",1) '
        'END surface_area '
    'FROM artworks  '
    'Where  "Diameter (cm)" is null AND ' # only get rows with null on "diameter"
        '("Height (cm)" is not null OR '
        '"Length (cm)" is not null OR '
        '"Width (cm)" is not null) '
    'GROUP BY "Artwork ID"'
)

# joins circular and rectangular table
sql_select_table_with_all_objects = (
    'Select artwork_ID, artist_ID, surface_area '
    'FROM'
        '(' + sql_select_table_with_circular_objects + ')'
    'UNION '
    'Select artwork_ID, artist_ID, surface_area '
    'FROM'
        '(' + sql_select_table_with_rectangular_objects + ')'
)

# adds artist name and sums the surface areas
sql_select_table_with_all_objects_and_artists = (
        'Select artists.Name, artists."artist ID" , SUM(surface_table.surface_area) as total_surface_area '
        'FROM '
            '(' + sql_select_table_with_all_objects + ') surface_table '
        'INNER JOIN artists on surface_table.artist_ID = artists."artist ID" '
        'GROUP BY artists.Name '
        'ORDER BY total_surface_area DESC'
)


c.execute(sql_select_only_rectangular_objects)       # executes the only 2d rectangular sql query
result_table_only_rectangular_objects = c.fetchall() # saves result

top_rectangular_name = get_entry(result_table_only_rectangular_objects, 0, 0)          # recovers name from result
top_rectangular_surface_area = get_entry(result_table_only_rectangular_objects, 0, 2)  # recovers surface area from result

c.execute(sql_select_table_with_all_objects_and_artists) # executes the all object sql query
result_table_only_all_objects_and_artists = c.fetchall() # saves result

all_objects_name = get_entry(result_table_only_all_objects_and_artists, 0, 0)           # recovers name from result
all_objects_surface_area = get_entry(result_table_only_all_objects_and_artists, 0, 2)   # recovers surface area from result

# generates output for submission
def question_three():
    print('     Question 3: (SQL) Which artist is created the most artwork by total surface area?')
    print('')
    print('Contrarily to the previous questions this  question is open to a multitude of interpretations, the surface\n'
          'area of artworks can be very complex to calculate, for example measuring the surface are of a sculpture \n'
          'can be near impossible. \n'
          '     Two answers are proposed for the question, the fist is relatively simple, we only look at 2D \n'
          'rectangular artworks.This can be done by looking at the "classification" attribute and only selecting data\n'
          'entries containing "Print", "Work on Paper", "Photography Research/Reference","Painting", "Photograph"or \n'
          '"Drawing", and only selecting the height and width values to measure the surface area. This approach \n'
          'returns', top_rectangular_name, 'as the artist with the most surface area with',
          "{:.4f}".format(top_rectangular_surface_area * 0.0001),
          'm^2 of art created.\nWhile this approach is straight forward is doesn\'t take any sculture into consideration'
          ' nor does it look at \nsimple 3D objects like plates or vases. It measures the surface area of 62 490 on 130'
          ' 000 artworks so', "{:.2f}".format(6249000 / 130000), '% \nof the artwork.\n'
          '     As mentioned previously measuring the surface are of all artworks is impossible however we can increase the\n'
          'percentage of used artworks to ',
          "{:.2f}".format(11231100 / 130000), '% by making a couple assumptions:\n'
          '-all objects with only a "diameter" attribute are circular objects\n'
          '-all objects with a "diameter" attribute and a value in "Width","Length","Height" are  cylinders\n'
          '-all objects with only two values in the "Width","Length","Height" attributes are rectangular artworks\n'
          '-all objects with three values in "Width","Length","Height" attributes are rectangular prisms\n'
          'With these assumptions we find that the artist with the most artwork by surface area is',
          all_objects_name,
          '\nwith', "{:.4f}".format(all_objects_surface_area * 0.0001), 'm^2 of art created. ')
