from flask import Blueprint, request, jsonify
from services.song_service import SongService

song_bp = Blueprint("song_bp", __name__)


@song_bp.route('/list', methods=["GET"])
def list():
    context = request.args
    return jsonify(SongService().list(context))


@song_bp.route('/create', methods=["GET"])
def create():
    context = request.args
    return SongService().create(context)


@song_bp.route('/update', methods=["GET"])
def create():
    context = request.args
    return SongService().update(context)


@song_bp.route('/delete/<int:_id>', methods=["GET"])
def delete(_id):
    return SongService().delete(_id)
