import logging
from enum import Enum, auto

logging = logging.getLogger(__name__)

class Application():
    def __init__(self):
        self.status = ApplicationStatus.STOPPED

    def start(self):
        if self.status != ApplicationStatus.STOPPED:
            raise InvalidStateTransition(f"Cannot start application while status is {self.status.name}.")
        
        self.status = ApplicationStatus.STARTING
        logging.info(f"Application starting. Status: {self.status.name}")

        self.status = ApplicationStatus.RUNNING
        logging.info(f"Application started. Status: {self.status.name}")

    def shutdown(self):
        if self.status != ApplicationStatus.RUNNING:
            raise InvalidStateTransition(f"Cannot shutdown application while status is {self.status.name}.")

        self.status = ApplicationStatus.SHUTTING_DOWN
        logging.info(f"Application shutting down. Status: {self.status.name}")
        
        self.status = ApplicationStatus.STOPPED
        logging.info(f"Application stopped. Status: {self.status.name}")

class ApplicationStatus(Enum):
    STARTING = auto()
    RUNNING = auto()
    SHUTTING_DOWN = auto()
    STOPPED = auto()

class InvalidStateTransition(Exception):
    pass