def register_routes(api, services):
    @api.get("/")
    async def root():
        return { "message": "Hello, world!" }