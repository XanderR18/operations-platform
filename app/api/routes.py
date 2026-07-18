import logging
from ..services.machine_service import MachineService
from .schemas.machine_response import MachineResponse

logging = logging.getLogger(__name__)

def register_routes(api, services) -> None:
    machine_service: MachineService = services["machine-service"]

    @api.get("/")
    async def root():
        return { "message": "Hello, world!" }
    
    @api.get("/machines", response_model = list[MachineResponse])
    async def list_machines():
        return [
            MachineResponse.from_machine(machine)
            for machine in machine_service.get_all_machines().values()
        ]
    
    logging.info("Routes succesfully registered.")