import psycopg2

# Connect to "chinook" database:
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
# A cursor object is another way of saying a 'set' or 'list', similar to an
# 'array' in JavaScript.
# Anything that we query from the database will become part of this cursor
# object,
# and to read that data, we should iterate over the cursor using a for-loop,
# as an example.
cursor = connection.cursor()

# query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# query 2
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# query 4
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# query 5
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# option1 : fetch the results (multiple)
results = cursor.fetchall()

# option2 : fetch the results (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
# our data sits within a cursor object, similar to an array, so in order to
# retrieve each record
# individually, we need to iterate over the results using a for-loop.
for result in results:
    print(result)
