import pytest
import datetime
from app import db
from app.models import CoffeeJournal
from app.api.functions import get_journal_entries, write_journal_entry, delete_journal_entry


@pytest.fixture
def insert_record_for_deletion():
    journal_entry = {'entry_datetime': datetime.datetime(2022, 1, 1, 12, 0), 'coffee_name': 'Delete',
                     'rating': 1,
                     'flavor_notes': 'ugly'}
    insert_del = CoffeeJournal(
            entry_datetime=journal_entry['entry_datetime'],  # Do this to keep server time
            coffee_name=journal_entry['coffee_name'],
            rating=journal_entry['rating'],
            flavor_notes=journal_entry['flavor_notes']
    )
    db.session.add(insert_del)
    db.session.commit()

    return insert_del.id


@pytest.mark.parametrize(
        'expected',
        [
            (
                    [{'id': 1, 'entry_datetime': datetime.datetime(2022, 1, 1, 12, 0), 'coffee_name': 'Test Coffee',
                      'rating': 7,
                      'flavor_notes': 'Bold,Fruity,Dark Chocolate'},
                     {'id': 2, 'entry_datetime': datetime.datetime(2022, 1, 1, 11, 0), 'coffee_name': 'Test Coffee 2',
                      'rating': 4,
                      'flavor_notes': 'Milk Chocolate'}]
            )
        ]
)
@pytest.mark.asyncio
async def test_get_journal_entries_success(expected):
    actual = await get_journal_entries()

    assert actual == expected


@pytest.mark.parametrize(
        'body, expected',
        [
            (
                    {'entry_datetime': datetime.datetime(2022, 1, 1, 12, 0), 'coffee_name': 'Test New Coffee',
                     'rating': 10,
                     'flavor_notes': 'Bold,Fruity,Caramel'},
                    {'id': 3, 'entry_datetime': datetime.datetime(2022, 1, 1, 12, 0), 'coffee_name': 'Test New Coffee',
                     'rating': 10,
                     'flavor_notes': 'Bold,Fruity,Caramel'}
            )
        ]
)
@pytest.mark.asyncio
async def test_write_journal_entry_success(body, expected):
    await write_journal_entry(body)

    actual = CoffeeJournal.query.filter_by(coffee_name=body['coffee_name']).first().to_dict()

    assert actual == expected


@pytest.mark.asyncio
async def test_del_journal_entry(insert_record_for_deletion):
    await delete_journal_entry(insert_record_for_deletion)

    actual = CoffeeJournal.query.filter_by(coffee_name='Delete').first()

    assert actual is None
