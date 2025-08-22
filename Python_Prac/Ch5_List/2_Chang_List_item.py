#Example 1 we change the value at index 2 of the given list.
list1=[1,2,3,4,5,6,7]
print("Orignal List: ",list1)
#changing the index 2 value with 8
list1[2]=8
print("List after changing value at index 2:",list1)#[1, 2, 8, 4, 5, 6, 7]

#Example 2  items at index 0 and 2 are replaced by items in another sublist.
name=['S','H','a','r','y']
print("orignal list: ",name)
list2=['s','h']
name[0:2]=list2
print("list after changing with sublist: ",name)# ['s', 'h', 'a', 'r', 'y']  

#Example 3
"""If the source sublist has more items than the slice to be replaced, 
the extra items in the source will be inserted. Take a look at the following code"""
num1=[1,2,3,7,8,9]
print("orignal string: ",num1)
num2=[4,5,6]
num1[3:4]=num2
print('list after changing with sublist: ',num1)#[1, 2, 3, 4, 5, 6, 8, 9]

#Example 4

"""
If the sublist with which a slice of original list is to be replaced, has lesser items,
the items with match will be replaced and rest of the items in original list will be removed."""

list3=['a','b','c','d']
print("Orignal list: ",list3)
list3[1:3]='X'
print("list after changing b and c with X:",list3)