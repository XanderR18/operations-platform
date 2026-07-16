from enum import Enum, auto

class ApplicationStatus(Enum):
    STARTING = auto()
    RUNNING = auto()
    SHUTTING_DOWN = auto()
    STOPPED = auto()

class Application():
    def __init__(self):
        pass

    def start(self):
        self.status = ApplicationStatus.STARTING
        print("Vroom vroom, I started.")
        self.status = ApplicationStatus.RUNNING

    def shutdown(self):
        self.status = ApplicationStatus.SHUTTING_DOWN
        print("Bye bye, I am shutting down.")
        self.status = ApplicationStatus.STOPPED