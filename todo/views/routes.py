from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__, url_prefix='/api/v1')

@api.route('/health')
def health():
    return jsonify({'status': 'ok'})
    