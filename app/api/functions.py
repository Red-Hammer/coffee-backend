from typing import List, Dict
from operator import itemgetter
import datetime

from app import db
from app.models import CoffeeJournal


async def get_journal_entries(account_id: int = None) -> List[Dict]:
    if not account_id:
        records = [r.to_dict() for r in CoffeeJournal.query]
        return sorted(records, key=itemgetter('entry_datetime'), reverse=True)
    # Add account id logic later


async def write_journal_entry(journal_entry: Dict, account_id: int = None) -> None:
    if not account_id:
        if 'entry_datetime' not in journal_entry.keys():
            journal_entry['entry_datetime'] = datetime.datetime.now()
        new_entry = CoffeeJournal(
                entry_datetime=journal_entry['entry_datetime'],  # Do this to keep server time
                coffee_name=journal_entry['coffee_name'],
                rating=journal_entry['rating'],
                flavor_notes=journal_entry['flavor_notes']
        )
        db.session.add(new_entry)
        db.session.commit()


async def delete_journal_entry(entry_id: int, account_id: int = None):
    if not account_id:
        record_to_delete = CoffeeJournal.query.filter_by(id=entry_id).first()
        if record_to_delete:
            db.session.delete(record_to_delete)
            db.session.commit()
