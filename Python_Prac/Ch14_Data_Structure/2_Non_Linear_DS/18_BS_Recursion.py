class BS:
    def __init__(self, left, right, list1):
        # Initialize the Binary Search object with left and right pointers and the list to search
        self.list = list1  # Assign the provided list to the instance variable
        self.left = left  # Initialize the left pointer
        self.right = right  # Initialize the right pointer

    def BSearch(self, key):
        # Perform binary search to find the index of the key in the list
        if self.left <= self.right:  # Check if left pointer is less than or equal to right pointer
            midValue = (self.left + self.right) // 2  # Calculate the middle index
            if key == self.list[midValue]:  # If key is found at middle index
                return midValue  # Return the index of the key
            elif key < self.list[midValue]:  # If key is less than value at middle index
                # Recursively search the left half of the list
                return BS(self.left, midValue - 1, self.list).BSearch(key)
            else:  # If key is greater than value at middle index
                # Recursively search the right half of the list
                return BS(midValue + 1, self.right, self.list).BSearch(key)
        else:
            return None  # Return None if key is not found after the search

list1 = [8, 11, 24, 56, 88, 131]  # Define the sorted list
obj = BS(0, 5, list1)  # Create an object of the BS class with left pointer, right pointer, and the list
n = int(input("Enter the key value: "))  # Prompt the user to enter the key to search for
result = obj.BSearch(n)  # Call the BSearch method to search for the key in the list
if result is not None:  # If key is found in the list
    print(f"{n} found at index: ", result)  # Print the index where key is found
else:  # If key is not found in the list
    print(f"{n} not found!")  # Print a message indicating key is not found
