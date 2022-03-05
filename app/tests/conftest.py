import datetime

import pytest_asyncio

from app import create_app, db
from app.models import CoffeeJournal
from test_config import TestConfig


@pytest_asyncio.fixture(scope='session', autouse=True)
def test_client():
    flask_app = create_app(TestConfig)

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


@pytest_asyncio.fixture(scope='function', autouse=True)
def init_db(test_client):
    db.create_all()

    # insert some fake data
    x = CoffeeJournal(
            entry_datetime=datetime.datetime(2022, 1, 1, 12, 0, 0, 0),
            coffee_name='Test Coffee',
            rating=7,
            flavor_notes='Bold,Fruity,Dark Chocolate'
    )
    db.session.add(x)
    db.session.commit()

    y = CoffeeJournal(
            entry_datetime=datetime.datetime(2022, 1, 1, 11, 0, 0, 0),
            coffee_name='Test Coffee 2',
            rating=4,
            flavor_notes='Milk Chocolate'
    )

    db.session.add(y)
    db.session.commit()

    yield

    db.drop_all()
