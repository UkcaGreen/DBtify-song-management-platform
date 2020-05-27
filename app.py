from flask import Flask
from models.schema import Schema

#from view.album_view import song_bp
from view.artist_view import artist_bp
#from view.song_view import song_bp
from view.listener_view import listener_bp

import sqlite3

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    Schema()
    app.register_blueprint(artist_bp, url_prefix="/artist")
    app.register_blueprint(listener_bp, url_prefix="/listener")
    app.run(debug=True)