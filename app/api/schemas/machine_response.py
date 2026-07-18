from pydantic import BaseModel
from datetime import datetime
from ...models.machine import Machine, MachineRole
from ...models.machine_health import MachineHealthStatus

class MachineResponse(BaseModel):
    id: str
    host_name: str
    ip: str
    role: MachineRole
    status: MachineHealthStatus
    last_updated: datetime | None

    @classmethod
    def from_machine(cls, machine: Machine):
        return cls(
            id = machine.id,
            host_name = machine.host_name,
            ip = machine.ip,
            role = machine.role,
            status = machine.health.status,
            last_updated = machine.health.last_updated
        )