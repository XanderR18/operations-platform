def register_routes(api):
    @api.get("/")
    async def root():
        return { "message": "Hello, world!" }