from application import Application

def main():
    print("[INFO] Initializing Operations Platform Application...")

    try:
        application = Application()
        print("[INFO] Application successfully initialized")
    except Exception as e:
        print(f"[ERROR] Application failed to initialize: {e}")


if __name__ == "__main__":
    main()
