import sqlite3


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('database/db.sql')
        self.create_album_table()
        self.create_song_table()
        self.create_listener_table()
        self.create_artist_table()
        # self.create_song_like_table()
        # self.create_album_like_table()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create_song_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "SONGS" (
          id INTEGER PRIMARY KEY,
          title TEXT,
          album_id INTEGER FOREIGNKEY REFERENCES ALBUMS(id)
        );
        """
        self.conn.execute(query)

    def create_album_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "ALBUMS" (
          id INTEGER PRIMARY KEY,
          title TEXT,
          genre TEXT
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

    def create_song_like_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "SONGLIKES" (
          id INTEGER PRIMARY KEY,
          listener_id INTEGER FOREIGNKEY REFERENCES LISTENERS(id),
          song_id INTEGER FOREIGNKEY REFERENCES SONGS(id)
        );
        """
        self.conn.execute(query)

    def create_album_like_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "ALBUMLIKES" (
          id INTEGER PRIMARY KEY,
          listener_id INTEGER FOREIGNKEY REFERENCES LISTENERS(id),
          album_id INTEGER FOREIGNKEY REFERENCES ALBUMS(id)
        );
        """
        self.conn.execute(query)
