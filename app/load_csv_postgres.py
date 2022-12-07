import psycopg2


def load_csv():
    conn = psycopg2.connect(
        database="postgres",
        user='postgres',
        password='postgres',
        host='10.5.0.6',
        port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS {};".format('prices'))
    conn.commit()
    sql1 = '''CREATE TABLE IF NOT EXISTS prices(price_date timestamp,price_bitcoin numeric)'''
    cursor.execute(sql1)
    conn.commit()

    """sql2 = '''COPY prices(price_date,price_bitcoin)
        FROM 
        DELIMITER ','
        CSV HEADER'''

    cursor.execute(sql2)"""

    with open('/app/app/prices_test.csv', 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f)  # Skip the header row.
        cursor.copy_from(f, 'prices', sep=',')
        conn.commit()

        sql3 = '''select * from prices;'''
        cursor.execute(sql3)
        for i in cursor.fetchall():
            print(i)
        conn.commit()
        conn.close()
