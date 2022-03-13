import datetime

import pytest

from app.models import CoffeeJournal


@pytest.mark.parametrize(
        'entry_datetime, coffee_name, rating, flavor_notes',
        [
            (
                    datetime.datetime(2022, 1, 1, 12, 2, 1, 0),
                    'Test',
                    4,
                    'some test notes',
                    
            )]
)
def test_new_record(entry_datetime, coffee_name, rating, flavor_notes) -> None:
    """Test that a new Coffee Journal Record is created correctly"""

    cj = CoffeeJournal(
            entry_datetime=entry_datetime, coffee_name=coffee_name, rating=rating, flavor_notes=flavor_notes
    )
    assert cj.entry_datetime == entry_datetime
    assert cj.coffee_name == coffee_name
    assert cj.rating == rating
    assert cj.flavor_notes == flavor_notes


@pytest.mark.parametrize(
        'entry_datetime, coffee_name, rating, flavor_notes, expected',
        [
            (
                    datetime.datetime(2022, 1, 1, 12, 2, 1, 0),
                    'Test',
                    4,
                    'some test notes',
                    {
                        'id': None, # because we aren't writing, the db never gives an id
                        'entry_datetime': datetime.datetime(2022, 1, 1, 12, 2, 1, 0),
                        'coffee_name': 'Test',
                        'rating': 4,
                        'flavor_notes': 'some test notes'
                    }
            )]
)
def test_to_dict_method(entry_datetime, coffee_name, rating, flavor_notes, expected) -> None:
    """
    Test whether the to_dict method is outputting what we expect
    """
    cj = CoffeeJournal(
            entry_datetime=entry_datetime, coffee_name=coffee_name, rating=rating, flavor_notes=flavor_notes
    )

    cj_dict = cj.to_dict()

    assert cj_dict == expected
