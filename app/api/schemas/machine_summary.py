from pydantic import BaseModel

class MachineSummary(BaseModel):
    total: int
    statuses: dict[str, int]
