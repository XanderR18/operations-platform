import logging
from fastapi import HTTPException
from ..services.machine_service import MachineService
from .schemas.machine_response import MachineResponse

logging = logging.getLogger(__name__)

def register_routes(api, services) -> None:
    machine_service: MachineService = services["machine-service"]

    @api.get("/")
    async def root():
        return { "message": "Hello, world!" }
    
    @api.get("/machines", response_model = list[MachineResponse])
    async def get_all_machines():
        return [
            MachineResponse.from_machine(machine)
            for machine in machine_service.get_all_machines().values()
        ]
    
    @api.get("/machines/{machine_id}", response_model = MachineResponse)
    async def get_machine(machine_id: str):
        machine = machine_service.get_machine(machine_id)

        if machine is None:
            raise HTTPException(status_code=404, detail="Machine not found")
        
        return MachineResponse.from_machine(machine)
    
    logging.info("Routes succesfully registered.")