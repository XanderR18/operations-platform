import logging
from enum import Enum, auto
from ..services.machine_service import MachineService
from ..bootstrap import bootstrap
from ..api.server import APIServer

logging = logging.getLogger(__name__)

class Application():
    def __init__(self):
        self.status = ApplicationStatus.STOPPED
        self.machine_service = MachineService("machine-service")
        self.api_server = APIServer()

    def start(self) -> None:
        if self.status != ApplicationStatus.STOPPED:
            raise InvalidStateTransition(f"Cannot start application while status is {self.status.name}.")
        
        self.status = ApplicationStatus.STARTING
        logging.info(f"Application starting. Status: {self.status.name}")

        # Start services
        logging.info("Starting machine service...")
        self.machine_service.start()

        # Creates inital state of the platform
        logging.info("Bootstrapping application...")
        bootstrap(self.machine_service)

        # Initial health refresh
        logging.info("Updating initial device healths")
        self.machine_service.refresh_health()

        # Add service to API
        logging.info("Adding machine service to API...")
        self.api_server.add_service(self.machine_service)

        # Start API
        logging.info("Starting API...")
        self.api_server.start()        

        self.status = ApplicationStatus.RUNNING
        logging.info(f"Application started. Status: {self.status.name}")

    def stop(self) -> None:
        if self.status != ApplicationStatus.RUNNING:
            raise InvalidStateTransition(f"Cannot shutdown application while status is {self.status.name}.")

        self.status = ApplicationStatus.STOPPING
        logging.info(f"Application stopping. Status: {self.status.name}")

        # Stop services
        logging.info("Stopping machine service...")
        self.machine_service.stop()
        
        self.status = ApplicationStatus.STOPPED
        logging.info(f"Application stopped. Status: {self.status.name}")

class ApplicationStatus(Enum):
    STARTING = auto()
    RUNNING = auto()
    STOPPING = auto()
    STOPPED = auto()

class InvalidStateTransition(Exception):
    pass