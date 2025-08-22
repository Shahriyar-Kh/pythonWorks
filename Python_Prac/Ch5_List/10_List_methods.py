#Example 1 clear() methods  clears only contents of list not removed from memory
# Removes all elements from the list, making it empty.
list=[1,2,3,4,5]
print("before clear list: ",list)
list.clear()
print("After clear the list: ",list)

#del is used to delete list permanantly
del list
print("After delete the list: ",list)

#Example list count() method
list2=[4,3,5,2,3]
print("Count of 3: ",list2.count(3))

#Example list Extend method
list2.extend(["Khan","Ali"])
print("After extended the list: ",list2)

#Example list index() method
print("First index of 'Khan': ",list2.index('Khan'))

#Example list insert() method  
# insert using for specific index insertion
list2.insert(0,'Fahad')
print("After inserted list: ",list2)

#Example list pop()  Removes the element at the specified index (or the last element if no index is provided) and returns it.

print("Popped list: ",list2.pop(0))
print(list2)

#Example list append() 
# Appends a single element at the end of the list.
list2.append(33)
print("Appended list: ",list2)

#Example list Extend()   multple elements from another list append
list2.extend([44,55,66])
print("Extended List: ",list2)

#Example list remove() method  
#Removes the first occurrence of a specified value.  Removes the specified value from the list. Raises a ValueError if the value is not found.
print("Orignal list: ",list2)
list2.remove(3)
print("After first occurense removing from list: ",list2)

#Example list reverse() method
list2.reverse()
print("Reversed the list: ",list2)