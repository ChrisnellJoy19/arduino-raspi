from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import Optional
import pytz

class CompartmentStatus(str, Enum):
    available = 'available'
    unavailable = 'unavailable'
    maintenance = 'maintenance'

class TransactionStatus(str, Enum):
    pending = 'pending'
    completed = 'completed'
    archived = 'archived'

class Compartment(BaseModel):
    id: str
    status: CompartmentStatus
    updated_at: datetime = datetime.now(pytz.UTC)

class Transaction(BaseModel):
    compartment_id: str
    transaction_type: str
    sender: str
    sender_contact: str
    receiver: Optional[str] = ''
    receiver_contact: Optional[str] = ''
    item: str
    item_category: str
    item_subcategory: Optional[str] = ''
    item_detail: Optional[str] = ''
    status: TransactionStatus
    otp: Optional[str] = ''
    dropoff_at: datetime
    received_at: Optional[datetime] = None

class dateutil:
    """
    Date utility helper
    """

    @staticmethod
    def get_datetime_gmt():
        """
        Get current datetime with GMT +8:00
        """
        return datetime.now(pytz.timezone('Asia/Manila'))
