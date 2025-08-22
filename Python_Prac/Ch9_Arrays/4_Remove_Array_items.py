#Example 1
#array.remove() Method
"""
The remove() method removes the first occurrence of a given value from the array"""
import array as b
newArray=b.array('i',[1,2,3,4])
print("Orignal array: ",newArray)
newArray.remove(1)
print("After remove the item 1: ",newArray)

#Example 2
#array.pop() Method
"""
The pop() method removes an element at the specified index from the array, and returns the removed element."""
newArray.pop(2)#poped 4
print("after Poped element: ",newArray)

