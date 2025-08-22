# # Example 1
# # Import necessary modules
# import _thread  # Module for creating and managing threads
# import time     # Module for time-related functions

# # Define a function for the thread
# def thread_Task(threadName, delay):
#     # Loop from 1 to 5
#     for count in range(1, 6):
#         # Pause execution for 'delay' seconds
#         time.sleep(delay)
#         # Print thread name and count
#         print("Thread name: {} count: {}".format(threadName, count))

# # Create two threads using the start_new_thread function
# try:
#     # Start the first thread, named "Thread-1", with a delay of 2 seconds
#     _thread.start_new_thread(thread_Task, ("Thread1", 0.5,))
    
#     # Start the second thread, named "Thread-2", with a delay of 4 seconds
#     _thread.start_new_thread(thread_Task, ("Thread2", 2,))
# except:
#     # Handle the case where thread creation fails
#     print("Error: unable to start thread")

# # Enter an infinite loop to keep the program running
# while True:
#     pass

# # Create thread instances
# thread3 = threading.Thread(target=thread_task, args=("Thread-3", 1))
# thread4 = threading.Thread(target=thread_task, args=("Thread-4", 2))

# # Start the threads
# thread3.start()
# thread4.start()

# """
# Thread name: Thread1 count: 1
# Thread name: Thread1 count: 2
# Thread name: Thread1 count: 3
# Thread name: Thread2 count: 1
# Thread name: Thread1 count: 4
# Thread name: Thread1 count: 5
# Thread name: Thread2 count: 2
# Thread name: Thread2 count: 3
# Thread name: Thread2 count: 4
# Thread name: Thread2 count: 5

#     """
