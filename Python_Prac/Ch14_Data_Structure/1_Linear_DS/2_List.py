#Example 1 Accessing Values
"""
To access values in lists, use the square brackets for slicing along with the index or indices to obtain value available at that index.
"""
list1=[1,2,3,4,5]
list2=["A","B","C",5,6,7]
print('List1 first item:',list1[0])
print('List2 first item:',list2[0])

#Example 2 Updating Lists
"""
You can update single or multiple elements of lists by giving the slice on the left-hand side of the assignment operator, and you can add to elements in a list with the append() method."""
print("\nAfter update list1:",list1)
list1[4]=55
print("Update last item:",list1)

#Example 3 Delete List Elements
"""
To remove a list element, you can use either the del statement if you know exactly which element(s) you are deleting or the remove() method if you do not know."""
del list1[4]
print("\nAfter delete last1 item:",list1)

#Example 4 Basic List Operations
"""
Lists respond to the + and * operators much like strings; they mean concatenation and repetition here too, except that the result is a new list, not a string."""
print("\nLength of list1:",len(list1))
print("\nConcatenation of two lists:",list1+list2)
print("\nRepetition of string:",("Shary")*3)

