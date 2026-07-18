from datetime import datetime
from enum import Enum, auto

class MachineHealth():
    def __init__(self):
        self.status = MachineHealthStatus.UNKNOWN
        self.last_updated = None

    def update(self: MachineHealth, status: MachineHealthStatus, updated_at: datetime):
        self.status = status
        self.last_updated = updated_at

class MachineHealthStatus(Enum):
    UNKNOWN = auto()
    OFFLINE = auto()
    ONLINE = auto()