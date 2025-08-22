#Example 1 Boble Sort

count=0  # Initialize a counter variable for iterations
def BobleSort(list1):
    global count
    count=0
    # Loop for iteration
    for i in range(len(list1)):
        swapped=False
        # Loop for comparing elements
        for j in range(0, len(list1) - i - 1):
            # Compare adjacent elements
            if list1[j] > list1[j + 1]:
                # Swap if the current element is greater than the next element
                list1[j],list1[j+1]=list1[j+1],list1[j]
                # temp = list1[j]
                # list1[j] = list1[j + 1]
                # list1[j + 1] = temp
                count += 1  # Increment the counter after each iteration of the outer loop
                swapped=True
    # no swapping means the array is already sorted
    # so no need for further comparison
        if not swapped:
            break
list1 = [-2, 45, 0, 11, -9]
BobleSort(list1)  # Call the Bubble Sort function
# Print the sorted list in ascending order
print(f"Sorted list in Ascending order:", list1)
# Print the number of iterations performed during sorting
print(f"Number of iterations:", count)


#EXample 2 Merged Sort
print("\n\n************************ Merge Sort *************************************")

def Merge_Sort(unsorted_list):
    # Base case: if the length of the list is 1 or less, it's already sorted
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    # Find the middle point and divide the list into two halves
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]  # Left half of the list
    right_list = unsorted_list[middle:]  # Right half of the list

    # Recursively call Merge_Sort on each half of the list
    left_list = Merge_Sort(left_list)
    right_list = Merge_Sort(right_list)

    # Merge the sorted halves using the merge function
    return list(merge(left_list, right_list))

def merge(left_list, right_list):
    result = []  # Initialize an empty list to store the merged result
    # Loop until either left_list or right_list becomes empty
    while len(left_list) != 0 and len(right_list) != 0:
        # Compare the first elements of left_list and right_list
        if left_list[0] < right_list[0]:
            # If the first element of left_list is smaller, append it to result
            result.append(left_list[0])
            # Remove the first element from left_list
            left_list.remove(left_list[0])
        else:
            # If the first element of right_list is smaller, append it to result
            result.append(right_list[0])
            # Remove the first element from right_list
            right_list.remove(right_list[0])

    # Add the remaining elements of left_list and right_list to result
    if len(left_list) == 0:
        result += right_list
    else:
        result += left_list

    return result  # Return the merged result

unsorted_list = [64, 34, 25, 12, 11, 90]
# Call Merge_Sort function to sort the unsorted_list
print("Sorted list After Merge Sort:", Merge_Sort(unsorted_list))

#Example 3 Insertion Sort
print("\n\n*************************** Insertion Sort **************************")

def insertion_Sort(input_list):
    # Iterate over each element in the input_list, starting from the second element
    for i in range(1, len(input_list)):
        next_item = input_list[i]  # Store the current element to be compared and inserted
        j = i - 1  # Start comparing with the previous element

        # Compare the current element with the previous ones and shift them if necessary
        while j >= 0 and input_list[j] > next_item:
            input_list[j + 1] = input_list[j]  # Shift the element to the right
            j -= 1  # Move to the previous element
        input_list[j + 1] = next_item  # Insert the current element at its correct position

    return input_list  # Return the sorted list

# Create a list to be sorted using insertion sort
input_list = [19, 2, 31, 45, 30, 11, 121, 27]
# Call the insertion_Sort function to sort the input_list
sorted_list = insertion_Sort(input_list.copy())  # Use copy to avoid modifying the original list
print("Sorted list After insertion sort:", sorted_list)  # Print the sorted list


#Example 4 Shell Sort
print("\n\n************************ Shell Sort ******************************")

def Shell_Sort(input_list):
    # Initialize the gap size to half the length of the input list
    gap = len(input_list) // 2
    
    # Iterate until the gap becomes 0
    while gap > 0:
        # Perform insertion sort for elements at each gap interval
        for i in range(gap, len(input_list)):
            temp = input_list[i]  # Store the current element to be compared and inserted
            j = i  # Start comparing with the previous elements at the specified gap
            
            # Compare the current element with the elements at a gap distance and shift them if necessary
            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]  # Shift the element to the right by the gap
                j -= gap  # Move to the previous element at the specified gap
                
            input_list[j] = temp  # Insert the current element at its correct position
            
        # Reduce the gap for the next iteration
        gap = gap // 2

# Create a list to be sorted using shell sort
input_list = [19, 2, 31, 45, 30, 11, 121, 27]
Shell_Sort(input_list)  # Call the Shell_Sort function to sort the input_list
print("Sorted list after shell sort:", input_list)  # Print the sorted list

#Example 5 Selection Sort
print("\n\n************************** Selection Sort *****************************")

def Selection_sort(input_list):
    # Iterate over each index of the input_list
    for current_idx in range(len(input_list)):
        min_idx = current_idx  # Assume the current index as the minimum index

        # Iterate over the unsorted part of the list to find the minimum value
        for jth_idx in range(current_idx + 1, len(input_list)):
            # Check if the value at the min_idx is greater than the value at jth_idx
            if input_list[min_idx] > input_list[jth_idx]:
                min_idx = jth_idx  # Update the minimum index to the index of the smaller value

        # Swap the minimum value with the value at the current index
        input_list[current_idx], input_list[min_idx] = input_list[min_idx], input_list[current_idx]

# Define a list to be sorted using selection sort
list = [19, 2, 31, 45, 30, 11, 121, 27]
# Call the Selection_sort function to sort the list
Selection_sort(list)
# Print the sorted list
print("Sorted list after selection sort:", list)
