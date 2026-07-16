from enum import Enum, auto

class Application():
    def __init__(self):
        self.status = ApplicationStatus.STOPPED

    def start(self):
        if self.status != ApplicationStatus.STOPPED:
            raise InvalidStateTransition(f"Cannot start application while status is {self.status.name}.")
        
        self.status = ApplicationStatus.STARTING
        # print("Vroom vroom, I started.")
        self.status = ApplicationStatus.RUNNING

    def shutdown(self):
        if self.status != ApplicationStatus.RUNNING:
            raise InvalidStateTransition(f"Cannot shutdown application while status is {self.status.name}.")

        self.status = ApplicationStatus.SHUTTING_DOWN
        # print("Bye bye, I am shutting down.")
        self.status = ApplicationStatus.STOPPED

class ApplicationStatus(Enum):
    STARTING = auto()
    RUNNING = auto()
    SHUTTING_DOWN = auto()
    STOPPED = auto()

class InvalidStateTransition(Exception):
    pass