import pytest
import datetime
from app.api.functions import get_journal_entries


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
async def test_get_journal_entry_success(expected):
    actual = await get_journal_entries()
    print(actual)

    assert actual == expected
