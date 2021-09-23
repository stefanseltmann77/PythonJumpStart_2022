# %% create a small database in memory
import sqlite3
from pathlib import Path

import pandas as pd

db = sqlite3.connect(':memory:')

staff_names = ('Pavlov', 'Skinner', 'Watson',
               'Zimbardo', 'Maslow', 'Adler',
               'Tajfel')

# %% setting up a small database
db.execute("CREATE TABLE testtable (person_id int, lastname CHAR); ")
# inserting values hardcodes, ... that is dumb
db.execute("INSERT INTO testtable (person_id, lastname) VALUES (1, 'Pavlov') ")
db.execute("INSERT INTO testtable (person_id, lastname) VALUES (2, 'Skinner') ")

# check the results by doing a simple select
result = db.execute("SELECT * FROM testtable")  # the result is a result-cursor

data = result.fetchmany(10)  # call the actual number of rows from the cursor
data

data[0]  # show the first row

# %% Inserting rows with string concat, ... also DUMB
# DON'T DO IT LIKE THIS!!!!
try:
    db.execute("DROP TABLE staff")
except sqlite3.OperationalError:
    pass

db.execute("CREATE TABLE staff (person_id int, lastname CHAR); ")
for person_id, lastname in enumerate(staff_names):
    db.execute("INSERT INTO staff (person_id, lastname) VALUES (" + str(person_id) + ", '" + lastname + "') ")
# DON'T DO IT LIKE THIS!!!! Bad example, because it is vulnerable to formats and injections


# %% Inserting rows with string format, ... also dumb
# DON'T DO IT LIKE THIS!!!! Bad example, because it is vulnerable to formats and injections
db.execute("DROP TABLE staff")
db.execute("CREATE TABLE staff (person_id int, lastname CHAR); ")
for person_id, lastname in enumerate(staff_names):
    db.execute("INSERT INTO staff (person_id, lastname) VALUES (%d, '%s') " % (person_id, lastname))

# %% Inserting rows with new string format, ... also still dumb
db.execute("DROP TABLE IF EXISTS staff")
db.execute("CREATE TABLE staff (person_id int, lastname CHAR); ")
for person_id, lastname in enumerate(staff_names):
    db.execute("INSERT INTO staff (person_id, lastname) VALUES ({person_id}, '{lastname}') ".format(person_id=person_id,
                                                                                                    lastname=lastname))

for row in enumerate(staff_names):
    db.execute("INSERT INTO staff (person_id, lastname) VALUES ({}, '{}') ".format(*row))

db.execute("INSERT INTO staff (person_id, lastname) VALUES ({person_id}, '{lastname}') ".
           format(person_id=50, lastname="O'Reilly"))  # ERROR

db.execute("INSERT INTO staff (person_id, lastname) VALUES ({person_id}, '{lastname}') ".
           format(person_id=50, lastname="O'Reilly".replace("'", "''")))
# DON'T DO IT LIKE THIS!!!! Bad example, because it is vulnerable to formats and injections


# %% The only correct way: using parameters
db.execute("INSERT INTO staff (person_id, lastname) VALUES (?, ?)", (51, "Mc'Donald"))
# show which kind of params to use
sqlite3.paramstyle  # qmark
print(sqlite3.apilevel)

# %% query the data
result = db.execute("SELECT * FROM  staff ")
result.fetchone()  # best for performance
result.fetchmany()
result.fetchall()

# %% do fancy tricks with tuple format
result = db.execute("SELECT * FROM staff WHERE person_id in {}".format((1, 3, 4)))
for row in result:
    print(row)
db.rollback()

# %% also possible: use alchemy and
from sqlalchemy import create_engine
import logging

logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
engine = create_engine('sqlite:///:memory:', echo=True, encoding="UTF-8")
conn = engine.connect()

# %% Data load in pandas
PATH_DATA = Path("./data")
FILENAME = Path("recipeData.csv")
FILEPATH = PATH_DATA / FILENAME
df = pd.read_csv(FILEPATH, encoding="ansi")
df.to_sql("beer_data", conn)

# %% read load in pandas
# use an existing connection and set it as the second parameter of one of these
# pandas functions.
df_from_db = pd.read_sql_table("beer_data", conn)
df_from_db = pd.read_sql("select * From beer_data ", conn)

# you can also use the old way and do it by hand
import pandas as pd

result = conn.connection.execute("""
    Select Style, count(*) 
    From beer_data group by Style """)
result = result.fetchall()  # get all rows
# cast the rows to a dataframe
df = pd.DataFrame(result, columns=["Style", "count"])
