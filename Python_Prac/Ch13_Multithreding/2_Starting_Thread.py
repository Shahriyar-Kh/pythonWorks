# Example 1
import threading  # Import the threading module for working with threads
import time       # Import the time module for time-related functions

# Define a function for the thread
def mythread(threadName, delay):
    for count in range(1, 6):
        time.sleep(delay)
        print("Thread name: {} count: {}".format(threadName, count))

# Create thread instances
thread1 = threading.Thread(target=mythread, args=("Thread1", 2))
thread2 = threading.Thread(target=mythread, args=("Thread2", 4))

# Start the threads
thread1.start()
thread2.start()

# Wait for threads to finish using the join method
thread1.join()
thread2.join()

# Main thread continues execution...
print("Main thread continues......")
