from enum import Enum, auto
from .machine_health import MachineHealth

class Machine():
    def __init__(self, id, host_name, IP, MAC, role):
        self.id = id
        self.host_name = host_name
        self.ip = IP
        self.mac = MAC
        self.role = role
        self.health = MachineHealth()

    def __repr__(self) -> str:
        return f"Machine(id='{self.id}', name='{self.host_name}', ip='{self.ip}', mac='{self.mac}')"
    
class MachineRole(Enum):
    COMPUTE = auto()
    NETWORK = auto()
    STORAGE = auto()
    WORKSTATION = auto()