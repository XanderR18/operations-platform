from fastapi import FastAPI
from .routes import register_routes

class APIServer():
    def __init__(self):
        self.app = FastAPI()
        self.services = {}

    def start(self):
        self._register_routes()

    def stop(self):
        pass

    def add_service(self, service):
        if service.name in self.services:
            raise DuplicateService(f"Service with name: {service.name} already exists")

        self.services[service.name] = service

    def _register_routes(self):
        register_routes(self.app, self.services)

class DuplicateService(Exception):
    pass