from flask import Blueprint, request, jsonify
from services.listener_service import ListenerService

listener_bp = Blueprint("listener_bp", __name__)


@listener_bp.route('/list', methods=["GET"])
def list():
    return jsonify(ListenerService().list())


@listener_bp.route('/create', methods=["GET"])
def create():
    context = request.args
    return ListenerService().create(context)


@listener_bp.route('/delete', methods=["GET"])
def delete():
    return ListenerService().delete()
