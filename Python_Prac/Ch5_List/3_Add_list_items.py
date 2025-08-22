#Add list items
#Example 1  The append() method adds the item at the end of an existing list
list1=[1,2,3,4,5]
print("orignal list: ",list1)
list1.append(6)
print("list after appending: ",list1)#[1,2,3,4,5,6]

#Example 2 The insert() method inserts the item at a specified index in the list.

list2=["database","HCI",1,2,3,4]
print("Orignal list: ",list2)
list2.insert(2,"MAD")
print("List after inserting at index 2 :",list2)
list2.insert(-1,"English")
print("List after inserting at index 4 :",list2)

