from typing import List, Dict
from operator import itemgetter

from app import db
from app.models import CoffeeJournal


async def get_journal_entries(account_id: int = None) -> List[Dict]:
    if not account_id:
        records = [r.to_dict() for r in CoffeeJournal.query]
        return sorted(records, key=itemgetter('entry_datetime'), reverse=True)
    # Add account id logic later


async def write_journal_entry(journal_entry: Dict, account_id: int = None) -> None:
    if not account_id:
        new_entry = CoffeeJournal(
                entry_datetime=journal_entry['entry_datetime'],
                coffee_name=journal_entry['coffee_name'],
                rating=journal_entry['rating'],
                flavor_notes=journal_entry['flavor_notes']
        )
        db.session.add(new_entry)
        db.session.commit()
