import signal
import time
import sys

def graceful_shutdown(signum, frame):
    print(f"Received signal {signum}: Initiating graceful shutdown...")
    # Add your graceful shutdown logic here
    print("Graceful shutdown completed.")
    sys.exit(0)

def non_graceful_shutdown(signum, frame):
    print(f"Received signal {signum}: Initiating non-graceful shutdown...")
    # Add your non-graceful shutdown logic here
    print("Non-graceful shutdown completed.")
    sys.exit(1)

# Register signal handlers
signal.signal(signal.SIGTERM, graceful_shutdown)
signal.signal(signal.SIGINT, non_graceful_shutdown)  # SIGINT is Ctrl+C

# Your application logic
while True:
        print("Running...")
        time.sleep(1)
