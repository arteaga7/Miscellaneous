'''This script connects to a PostgreSQL database, make a query by using a python variable,
retrieves data from a table, and appends new data to it.

To create the table, you can use the following SQL command:
CREATE TABLE table_1 (
    column1 INTEGER,
    column2 INTEGER
);
'''

#!/usr/bin/python
#!pip install SQLAlchemy, psycopg2

# Import libraries
import pandas as pd
from sqlalchemy import create_engine

# Define the parameters to connect to the database
db_config = {'user': 'tony',            # username
             'pwd': '1234',             # password
             'host': 'localhost',       # server address
             'port': 5432,              # connection port
             'db': 'db_1'}              # database name

# Create database connection string .
connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_config['user'],
                                                         db_config['pwd'],
                                                         db_config['host'],
                                                         db_config['port'],
                                                         db_config['db'])
# Connect to the database.
engine = create_engine(connection_string)

# Create a SQL query
value = 1
query = ''' SELECT *
            FROM table_1
            WHERE column1 = '{}'
        '''.format(value)

# Obtain data from query and store it in a DataFrame
df = pd.io.sql.read_sql(query, engine)

# Show the first rows of the DataFrame
print(df.head())

# Create DataFrame form dictionary
df2 = pd.DataFrame(
    {
        'column1': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'column2': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    })

print('New data')
print(df2)

# Append new data to the table
# if_exists={'append', 'replace', 'fail'}.
# Use 'fail' to raise an error if the table exists. if it does not exist, it will be created
df2.to_sql(name='table_1', con=engine, if_exists='append', index=False)
