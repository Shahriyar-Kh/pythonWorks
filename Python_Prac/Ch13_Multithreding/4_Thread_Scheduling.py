import sched               # Import the 'sched' module for event scheduling
import time                # Import the 'time' module for time-related functions

# Create a scheduler instance
scheduler = sched.scheduler(time.time, time.sleep)

# Define a function to be scheduled
def schedule_event(name, start):
    now = time.time()       # Get the current time
    elapsed = int(now - start)  # Calculate the elapsed time since the start time
    print('elapsed=', elapsed, 'name=', name)  # Print the elapsed time and the name of the scheduled event

# Record the start time
start = time.time()

# Print the start time
print('Start:', time.ctime(start))  # Print the start time in a human-readable format

# Schedule the first event to occur 2 seconds after the start time with a priority of 0.5
scheduler.enter(2, 3, schedule_event, ("Event1", start))

# Schedule the second event to occur 5 seconds after the start time with a priority of 3
scheduler.enter(3, 1, schedule_event, ("Event2", start))

# Run the scheduler, which will execute the scheduled events
scheduler.run()

"""
Output:
Start: Wed Jan  3 03:27:55 2024
elapsed= 2 name= Event1
elapsed= 3 name= Event2

    """
    
#Example 2
import sched                 # Import the 'sched' module for event scheduling
from datetime import datetime  # Import the 'datetime' module to work with dates and times
import time                   # Import the 'time' module for time-related functions

# Define a function 'addition' that performs addition and prints information about the operation
def addition(a, b):
    print("\nPerforming Addition: ", datetime.now())  # Print the current date and time
    print("Time: ", time.monotonic())  # Print the current monotonic time
    print("Results: ", a + b)  # Print the result of the addition operation

# Create a scheduler instance
s = sched.scheduler()

# Print the start time of the program
print("\nStart time: ", datetime.now())

# Schedule an event to perform the 'addition' function after 10 seconds with a priority of 1
event1 = s.enter(1, 1, addition, argument=(5, 6))
print("Event Created: ", event1)  # Print information about the created event

# Run the scheduler, which will execute the scheduled event
s.run()

# Print the end time of the program
print("End time:", datetime.now())
