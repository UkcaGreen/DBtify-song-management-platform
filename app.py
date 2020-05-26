from flask import Flask
from controllers.song_controller import song_bp
from controllers.album_controller import album_bp
import sqlite3

def db_init():
    conn = sqlite3.connect("./database/cat.sql")
    c = conn.cursor()
    try:
        c.execute("""CREATE TABLE listeners (
                username text,
                email text
                )""")
        
        c.execute("""CREATE TABLE artists (
                name text,
                surname text
                )""")
        
        c.execute("""CREATE TABLE songs (
                id integer,
                title text
                )""")

        c.execute("""CREATE TABLE albums (
                id integer,
                title text,
                genre text
                )""")
    except:
        pass
    conn.close()

def flask_init():
    app = Flask(__name__)

    app.register_blueprint(song_bp, url_prefix="/song")
    app.register_blueprint(album_bp, url_prefix="/album")

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app

if __name__ == '__main__':
    db_init()
    app = flask_init()
    app.run(host='localhost', port='8000', debug=True)