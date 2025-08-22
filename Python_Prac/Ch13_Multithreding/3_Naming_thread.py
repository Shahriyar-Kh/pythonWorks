# Example 1
import threading  # Import the threading module for working with threads
import time       # Import the time module for time-related functions

class mythread(threading.Thread):  # Create a custom thread class that inherits from threading.Thread
    def __init__(self, name):  # Define the initialization method for the custom thread class
        threading.Thread.__init__(self)  # Call the initialization method of the parent class
        self.name = name  # Set the thread name attribute

    def run(self):  # Define the run method, which will be executed when the thread is started
        print("Starting " + self.name)
        for count in range(1, 6):
            time.sleep(5)
            print("Thread Name: {} Count: {}".format(self.name, count))
        print("Exiting " + self.name)

# Create new threads
thread1 = mythread("Thread1")
thread2 = mythread("Thread2")

# Start new threads
thread1.start()  # Start the first thread
thread2.start()  # Start the second thread

thread1.join()  # Wait for the first thread to finish
thread2.join()  # Wait for the second thread to finish

print("Exiting Main thread")  # Print a message indicating the main thread is exiting
