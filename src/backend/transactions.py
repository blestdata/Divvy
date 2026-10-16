import uuid
import datetime as dt
from decimal import Decimal

class Transaction:
    """
    Main transaction class 
    """
    transaction_id: str
    transaction_description: str
    transaction_created_at: dt.datetime
    transaction_modified_at: dt.datetime
    transaction_created_by: str
    transaction_modified_by: str
    transaction_amount: Decimal


    def __init__(self, transaction_id: str = str(uuid.uuid4()).upper(), transaction_description: str = "",
                 transaction_created_by: str = "", transaction_amount: Decimal = Decimal(0)):
        """
        Initialize the transaction class, 
        Keep in mind operationally we may enter wrond date/amount in some cases, keep a record of last modification
        """
        self.transaction_id = transaction_id
        self.transaction_description = transaction_description
        self.transaction_created_at = dt.datetime.now(dt.timezone.utc)
        self.transaction_modified_at = dt.datetime.now(dt.timezone.utc)
        self.transaction_created_by = transaction_created_by
        self.transaction_modified_by = transaction_created_by
        self.transaction_amount = transaction_amount
        
