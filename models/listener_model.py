import sqlite3

TABLENAME = "LISTENERS"


class ListenerModel:

    def __init__(self):
        self.connection = sqlite3.connect('database/db.sql')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.commit()
        self.connection.close()

    def create(self, username, email):

        query = f"""
        INSERT INTO {TABLENAME} 
        (username, email) 
        VALUES ("{username}","{email}");
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

        result = [{"id": e[0], "username": e[1], "email": e[2]}
                  for e in elements]

        return result

    def delete(self):

        query = f"""
        DELETE
        FROM {TABLENAME};
        """

        self.cursor.execute(query)

        return "OK"
