import sqlite3

class TourDB:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.db_name = "tour.db"
    def open(self):
        self.conn = sqlite3.connect("tour.db")
        self.cursor = self.conn.cursor()


    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_all_places(self):
        self.open()
        self.cursor.execute("SELECT * FROM places")
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def get_place(self, id):
        self.open()
        self.cursor.execute("SELECT * FROM places WHERE id == (?)", [id])
        data = self.cursor.fetchone()
        self.close()
        return data
    def get_all_comments(self):
        self.open()
        self.cursor.execute("SELECT * FROM comments")
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def get_comment(self, id):
        self.open()
        self.cursor.execute("SELECT * FROM comment WHERE id == (?)", [id])
        data = self.cursor.fetchone()
        self.close()
        return data
    def add_place(self,*data):
        self.open()
        self.cursor.execute('''INSERT INTO places(name,price,desc,address,image)
        VALUES((?),(?),(?),(?),(?))''',[*data])
        self.conn.commit()
        self.close()
    def add_comment(self,*data):
        self.open()
        self.cursor.execute('''INSERT INTO comments(name,comment)
        VALUES((?),(?))''',[*data])
        self.conn.commit()
        self.close()