import psycopg2 as pg

post = { "DB" : 'postgres',
  "User" : 'pybot',
  "Pass": 'pybot',
  "Host": 'localhost',
  "Port": 5432}

# Connect to an existing database
conn = pg.connect("dbname=" + post["DB"] + " user=" + post["User"] + " password=" + post["Pass"])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("drop table if exists public.test;")


# Execute a command: this creates a new table
cur.execute("CREATE TABLE public.test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO public.test (num, data) VALUES (%s, %s)",(100, "abc'def"))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM public.test;")
print cur.fetchone()
#Out: (1, 100, "abc'def")

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close() 
conn.close()

