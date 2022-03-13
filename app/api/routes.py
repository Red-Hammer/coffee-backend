from flask import request

from app.utils import construct_standard_response as csr, \
    build_cors_preflight_response as pre_flight

from app.api import bp
from app.api.functions import get_journal_entries, write_journal_entry


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


@bp.route('/write-journal', methods=['POST', 'OPTIONS'])
async def write_journal():
    if request.method == 'OPTIONS':
        return pre_flight()

    # Expected JSON object sample
    # {
    # "entry_datetime": "2022-01-01 11:00:00",
    #  "coffee_name": "Test Coffee 2",
    #  "rating": 4,
    #  "flavor_notes": "Milk Chocolate"
    #  }

    if request.method == 'POST':
        body = request.json
        await write_journal_entry(body)
        return csr({'Status': 'Success'})


@bp.route('/delete-entry/<int:entry_id>', methods=['POST', 'OPTIONS'])
async def delete_entry(entry_id):
    if request.method == 'OPTIONS':
        return pre_flight()

    if request.method == 'POST':
        return csr({'Status': 'You deleted entry with id:{}'.format(entry_id)})
