from fastapi import FastAPI

class APIServer():
    def __init__(self):
        self.app = FastAPI()
        self.services = {}

    def start(self):
        pass

    def stop(self):
        pass

    def add_service(self, service):
        self.services[service.name] = service