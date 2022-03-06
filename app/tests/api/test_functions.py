import pytest
import datetime
from app.models import CoffeeJournal
from app.api.functions import get_journal_entries, write_journal_entry


@pytest.mark.parametrize(
        'expected',
        [
            (
                    [{'entry_datetime': datetime.datetime(2022, 1, 1, 12, 0), 'coffee_name': 'Test Coffee', 'rating': 7,
                      'flavor_notes': 'Bold,Fruity,Dark Chocolate'},
                     {'entry_datetime': datetime.datetime(2022, 1, 1, 11, 0), 'coffee_name': 'Test Coffee 2',
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
                    {'entry_datetime': datetime.datetime(2022, 1, 1, 12, 0), 'coffee_name': 'Test New Coffee',
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
