from flask import Flask, render_template, session, redirect, url_for, request
from models.schema import Schema

from routes.album_route import album_bp
from routes.artist_route import artist_bp
from routes.song_route import song_bp
from routes.listener_route import listener_bp

from services.song_service import SongService
from services.album_service import AlbumService
from services.artist_service import ArtistService
from services.listener_service import ListenerService

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


@app.route('/listener/song/<page>')
def listener_song(page):
    if page == "all":
        songs = SongService().list()
    elif page == "popular":
        songs = SongService().list_by_popularity()
    elif page == "liked":
        songs = SongService().list_liked()
    else:
        return

    context = {
        "songs": songs
    }
    return render_template('listener_song.html', context=context)


@app.route('/listener/song/by/<page>/<_id>')
def listener_song_specific(page, _id):
    if page == "artist":
        songs = SongService().list_by_artist_id(_id)
    elif page == "album":
        songs = SongService().list_by_album_id(_id)
    elif page == "listener":
        songs = SongService().list_by_listener_id(_id)
    else:
        return

    context = {
        "songs": songs
    }
    return render_template('listener_song.html', context=context)


@app.route('/listener/song/by/artist/<_id>/popular')
def listener_song_artist_popular(_id):
    songs = SongService().list_by_artist_id_and_popularity(_id)

    context = {
        "songs": songs
    }
    return render_template('listener_song.html', context=context)


@app.route('/listener/album/<page>')
def listener_album(page):
    if page == "all":
        albums = AlbumService().list()
    elif page == "popular":
        albums = AlbumService().list_by_popularity()
    elif page == "liked":
        albums = AlbumService().list_liked()
    else:
        return

    context = {
        "albums": albums
    }
    return render_template('listener_album.html', context=context)


@app.route('/listener/album/<page>/<_id>')
def listener_album_specific(page, _id):
    if page == "artist":
        albums = AlbumService().list_by_artist_id(_id)
    else:
        return

    context = {
        "albums": albums
    }
    return render_template('listener_album.html', context=context)


@app.route('/listener/artist/<page>')
def listener_artist(page):
    if page == "all":
        artists = ArtistService().list()
    elif page == "popular":
        artists = ArtistService().list_by_popularity()
    else:
        return

    context = {
        "artists": artists
    }
    return render_template('listener_artist.html', context=context)


@app.route('/listener/listener')
def listener_listener():
    context = {
        "listeners": ListenerService().list()
    }
    return render_template('listener_listener.html', context=context)


@app.route('/artist/album')
def artist_album():
    context = {
        "albums": AlbumService().list_by_artist_id(session["id"]),
        "artists": ArtistService().list()
    }
    return render_template('artist_album.html', context=context)


@app.route('/artist/album/<album_id>')
def artist_album_song(album_id):
    context = {
        "album": AlbumService().get_by_id(album_id),
        "songs": SongService().list_by_album_id(album_id),
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
