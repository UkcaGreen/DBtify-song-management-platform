from flask import Blueprint, request, jsonify
from services.artist_service import ArtistService

artist_bp = Blueprint("artist_bp", __name__)


@artist_bp.route('/list', methods=["GET"])
def list():
    return jsonify(ArtistService().list())


@artist_bp.route('/create', methods=["GET"])
def create():
    context = request.args
    return ArtistService().create(context)


@artist_bp.route('/delete', methods=["GET"])
def delete():
    return ArtistService().delete()
