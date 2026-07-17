import logging

logging = logging.getLogger(__name__)

def register_routes(api, services):
    @api.get("/")
    async def root():
        return { "message": "Hello, world!" }
    
    logging.info("Routes succesfully registered.")