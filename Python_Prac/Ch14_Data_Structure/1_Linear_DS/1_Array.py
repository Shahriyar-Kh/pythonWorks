#Example1 Create Array
from array import*
array1=array('i',[10,20,30,40,50])
for i in array1:
    print(i)

#Example 2 Accessing Array element
print("\nAccessing arrya Items:",array1[0])
print(array1[1])
print(array1[2])
print(array1[3])
print(array1[4])

#Example 3 Insetion 
"""
Insert operation is to insert one or more data elements into an array. 
Based on the requirement, 
a new element can be added at the beginning, end, or any given index of array.
    """
print("\n Insert 60 into specifice index(1):")
array1.insert(1,60)
for i in array1:
    print(i)
    
#Example 4 Deletion
"""
Deletion refers to removing an existing element from the array and re-organizing all elements of an array.
    """
print("\n Item 60 remove from array: ")
array1.remove(60)
for i in array1:
    print(i)

#Example 5 Search Operation
"""
You can perform a search for an array element based on its value or its index.
Here, we search a data element using the python in-built index() method.
"""
print("\nIndex of 20 is:",array1.index(20))

#Example 6 Update Operation
"""
Update operation refers to updating an existing element from the array at a given index.
Here, we simply reassign a new value to the desired index we want to update."""

array1[4]=45
print("Update last item in array:")
for i in array1:
    print(i)

