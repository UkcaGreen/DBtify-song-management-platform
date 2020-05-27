import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('database/db.sql')
        print("hello")
        self.create_listener_table()
        self.create_artist_table()
        #self.create_song_table()
        #self.create_album_table()


    def __del__(self):
        self.conn.commit()
        self.conn.close()


    def create_song_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "SONGS" (
          id INTEGER PRIMARY KEY,
          title TEXT,
          is_deleted boolean,
          album_id INTEGER FOREIGNKEY REFERENCES album(id)
        );
        """
        self.conn.execute(query)    
    

    def create_album_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "ALBUMS" (
          id INTEGER PRIMARY KEY,
          title TEXT,
          genre TEXT,
          is_deleted boolean,
          artist_id INTEGER FOREIGNKEY REFERENCES artist(id)
        );
        """
        self.conn.execute(query)


    def create_listener_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "LISTENERS" (
          id INTEGER PRIMARY KEY,
          username TEXT,
          email TEXT
        );
        """
        self.conn.execute(query)


    def create_artist_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "ARTISTS" (
          id INTEGER PRIMARY KEY,
          name TEXT,
          surname TEXT
        );
        """
        self.conn.execute(query)
