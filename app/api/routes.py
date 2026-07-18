import logging
from fastapi import HTTPException
from ..services.machine_service import MachineService, DuplicateMachine, MachineNotFound
from ..models.machine import Machine
from .schemas.machine_response import MachineResponse
from .schemas.machine_request import MachineRequest

logging = logging.getLogger(__name__)

def register_routes(api, services) -> None:
    machine_service: MachineService = services["machine-service"]

    @api.get("/")
    async def root():
        return { "message": "Hello, world!" }
    
    # Discovery
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
    
    # Management
    @api.post("/machines", response_model = MachineResponse)
    async def create_machine(req: MachineRequest):
        try:
            machine = Machine(
                id = req.id,
                host_name = req.host_name,
                ip = req.ip,
                mac = req.mac,
                role = req.role
            )

            machine_service.add_machine(machine)

        except DuplicateMachine as e:
            raise HTTPException(status_code=400, detail=str(e))

        return MachineResponse.from_machine(machine)
    
    @api.post("/machines/{machine_id}", response_model = MachineResponse)
    async def update_machine(machine_id: str, req: MachineRequest):
        try:
            updated_machine = Machine(
                id=machine_id,
                host_name=req.host_name,
                ip=req.ip,
                mac=req.mac,
                role=req.role
            )

            machine_service.update_machine_identity(updated_machine)

            machine = machine_service.get_machine(machine_id)

        except MachineNotFound as e:
            raise HTTPException(status_code=404, detail=str(e))

        return MachineResponse.from_machine(machine)
    
    @api.delete("/machines/{machine_id}")
    async def delete_machine(machine_id: str):
        try:
            machine_service.remove_machine(machine_id)
        except MachineNotFound as e:
            raise HTTPException(status_code=404, detail=str(e))

    # Operations
    @api.patch("/machines/{machine_id}/refresh", response_model = MachineResponse)
    async def refresh_machine(machine_id: str):
        try:
            machine_service.refresh_machine_health(machine_id)
        except MachineNotFound as e:
            raise HTTPException(status_code=404, detail=str(e))
        
        updated_machine = machine_service.get_machine(machine_id)

        return MachineResponse.from_machine(updated_machine)

    @api.patch("/machines/refresh", response_model = list[MachineResponse])
    async def refresh_all_machines():
        machine_service.refresh_health()
        return [
            MachineResponse.from_machine(machine)
            for machine in machine_service.get_all_machines().values()
        ]

    # Statistics
    # Machines summary
    
    logging.info("Routes succesfully registered.")