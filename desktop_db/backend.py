import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, year INTEGER, ISBN INTEGER)")
    conn.commit()
    conn.close()

def view_all():
    print("View all")
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search_entry(title="",author="",year="",ISBN=""):
    print("Search entry")
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR ISBN=?",(title,author,year,ISBN))
    rows=cur.fetchall()
    conn.close()
    return rows

def add_entry(title,author,year,ISBN):
    print("Add entry")
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,ISBN))
    conn.commit()
    conn.close()

def update_selected(title,author,year,ISBN,id):
    print("Update selected")
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, ISBN=? WHERE id=?", (title,author,year,ISBN,id))
    conn.commit()
    conn.close()

def delete_selected(id):
    print("Delete selected")
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def close():
    print("Close")

connect()
# add_entry("Witches","Terry Pratchet",1994,202202202)
# delete_selected(3)
#update_selected(title="Witches",author="Terry Pratchet",year=1995,ISBN=202202202,id=4)
#print(search_entry(author="Terry Pratchet"))
#print(view_all())
