# Import necessary modules
from time import sleep
from threading import current_thread, Thread
import threading

# Function to be executed by the new thread
def run():
    # Get the current thread
    thread = current_thread()
    
    # Is it a daemon thread?
    print(f"Daemon thread: {thread.daemon}")

# Create a new thread using the Thread class, targeting the 'run' function
thread = Thread(target=run)

# Start the new thread
thread.start()

# Block the main thread for 0.5 seconds
sleep(0.5)

# Output:
# Daemon thread: False

# Create a non-daemon thread explicitly
t1 = threading.Thread(target=run)
# This statement creates a non-daemon thread. When started, it calls the run() method.
