import logging
from .server import APIServer

logging = logging.getLogger(__name__)

def register_routes(api: APIServer, services) -> None:
    @api.get("/")
    async def root():
        return { "message": "Hello, world!" }
    
    logging.info("Routes succesfully registered.")