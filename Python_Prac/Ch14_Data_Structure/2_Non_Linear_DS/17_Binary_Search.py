print("\n\n***************** Binary Search ***********************")
class BSearch:
    def __init__(self, list1):
        # Initialize the Binary Search object with a sorted list
        self.list = list1  # Assign the provided list to the instance variable
        self.left = 0  # Initialize the left pointer to the start index of the list
        self.right = len(self.list) - 1  # Initialize the right pointer to the end index of the list
    
    def bSearch(self, key):
        # Perform binary search to find the index of the key in the list
        while self.left <= self.right:
            midValue = (self.left + self.right) // 2  # Calculate the middle index
            if self.list[midValue] == key:
                # If the key is found at the middle index, return the index
                return midValue
            elif key > self.list[midValue]:
                # If the key is greater than the value at the middle index, update the left pointer
                self.left = midValue + 1
            else:
                # If the key is less than the value at the middle index, update the right pointer
                self.right = midValue - 1
        return None  # Return None if the key is not found in the list after the loop ends
        
list1 = [2, 7, 19, 34, 53, 72]

obj = BSearch(list1)  # Create an object of the BSearch class with the list
n = int(input("Enter the key: "))  # Prompt the user to enter the key to search for

# Call the bSearch method to search for the key in the list
result = obj.bSearch(n)

# Check if the key is found in the list and print the result accordingly
if n in list1:
    print(f"{n} Found at index:", result)
else:
    print(f"{n} Not Found!")
