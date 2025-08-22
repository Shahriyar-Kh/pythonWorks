#Example 1
"""
Now let's take a look at some examples to understand how we can sort lists in Python 
−"""
list1=['Physics','Biology','chemistry','maths']
print("List before sort: ",list1)
list1.sort()
print("List after sorted list: ",list1)

list2=[10,16,9,5,24]
print("List before sort: ",list2)
list2.sort()
print("List after sorted : ",list2)

#Example 2
"""
the str.lower() method is used as key parameter in sort() method.
"""
list3=["shahriyar","Ali","Muhammad","Umair","Hamsafer"]
print("Orignal list: ",list3)
list3.sort(key=str.lower)
print("list after sorted: ",list3)

#Example 3
"""
The myfunction() uses % operator to return the remainder, 
based on which the sort is done."""

def myfunction(x):
    result=x%10
    return result
list4=[23,17,46,51,90]
print("Orignal list: ",list4)
list4.sort(key=myfunction)
print("Sorted list: ",list4)

