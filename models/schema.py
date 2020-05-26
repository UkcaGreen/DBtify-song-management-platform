import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create_song_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "song" (
          id INTEGER PRIMARY KEY,
          title TEXT,
          is_deleted boolean,
          album_id INTEGER FOREIGNKEY REFERENCES album(id)
        );
        """

        self.conn.execute(query)    
    

    def create_album_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "album" (
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
        CREATE TABLE IF NOT EXISTS "listener" (
          username TEXT,
          email TEXT,
        );
        """

        self.conn.execute(query)


    def create_listener_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "artist" (
          name TEXT,
          surname TEXT,
        );
        """

        self.conn.execute(query)
