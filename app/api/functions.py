from typing import List, Dict
from operator import itemgetter

from app.models import CoffeeJournal


async def get_journal_entries(account_id: int = None) -> List[Dict]:
    if not account_id:
        records = [r.to_dict() for r in CoffeeJournal.query]
        return sorted(records, key=itemgetter('entry_datetime'), reverse=True)
    # Add account id logic later
