import logging
from fastapi import FastAPI
from .routes import register_routes

logging = logging.getLogger(__name__)

class APIServer():
    def __init__(self):
        self.app = FastAPI()
        self.services = {}

    def start(self: APIServer) -> None:
        logging.info("Registering routes...")
        self._register_routes()

        logging.info("API succesfully started.")

    def stop(self: APIServer) -> None:
        logging.info("API succesfully stopped.")

    def add_service(self: APIServer, service) -> None:
        if service.name in self.services:
            raise DuplicateService(f"Service with name: {service.name} already exists")

        self.services[service.name] = service
        logging.info(f"Service with name: {service.name} has been added.")

    def _register_routes(self: APIServer) -> None:
        register_routes(self.app, self.services)

class DuplicateService(Exception):
    pass