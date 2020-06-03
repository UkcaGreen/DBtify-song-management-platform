import pymysql
TABLENAME = "listener_table"


class ListenerModel:

    def __init__(self):
        self.connection = self.conn = pymysql.connect(
            "localhost", "root", "", "dbtify")
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

    def login(self, username, email):

        query = f"""    
        INSERT INTO {TABLENAME} 
        (username, email) 
        VALUES ("{username}","{email}");
        """
        self.cursor.execute(query)

        query = f"""    
        SELECT *
        FROM {TABLENAME}
        WHERE username="{username}" OR email="{email}"
        """
        self.cursor.execute(query)

        element = self.cursor.fetchall()[0]

        result = {"id": element[0],
                  "username": element[1],
                  "email": element[2]}

        return result
