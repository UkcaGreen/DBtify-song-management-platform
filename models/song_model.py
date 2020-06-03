import pymysql

TABLENAME = "song_table"


class SongModel:

    def __init__(self):
        self.connection = self.conn = pymysql.connect(
            "localhost", "root", "", "dbtify")
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.commit()
        self.connection.close()

    def create(self, title, album_id, artist_id, other_artists):

        query = f"""
        INSERT INTO {TABLENAME} 
        (title, album_id) 
        VALUES ("{title}","{album_id}");
        """
        self.cursor.execute(query)

        query = f"""
        SELECT id 
        FROM {TABLENAME} 
        WHERE title='{title}' AND album_id='{album_id}'
        LIMIT 1;
        """
        self.cursor.execute(query)

        song_id = self.cursor.fetchone()[0]

        if(type(other_artists) == str):
            other_artists = [other_artists]

        artists = [artist_id] + other_artists

        for artist_id in artists:
            query = f"""
            INSERT INTO song_artist_table
            (song_id, artist_id)
            VALUES ("{song_id}","{artist_id}");
            """
            result = self.cursor.execute(query)

    def delete(self, _id):

        query = f"""
        DELETE
        FROM {TABLENAME}
        WHERE id='{_id}';
        """

        self.cursor.execute(query)

        return "OK"

    def update(self, _id, title):

        query = f"""
            UPDATE {TABLENAME}
            SET title="{title}"
            WHERE id="{_id}"; 
        """

        result = self.cursor.execute(query)

        return "OK"

    def list(self):

        query = f"""
        SELECT 
        song_table.id AS song_id,
        song_table.title AS song_title,
        album_table.title AS album_title,
        GROUP_CONCAT(CONCAT(artist_table.name, ' ',artist_table.surname)) AS full_names,
        NOT ISNULL(song_like_table.listener_id) AS liked
        FROM song_artist_table 
        INNER JOIN song_table ON song_table.id = song_artist_table.song_id
        INNER JOIN artist_table ON artist_table.id = song_artist_table.artist_id
        INNER JOIN album_table ON album_table.id = song_table.album_id
        LEFT JOIN song_like_table ON song_like_table.song_id = song_table.id
        GROUP BY song_id;
        """

        self.cursor.execute(query)

        songs = self.cursor.fetchall()

        result = [{
            "song_id": song[0],
            "song_title": song[1],
            "album_title": song[2],
            "artist_names": song[3],
            "is_liked": song[4]
        } for song in songs]

        return result

    def get_by_album_id(self, album_id):

        query = f"""
        SELECT 
        song_table.id AS song_id,
        song_table.title AS song_title,
        album_table.title AS album_title,
        GROUP_CONCAT(CONCAT(artist_table.name, ' ',artist_table.surname)) AS full_names,
        NOT ISNULL(song_like_table.listener_id) AS liked
        FROM song_artist_table 
        INNER JOIN song_table ON song_table.id = song_artist_table.song_id
        INNER JOIN artist_table ON artist_table.id = song_artist_table.artist_id
        INNER JOIN album_table ON album_table.id = song_table.album_id
        LEFT JOIN song_like_table ON song_like_table.song_id = song_table.id
        WHERE song_table.album_id={album_id}
        GROUP BY song_id;
        """
        self.cursor.execute(query)

        songs = self.cursor.fetchall()

        result = [{
            "song_id": song[0],
            "song_title": song[1],
            "album_title": song[2],
            "artist_names": song[3],
            "is_liked": song[4]
        }for song in songs]

        return result

    def delete(self, _id):

        query = f"""
        DELETE
        FROM {TABLENAME}
        WHERE id={_id};
        """

        self.cursor.execute(query)

        return "OK"

    def like(self, song_id, listener_id):

        query = f"""    
        INSERT INTO song_like_table
        (song_id, listener_id) 
        VALUES ("{song_id}","{listener_id}");
        """
        self.cursor.execute(query)

        return "OK"

    def unlike(self, song_id, listener_id):

        query = f"""    
        DELETE 
        FROM song_like_table
        WHERE song_id='{song_id}' AND listener_id='{listener_id}';
        """
        self.cursor.execute(query)

        return "OK"
