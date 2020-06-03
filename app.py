from flask import Flask, render_template, session, redirect, url_for, request
from models.schema import Schema

from routes.album_route import album_bp
from routes.artist_route import artist_bp
from routes.song_route import song_bp
from routes.listener_route import listener_bp

from services.song_service import SongService
from services.album_service import AlbumService
from services.artist_service import ArtistService

import sqlite3

app = Flask(__name__)
app.secret_key = "super-secret-key"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/listener/song')
def listener_song():
    context = {
        "songs": SongService().list()
    }
    return render_template('listener_song.html', context=context)


@app.route('/listener/song/popular')
def listener_song_popular():
    context = {
        "songs": SongService().list_by_popularity()
    }
    return render_template('listener_song.html', context=context)


@app.route('/listener/song/liked')
def listener_song_liked():
    context = {
        "songs": SongService().list_liked()
    }
    return render_template('listener_song.html', context=context)


@app.route('/listener/album')
def listener_album():
    context = {
        "albums": AlbumService().list()
    }
    return render_template('listener_album.html', context=context)


@app.route('/listener/artist')
def listener_artist():
    context = {
        "artists": ArtistService().list()
    }
    return render_template('listener_artist.html', context=context)


@app.route('/artist/album')
def artist_album():
    context = {
        "albums": AlbumService().list(),
        "artists": ArtistService().list()
    }
    return render_template('artist_album.html', context=context)


@app.route('/artist/album/<album_id>')
def artist_album_song(album_id):
    context = {
        "album": AlbumService().get_by_id(album_id),
        "songs": SongService().get_by_album_id(album_id),
        "artists": ArtistService().list()
    }
    return render_template('artist_album_song.html', context=context)


if __name__ == '__main__':
    Schema()
    app.register_blueprint(artist_bp, url_prefix="/artist")
    app.register_blueprint(listener_bp, url_prefix="/listener")
    app.register_blueprint(song_bp, url_prefix="/song")
    app.register_blueprint(album_bp, url_prefix="/album")
    app.run(debug=True)
