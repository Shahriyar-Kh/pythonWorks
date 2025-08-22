#Example 1 
list1=[10,20]
print("list1: ",list1,"Id(list)",id(list1))
list2=list1 #same memeory address because only refrence
print("list2: ",list2,"Id(list)",id(list2))

"""As a result, if we update "lst", it will automatically reflect in "lst1". Change lst[0] to 100"""
list1[0]=100
print("list1: ",list1,"Id(list)",id(list1))
print("list2: ",list2,"Id(list)",id(list2))#Hence, we can say that "lst1" is not the physical copy of "lst".

#Using the Copy Method of List Class
"""
Python's list class has a copy() method to create a new physical copy of a list object."""

list3=[1,2,10,34]
list4=list3.copy()
print("List3 :",list3,"id(list3):",id(list3))
print("List4 :",list4,"id(list4):",id(list4))