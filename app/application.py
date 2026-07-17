import logging
from enum import Enum, auto
from .services.machine_service import MachineService
from .bootstrap import bootstrap

logging = logging.getLogger(__name__)

class Application():
    def __init__(self):
        self.status = ApplicationStatus.STOPPED
        self.machine_service = MachineService()

    def start(self):
        if self.status != ApplicationStatus.STOPPED:
            raise InvalidStateTransition(f"Cannot start application while status is {self.status.name}.")
        
        self.status = ApplicationStatus.STARTING
        logging.info(f"Application starting. Status: {self.status.name}")

        # Start services
        self.machine_service.start()

        # Creates inital state of the platform
        bootstrap(self.machine_service)

        self.status = ApplicationStatus.RUNNING
        logging.info(f"Application started. Status: {self.status.name}")

    def stop(self):
        if self.status != ApplicationStatus.RUNNING:
            raise InvalidStateTransition(f"Cannot shutdown application while status is {self.status.name}.")

        self.status = ApplicationStatus.STOPPING
        logging.info(f"Application stopping. Status: {self.status.name}")

        # Stop services
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