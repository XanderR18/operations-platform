import logging
from .application import Application, InvalidStateTransition

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
    logging.info("Starting application...")
    try:
        application.start()
        logging.info("Application succesfully started.\n")
    except InvalidStateTransition as e:
        logging.error(f"Application failed to start:\n {e}\n")

    # Shutdown application
    logging.info("Stopping application...")
    try:
        application.stop()
        logging.info("Application succesfully stopped.\n")
    except InvalidStateTransition as e:
        logging.error(f"Application failed to stop:\n {e}\n")

if __name__ == "__main__":
    main()
