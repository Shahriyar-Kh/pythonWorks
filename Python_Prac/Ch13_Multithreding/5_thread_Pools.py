from concurrent.futures import ThreadPoolExecutor  # Import ThreadPoolExecutor for concurrent execution
from time import sleep  # Import the sleep function for introducing delays

# Define a function to calculate the square of numbers
def squar(num):
    for value in num:
        result = pow(value, 2)  # Calculate the square for each individual number using the pow() function
        sleep(1)  # Simulate some processing time (1 second sleep)
        print("Number: {} Square:{}".format(value, result))  # Print the result

# Define a function to calculate the cube of numbers
def cube(num):
    for value in num:
        result = pow(value, 3)  # Calculate the cube for each individual number using the pow() function
        sleep(1)  # Simulate some processing time (1 second sleep)
        print("Number: {} Cube:{}".format(value, result))  # Print the result

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]  # List of numbers
    executer = ThreadPoolExecutor(4)  # Create a ThreadPoolExecutor with 4 threads

    # Submit the squar function to the thread pool with numbers as an argument
    thread1 = executer.submit(squar, (numbers))
    
    # Submit the cube function to the thread pool with numbers as an argument
    thread2 = executer.submit(cube, (numbers))

    # Print whether Thread 1 and Thread 2 have completed their execution
    print("Thread 1 executed?:", thread1.done())
    print("Thread 2 executed?:", thread2.done())

    sleep(2)  # Sleep for 2 seconds to allow threads to run

    # Print whether Thread 1 and Thread 2 have completed their execution after 2 seconds
    print("Thread 1 executed?:", thread1.done())
    print("Thread 2 executed?:", thread2.done())
