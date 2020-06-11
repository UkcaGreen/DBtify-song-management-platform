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
    context = []
    return render_template('index.html', context=context)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/listener/song/<page>', methods=["GET", "POST"])
def listener_song(page):
    if page == "all":
        title = "All Songs"
        songs = SongService().list()
    elif page == "popular":
        title = "Popular Songs"
        songs = SongService().list_by_popularity()
    elif page == "liked":
        title = "Liked Songs"
        songs = SongService().list_liked()
    elif page == "search":
        title = "Searched Songs"
        form = request.form
        songs = SongService().search(form)
    else:
        return

    genres = AlbumService().list_genre()

    context = {
        "title": title,
        "genres": genres,
        "songs": songs
    }
    return render_template('listener_song.html', context=context)


@app.route('/listener/song/by/<page>/<_id>')
def listener_song_specific(page, _id):
    if page == "artist":
        title = "Songs of An Artist"
        songs = SongService().list_by_artist_id(_id)
    elif page == "album":
        title = "Songs of An Album"
        songs = SongService().list_by_album_id(_id)
    elif page == "listener":
        title = "Songs that are Liked by a Listener"
        songs = SongService().list_by_listener_id(_id)
    else:
        return

    genres = AlbumService().list_genre()

    context = {
        "title": title,
        "genres": genres,
        "songs": songs
    }
    return render_template('listener_song.html', context=context)


@app.route('/listener/song/by/artist/<_id>/popular')
def listener_song_artist_popular(_id):
    title = "Popular Songs"
    songs = SongService().list_by_artist_id_and_popularity(_id)

    genres = AlbumService().list_genre()

    context = {
        "title": title,
        "genres": genres,
        "songs": songs
    }
    return render_template('listener_song.html', context=context)


@app.route('/listener/album/<page>')
def listener_album(page):
    if page == "all":
        title = "All Albums"
        albums = AlbumService().list()
    elif page == "popular":
        title = "Popular Albums"
        albums = AlbumService().list_by_popularity()
    elif page == "liked":
        title = "Liked Albums"
        albums = AlbumService().list_liked()
    else:
        return

    genres = AlbumService().list_genre()

    context = {
        "title": title,
        "genres": genres,
        "albums": albums
    }
    return render_template('listener_album.html', context=context)


@app.route('/listener/album/<page>/<key>')
def listener_album_specific(page, key):
    if page == "artist":
        albums = AlbumService().list_by_artist_id(key)
    elif page == "genre":
        albums = AlbumService().list_by_genre(key)
    else:
        return

    title = "Albums of Artist"
    genres = AlbumService().list_genre()

    context = {
        "title": title,
        "genres": genres,
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

    title = "Artists"
    genres = AlbumService().list_genre()

    context = {
        "title": title,
        "genres": genres,
        "artists": artists
    }
    return render_template('listener_artist.html', context=context)


@app.route('/listener/listener')
def listener_listener():
    title = "Listeners"
    genres = AlbumService().list_genre()

    context = {
        "title": title,
        "genres": genres,
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
