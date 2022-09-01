import psycopg2


conn = psycopg2.connect(host='localhost',
                       dbname='postgres',
                       user='postgres',
                       password='Alpha140ErC',
                       port='5432')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS restaurant(francnise text, name text, city text, address text, phone text)")

with open('restaurants.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'postgres', sep=',')
    conn.commit()
    conn.close()

f.close()
