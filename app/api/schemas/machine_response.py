from pydantic import BaseModel
from datetime import datetime
from ...models.machine import Machine

class MachineResponse(BaseModel):
    id: str
    host_name: str
    ip: str
    role: str
    status: str
    last_updated: datetime | None

    @classmethod
    def from_machine(cls, machine: Machine) -> MachineResponse:
        return cls(
            id = machine.id,
            host_name = machine.host_name,
            ip = machine.ip,
            role = machine.role.name,
            status = machine.health.status.name,
            last_updated = machine.health.last_updated
        )