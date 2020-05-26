from flask import Blueprint

song_bp = Blueprint("song_bp", __name__)

@song_bp.route('/')
def get():
    return 'get song'

@song_bp.route('/create')
def create():
    return 'create  song'

@song_bp.route('/update')
def update():
    return 'create  song'

@song_bp.route('/delete')
def delete():
    return 'delete song'


