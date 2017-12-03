import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, year INTEGER, ISBN INTEGER)")
        self.conn.commit()

    def view_all(self):
        print("View all")
        self.cur.execute("SELECT * FROM book")
        self.rows=self.cur.fetchall()
        return self.rows

    def search_entry(self,title="",author="",year="",ISBN=""):
        print("Search entry")
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR ISBN=?",(title,author,year,ISBN))
        self.rows=self.cur.fetchall()
        return self.rows

    def add_entry(self,title,author,year,ISBN):
        print("Add entry")
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,ISBN))
        self.conn.commit()

    def update_selected(self,title,author,year,ISBN,id):
        print("Update selected")
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, ISBN=? WHERE id=?", (title,author,year,ISBN,id))
        self.conn.commit()

    def delete_selected(self,id):
        print("Delete selected")
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
