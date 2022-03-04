from flask import request

from app.utils import construct_standard_response as csr, \
    build_cors_preflight_response as pre_flight
from app.api import bp


@bp.route('/test', methods=['GET', 'OPTIONS'])
def test():
    if request.method == 'OPTIONS':
        return pre_flight()

    if request.method == 'GET':
        body = {'test_key': 'test_val'}
        return csr(body)
