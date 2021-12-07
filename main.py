import psycopg2
import matplotlib.pyplot as plt
from ps import pas

username = 'nad'
password = pas
database = 'labaratory2'
host = 'localhost'
port = '5432'

query_1 = '''
   create view AttacksCountry as
   select TRIM(Country.country_name), count(country_name) as total from AttackDate join AttackPlace on (AttackDate.attack_id = AttackPlace.attack_id)
    join Place on (AttackPlace.place_name = Place.place_id) join Country on (Place.country_id = Country.country_id)
    group by Country.country_name;
'''

query_2 = '''
    create view TerractPart as
    select TRIM(Place.place_name) as City, count(Place.place_name) from AttackDate join AttackPlace on (AttackDate.attack_id = AttackPlace.attack_id)
    join Place on (AttackPlace.place_name = Place.place_id)
    where attack_date > '2009-09-09'
    group by place.place_name;
'''

query_3 ='''
    create view AttacksYear as
    select extract(isoyear from AttackDate.attack_date) as year, count(extract(isoyear from AttackDate.attack_date)) as total
    from AttackDate
    group by extract(isoyear from AttackDate.attack_date)
    order by year;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
with conn:

    print("Database opened successfully")

    cur1 = conn.cursor()
    cur1.execute('DROP VIEW IF EXISTS AttacksCountry')
    cur1.execute(query_1)
    cur1.execute('SELECT * FROM AttacksCountry')

    country = []
    total = []

    for row in cur1:
        country.append(row[0][0])
        total.append(row[1])

    x_range = range(len(country))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(country, total, label='Total')
    bar_ax.set_title('Залежність кількості терактів від країни')
    bar_ax.set_xlabel('Країна')
    bar_ax.set_ylabel('Кількість терактів')
    bar_ax.set_xticks(x_range)

    cur2 = conn.cursor()
    cur2.execute('DROP VIEW IF EXISTS TerractPart')
    cur2.execute(query_2)
    cur2.execute('SELECT * FROM TerractPart')
    city = []
    total = []
    for row in cur2:
        city.append(row[0])
        total.append(row[1])

    pie_ax.pie(total, labels=city, autopct='%1.1f%%')
    pie_ax.set_title('Частка терактів у заначеному місті')

    cur3 = conn.cursor()
    cur3.execute('DROP VIEW IF EXISTS AttacksYear')
    cur3.execute(query_3)
    cur3.execute('SELECT * FROM AttacksYear')
    ter_numb = []
    year = []

    for row in cur3:
        year.append(row[0])
        ter_numb.append(row[1])

    graph_ax.plot(year, ter_numb, marker='o')

    graph_ax.set_xlabel('Рік')
    graph_ax.set_ylabel('Кількість терактів')
    graph_ax.set_title('Залежність кількості терактів від року')


mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()