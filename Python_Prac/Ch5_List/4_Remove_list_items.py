#Using the remove method 
# shows how you can use the remove() method to remove list items −

list1=["Shary","khan",1,2,3,4.5]
print("Orignal string: ",list1)
#remove is use for given specific item delete 
list1.remove('khan')
print("List after removing : ",list1)

#Using the pop() Method
"""
shows how you can use the pop() method to remove list items −
"""
print("\Origna string :",list1)
#pop using index
list1.pop(2)
print("List after popping index 2: ",list1)

#Using the "del" Keyword
""" Python has the "del" keyword that deletes any Python object from the memory."""
print("Orignal string: ",list1)
#del to delete the list items
del list1[0]
print("List after delating item at index 0: ",list1)

#we can also delete sreies of items like slicing
del list1[0:2]
print("List after delete item from index 0 to 2 : ",list1)