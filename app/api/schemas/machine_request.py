from pydantic import BaseModel
from app.models.machine import MachineRole

class MachineRequest(BaseModel):
    id: str
    host_name: str
    ip: str
    mac: str
    role: MachineRole