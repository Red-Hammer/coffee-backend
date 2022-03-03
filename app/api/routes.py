from flask import render_template, jsonify
from app.api import bp


@bp.route('/')
@bp.route('/test')
def test():
    return jsonify({'test_key': 'test_val'})
