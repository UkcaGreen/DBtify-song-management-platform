import pymysql

TABLENAME = "artist_table"


class ArtistModel:

    def __init__(self):
        self.connection = self.conn = pymysql.connect(
            "localhost", "root", "", "dbtify")
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

        result = [{"id": e[0], "name": e[1], "surname": e[2]}
                  for e in elements]

        return result

    def delete(self):

        query = f"""
        DELETE
        FROM {TABLENAME};
        """

        self.cursor.execute(query)

        return "OK"

    def login(self, name, surname):

        query = f"""    
        INSERT INTO {TABLENAME} 
        (name, surname) 
        VALUES ("{name}","{surname}");
        """
        self.cursor.execute(query)

        query = f"""    
        SELECT *
        FROM {TABLENAME}
        WHERE name="{name}" OR surname="{surname}"
        """
        self.cursor.execute(query)

        element = self.cursor.fetchall()[0]
        print(element)

        result = {"id": element[0],
                  "name": element[1],
                  "surname": element[2]}

        return result
