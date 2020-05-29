from flask import Flask
from models.schema import Schema

from routes.album_route import album_bp
from routes.artist_route import artist_bp
from routes.song_route import song_bp
from routes.listener_route import listener_bp

import sqlite3

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    Schema()
    app.register_blueprint(artist_bp, url_prefix="/artist")
    app.register_blueprint(listener_bp, url_prefix="/listener")
    app.register_blueprint(song_bp, url_prefix="/song")
    app.register_blueprint(album_bp, url_prefix="/album")
    app.run(debug=True)