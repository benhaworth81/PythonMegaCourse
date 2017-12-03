import psycopg2

conn_string="dbname='postgres' user='postgres' password='t8repeXAwe$6' host='localhost' port=5432"

def create_table():
    conn=psycopg2.connect(conn_string)
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS public.store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_row(item,quantity,price):
    conn=psycopg2.connect(conn_string)
    cur=conn.cursor()
    cur.execute("INSERT INTO public.store VALUES (%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()

def view_table():
    conn=psycopg2.connect(conn_string)
    cur=conn.cursor()
    cur.execute("SELECT * FROM public.store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete_row(item):
    conn=psycopg2.connect(conn_string)
    cur=conn.cursor()
    cur.execute("DELETE FROM public.store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update_row(quantity,price,item):
    conn=psycopg2.connect(conn_string)
    cur=conn.cursor()
    cur.execute("UPDATE public.store SET quantity=%s, price=%s WHERE item=%s", (quantity,price,item))
    conn.commit()
    conn.close()

#create_table()
#insert_row('Wine Glass',5,2)
#insert_row('Coffee Cup',10,5)
#delete_row('Wine Glass')
#update_row(3,4,'Coffee Cup')
print(view_table())
