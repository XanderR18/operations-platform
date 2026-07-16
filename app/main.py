from application import Application

def main():
    # Initalize application
    print("[INFO] Initializing Operations Platform Application...")
    try:
        application = Application()
        print("[INFO] Application successfully initialized.")
    except Exception as e:
        print(f"[ERROR] Application failed to initialize:\n {e}")

    # Start application
    print("[INFO] Starting application...")
    try:
        application.start()
        print("[INFO] Application succesfully started.")
    except Exception as e:
        print(f"[ERROR] Application failed to start:\n {e}")

    # Shutdown application
    print("[INFO] Shutting down application...")
    try:
        application.shutdown()
        print("[INFO] Application succesfully shutdown.")
    except Exception as e:
        print(f"[ERROR] Application failed to shut down:\n {e}")

if __name__ == "__main__":
    main()
