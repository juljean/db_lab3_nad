import psycopg2
import csv
from ps import pas
import datetime

username = 'nad'
password = pas
database = 'labaratory2'
host = 'localhost'
port = '5432'

query_0 = """
DELETE FROM attacktype;
DELETE FROM attackdate;
DELETE FROM attackplace;
DELETE FROM place;
DELETE FROM country;
DELETE FROM generaltype;
"""

query_1 = '''
INSERT INTO attackdate 
(attack_id, attack_date)
VALUES (%s, %s)
'''

query_2 = '''
INSERT INTO Place 
(place_id, place_name, country_id)
VALUES (%s, %s, %s)
'''

query_3 = '''
INSERT INTO AttackPlace 
(attack_id, place_name)
VALUES (%s, (SELECT place_id FROM place right join country 
on place.country_id = country.country_id where place_name = %s and country.country_name = %s))
ON CONFLICT DO NOTHING;
'''

query_4 = '''
    INSERT INTO country 
    (country_id, country_name)
    VALUES (%s, %s)
'''

query_5 = '''
INSERT INTO generaltype 
(type_id, type_name)
VALUES (%s, %s)
'''

query_6 = '''
INSERT INTO attacktype 
(attack_id, type_name)
VALUES (%s, (select type_id from generaltype where generaltype.type_name = %s))
'''

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(con))

INPUT_CSV_FILE = 'globalterrorismdb.csv'

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute(query_0)
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            if row['city'] != "Unknown" and row['iday']!='0':
                values4 = (row['country'], row['country_txt'])
                values2 = (row['city'][0:2] + row['country'], row['city'], row['country'])
                values5 = (row['attacktype1'], row['attacktype1_txt'])
                daten = datetime.datetime(int(row['iyear']), int(row['imonth']), int(row['iday']))
                values1 = (idx, daten)
                values3 = (idx, row['city'], row['country_txt'])
                values6 = (idx, row['attacktype1_txt'])
                try:
                    cur.execute(query_4, values4)
                    try:
                        cur.execute(query_2, values2)
                        cur.execute(query_5, values5)
                        cur.execute(query_3, values3)
                        cur.execute(query_1, values1)
                        try:
                            cur.execute(query_6, values6)
                        except psycopg2.errors.UniqueViolation or psycopg2.errors.NotNullViolation:
                            pass
                    except psycopg2.errors.UniqueViolation or psycopg2.errors.NotNullViolation:
                            pass
                except psycopg2.errors.UniqueViolation or psycopg2.errors.NotNullViolation:
                    pass
                conn.commit()