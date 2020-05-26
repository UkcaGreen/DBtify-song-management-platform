from flask import Blueprint, request, jsonify
from services.album_service import AlbumService

album_bp = Blueprint("album_bp", __name__)

@album_bp.route('/',method=["GET"])
def getAll():
    return AlbumService().getAll() 

@album_bp.route('/create',method=["POST"])
def create():
    return AlbumService().create(request.get_json())

@album_bp.route('/update',method=["POST"])
def update():
    return AlbumService().update(request.get_json())

@album_bp.route('/delete', method=["GET"])
def delete():
    return AlbumService().delete(request.get_json())