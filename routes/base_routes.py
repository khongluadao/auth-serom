from flask import Blueprint
from controllers.base_controller import index, healthy, devices, login, logout, work, log_api

base_bp = Blueprint('base', __name__)

base_bp.route('/', methods=['GET'])(index)
base_bp.route('/healthy', methods=['GET', 'POST'])(healthy)
base_bp.route('/devices', methods=['GET'])(devices)
base_bp.route('/login', methods=['GET', 'POST'])(login)
base_bp.route('/logout', methods=['GET'])(logout)
base_bp.route('/work', methods=['GET', 'POST'])(work)
base_bp.route('/log', methods=['GET', 'POST'])(log_api)
