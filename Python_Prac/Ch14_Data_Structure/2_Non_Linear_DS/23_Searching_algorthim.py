#Example 1 Linear Search
# Print a header indicating that the following code is an example of Linear Search
print("\n\n********************** Linear Search ************************************")

# Define a function called Linear_Search that takes two parameters:
# - list_Values: a list of values to search through
# - Search_key: the value to search for in the list
def Linear_Search(list_Values, Search_key):
    # Initialize a variable to keep track of the index being searched
    search_at = 0
    # Initialize a variable to store the search result, initially set to False
    search_result = False
    
    # Start a loop that continues as long as the search index is less than the length of the list
    # and the search result is False
    while search_at < len(list_Values) and search_result is False:
        # Check if the value at the current index matches the search key
        if list_Values[search_at] == Search_key:
            # If a match is found, set the search result to True
            search_result = True
        else:
            # If no match is found, move to the next index by incrementing search_at
            search_at += 1  # increment index
    
    # Return the final search result (True if the value was found, False otherwise)
    return search_result

# Create a list of values
list = [64, 34, 25, 12, 22, 11, 90]

# Call the Linear_Search function to search for the value 12 in the list
# and print the result (True if found, False if not found)
print(Linear_Search(list, 12))

# Call the Linear_Search function to search for the value 10 in the list
# and print the result (True if found, False if not found)
print(Linear_Search(list, 10))


#Example 2 
print("\n\n*********************** Interploation Search ****************************")
"""
There is a specific formula to calculate the middle position which is indicated in the program below −
"""

def Interploation_Search(list_Values, key):
    # Initialize start and end indices for the search range
    start_idx = 0
    end_idx = len(list_Values) - 1

    # Perform interpolation search as long as start index is less than or equal to end index
    # and the search key is within the range of values in the list
    while start_idx <= end_idx and key >= list_Values[start_idx] and key <= list_Values[end_idx]:
        # Calculate the mid-point using interpolation formula
        mid = start_idx + int((float(end_idx - start_idx) / (list_Values[end_idx] - list_Values[start_idx])) * (key - list_Values[start_idx]))

        # Check if the key is found at the mid-point
        if key == list_Values[mid]:
            return "Searched element " + str(key) + " found at index: " + str(mid)
        # If key is greater than the value at mid-point, update start index
        elif key > list_Values[mid]:
            start_idx = mid + 1
        # If key is smaller than the value at mid-point, update end index
        else:
            end_idx = mid - 1
    
    # If key is not found in the list, return a message indicating that
    return "Searched element " + str(key) + " not found in the list"

# Create a list of values
list = [2, 6, 11, 19, 27, 31, 45, 121]

# Perform interpolation search for key 50 in the list and print the result
print(Interploation_Search(list, 50))

# Perform interpolation search for key 31 in the list and print the result
print(Interploation_Search(list, 31))
