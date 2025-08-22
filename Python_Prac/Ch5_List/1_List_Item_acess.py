# 5.1 Access List Items

#Example 1
list1=["Shary","Umair",1,2,3,4,6.7]
list2=[1,2,3,4,5]
print("Item at index1 in list1: ",list1[1])#umair
print("Item at index4 in list2: ",list1[4])#3

#Example 2 Python allows negative index to be used with any sequence type. The "-1" index refers to the last item in the list.

print("item at index 0 in list1:",list1[-1])#6.7
print("item at index 0 in list2:",list1[-3])#3

#Example 3 Slicing 
"""The slice operator extracts a sublist from the original list."""
print("item from index 0 to 2 :",list1[0:3])#Shary and umair
print("item from index 4 to -1 :",list2[3:-1])#4 

#Example 4 
print("items from start 1 to end in list1: ",list1[1:])
print("items from index 0 to 2 in list2: ",list2[:3])#1 2 3

