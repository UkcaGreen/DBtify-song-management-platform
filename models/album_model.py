import sqlite3

class AlbumModel:
    TABLENAME = "album"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create(self, title, genre):
        
        query = f"""
        INSERT INTO {TABLENAME} 
        (title, genre) 
        VALUES ("{title}","{genre}")
        """
        
        result = self.conn.execute(query)
        return result