from flask import request

from app.utils import construct_standard_response as csr, \
    build_cors_preflight_response as pre_flight

from app.api import bp
from app.api.functions import get_journal_entries


@bp.route('/test', methods=['GET', 'OPTIONS'])
def test():
    if request.method == 'OPTIONS':
        return pre_flight()

    if request.method == 'GET':
        body = {'test_key': 'test_val'}
        return csr(body)


@bp.route('/read-journal', methods=['GET', 'OPTIONS'])
async def read_journal():
    """Read the journal and return the results as a json object"""
    if request.method == 'OPTIONS':
        return pre_flight()

    if request.method == 'GET':
        records = await get_journal_entries()
        return csr(records)
