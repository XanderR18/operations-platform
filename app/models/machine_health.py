from enum import Enum, auto
import datetime

class MachineHealth():
    def __init__(self):
        self.status = MachineHealthStatus.UNKNOWN
        self.last_updated = None

class MachineHealthStatus(Enum):
    UNKNOWN = auto()
    OFFLINE = auto()
    ONLINE = auto()