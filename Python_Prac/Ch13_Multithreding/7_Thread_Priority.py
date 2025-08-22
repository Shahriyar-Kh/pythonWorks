# Example 1
from time import sleep
from random import random, randint
from threading import Thread
from queue import PriorityQueue

# Create a PriorityQueue instance for thread-safe communication
queue = PriorityQueue()

# Producer function to add items to the queue
def producer(queue):
    print("Producer: Running")
    for i in range(5):
        # Generate a random value between 0 and 1
        value = random()

        # Generate a random priority between 0 and 5
        priority = randint(0, 5)

        # Create a tuple representing an item with priority and value
        item = (priority, value)

        # Put the item into the priority queue
        queue.put(item)
    # Wait for all items to be processed
    queue.join()
    # Add a sentinel item to signal the end of production
    queue.put(None)
    print("Producer: Done")

# Consumer function to process items from the queue
def consumer(queue):
    print("Consumer: Running")
    
    while True:
        # Get a unit of work (a tuple representing a priority-value pair)
        item = queue.get()
        if item is None:
            # Break the loop if the sentinel item is received
            break
        
        # Simulate processing time based on the value
        sleep(item[1])

        # Print the processed item
        print(item)

        # Signal that the unit of work is complete
        queue.task_done()
    print("Consumer: Done")

# Create a thread for the producer function
producer_thread = Thread(target=producer, args=(queue,))
producer_thread.start()

# Create a thread for the consumer function
consumer_thread = Thread(target=consumer, args=(queue,))
consumer_thread.start()

# Wait for the producer thread to complete
producer_thread.join()

# Wait for the consumer thread to complete
consumer_thread.join()
