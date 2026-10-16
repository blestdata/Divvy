import uuid
import datetime as dt

class Account:
    """
    Handles all Accounts 
    """
    account_id: str
    account_name: str
    account_created_at: dt.datetime

    def __init__(self, account_id: str = str(uuid.uuid4()).upper(), account_name: str = ""):
        self.account_id = account_id
        self.account_name = account_name
        self.account_created_at = dt.datetime.now(dt.timezone.utc)
