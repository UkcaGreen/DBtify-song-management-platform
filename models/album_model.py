import sqlite3

TABLENAME = "ALBUMS"


class AlbumModel:

    def __init__(self):
        self.connection = sqlite3.connect('database/db.sql')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.commit()
        self.connection.close()

    def create(self, title, genre):

        query = f"""
        INSERT INTO {TABLENAME} 
        (title, genre) 
        VALUES ("{title}","{genre}");
        """

        result = self.cursor.execute(query)

        return "OK"

    def list(self):

        query = f"""
        SELECT *
        FROM {TABLENAME};
        """

        self.cursor.execute(query)

        elements = self.cursor.fetchall()

        result = [{"id": e[0], "title": e[1], "genre": e[2]} for e in elements]

        return result

    def delete(self, _id):

        query = f"""
        DELETE
        FROM {TABLENAME}
        WHERE id={_id};
        """

        self.cursor.execute(query)

        return "OK"
