import logging
import uvicorn
from .models.application import Application, InvalidStateTransition

def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s"
    )

    # Initalize application
    logging.info("Initializing Operations Platform Application...")
    application = Application()
    logging.info("Application successfully initialized.\n")

    # Start application
    try:
        application.start()
    except InvalidStateTransition as e:
        logging.error(f"Application failed to start:\n {e}\n")

    # Start Uvicorn for testing. Temporary location
    logging.info("Starting Uvicorn..")
    uvicorn.run(
        application.api_server.app,
        host="127.0.0.1",
        port=8000
    )

    # Stop application
    try:
        application.stop()
    except InvalidStateTransition as e:
        logging.error(f"Application failed to stop:\n {e}\n")

if __name__ == "__main__":
    main()
