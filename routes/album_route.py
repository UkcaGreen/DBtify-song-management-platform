from flask import Blueprint, request, jsonify
from services.album_service import AlbumService

album_bp = Blueprint("album_bp", __name__)


@album_bp.route('/list', methods=["GET"])
def list():
    return jsonify(AlbumService().list())


@album_bp.route('/create', methods=["GET"])
def create():
    context = request.args
    return AlbumService().create(context)


@album_bp.route('/delete/<int:_id>', methods=["GET"])
def delete(_id):
    return AlbumService().delete(_id)
