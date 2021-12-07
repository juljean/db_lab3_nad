import csv
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
with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])