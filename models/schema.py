import pymysql


class Schema:
    def __init__(self):
        self.conn = pymysql.connect("localhost", "root", "", "dbtify")
        self.cursor = self.conn.cursor()
        self.create_listener_table()
        self.create_artist_table()
        self.create_album_table()
        self.create_song_table()
        self.create_song_artist_table()
        self.create_song_like_table()
        self.create_album_like_table()
        # self.create_trigger_delete_song()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create_trigger_delete_song(self):
        query = """
        DELIMITER //
        CREATE TRIGGER delete_song BEFORE DELETE ON album_table
        FOR EACH ROW BEGIN 
          DELETE FROM song_table WHERE song_table.album_id = OLD.id; 
        END
        //
        DELIMITER ;
        """
        self.cursor.execute(query)

    def create_trigger_delete_song_artist_relation(self):
        query = """
        DELIMITER //
        CREATE TRIGGER delete_song_artist BEFORE DELETE ON song_table
        FOR EACH ROW BEGIN 
          DELETE FROM song_artist_table WHERE song_artist_table.song_id = OLD.id; 
        END
        //
        DELIMITER ;
        """
        self.cursor.execute(query)

    def create_song_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS song_table (
          id INTEGER NOT NULL AUTO_INCREMENT,
          title varchar(32),
          album_id INTEGER,
          FOREIGN KEY(album_id) REFERENCES album_table(id),
          PRIMARY KEY(id)
        );
        """
        self.cursor.execute(query)

    def create_album_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS album_table (
          id INTEGER NOT NULL AUTO_INCREMENT,
          title varchar(32),
          genre varchar(32),
          artist_id INTEGER,
          FOREIGN KEY(artist_id) REFERENCES artist_table(id),
          PRIMARY KEY(id)
        );
        """
        self.cursor.execute(query)

    def create_listener_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS listener_table (
          id INTEGER NOT NULL AUTO_INCREMENT,
          username varchar(32),
          email varchar(32),
          PRIMARY KEY(id),
          UNIQUE(
          username,
          email
          )
        );
        """
        self.cursor.execute(query)

    def create_artist_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS artist_table (
          id INTEGER NOT NULL AUTO_INCREMENT,
          name varchar(32),
          surname varchar(32),
          PRIMARY KEY(id)
        );
        """
        self.cursor.execute(query)

    def create_song_artist_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS song_artist_table (
          id INTEGER NOT NULL AUTO_INCREMENT,
          song_id INTEGER,
          artist_id INTEGER,
          FOREIGN KEY(song_id) REFERENCES song_table(id),
          FOREIGN KEY(artist_id) REFERENCES artist_table(id),
          PRIMARY KEY(id)
        );
        """
        self.cursor.execute(query)

    def create_song_like_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS song_like_table (
          id INTEGER NOT NULL AUTO_INCREMENT,
          listener_id INTEGER,
          song_id INTEGER,
          FOREIGN KEY(listener_id) REFERENCES listener_table(id),
          FOREIGN KEY(song_id) REFERENCES song_table(id),
          PRIMARY KEY(id)
        );
        """
        self.cursor.execute(query)

    def create_album_like_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS album_like_table (
          id INTEGER NOT NULL AUTO_INCREMENT,
          listener_id INTEGER,
          album_id INTEGER,
          FOREIGN KEY(listener_id) REFERENCES listener_table(id),
          FOREIGN KEY(album_id) REFERENCES album_table(id),
          PRIMARY KEY(id)
        );
        """
        self.cursor.execute(query)
