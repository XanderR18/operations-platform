from application import Application
import logging

def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s"
    )

    # Initalize application
    logging.info("Initializing Operations Platform Application...")
    try:
        application = Application()
        logging.info("Application successfully initialized.\n")
    except Exception as e:
        logging.error(f"Application failed to initialize:\n {e}\n")

    # Start application
    logging.info("Starting application...")
    try:
        application.start()
        logging.info("Application succesfully started.\n")
    except Exception as e:
        logging.error(f"Application failed to start:\n {e}\n")

    # Shutdown application
    logging.info("Shutting down application...")
    try:
        application.shutdown()
        logging.info("Application succesfully shutdown.\n")
    except Exception as e:
        logging.error(f"Application failed to shut down:\n {e}\n")

if __name__ == "__main__":
    main()
