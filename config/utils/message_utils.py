# config/utils/message_utils.py
from enum import Enum

class MessageType(Enum):
    SUCCESS = 'success'
    ERROR = 'error'
    WARNING = 'warning'
    INFO = 'info'