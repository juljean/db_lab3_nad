import json
import psycopg2
from ps import pas

TABLES = [
    'course',
    'organization',
    'courses_organizations',
    'difficultytype',
    'ratings',
    'students',
    'certification'
]

username = 'nad'
password = pas
database = 'labaratory2'
host = 'localhost'
port = '5432'

OUTPUT_FILE_T = 'Nad_DB_{}.csv'

TABLES = [
    'attacktype',
    'attackdate',
    'attackplace',
    'place',
    'country',
    'generaltype'
]

conn = psycopg2.connect(user=username, password=password, dbname=database)
data = {}

with conn:
    cur = conn.cursor()

    for table in TABLES:
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open('all_data.json', 'w') as outf:
    json.dump(data, outf, default=str)