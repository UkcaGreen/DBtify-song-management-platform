import sqlite3

TABLENAME = "ARTISTS"

class ArtistModel:

    def __init__(self):
        self.connection = sqlite3.connect('database/db.sql')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.commit()
        self.connection.close()

    def create(self, name, surname):
        
        query = f"""
        INSERT INTO {TABLENAME} 
        (name, surname) 
        VALUES ("{name}","{surname}");
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

        result = [{"id": e[0], "name": e[1], "surname": e[2]} for e in elements]

        return result

    def delete(self):

        query = f"""
        DELETE
        FROM {TABLENAME};
        """

        self.cursor.execute(query)

        return "OK"