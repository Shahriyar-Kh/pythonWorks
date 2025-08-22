#Example 1 First method
import array as ary
a=ary.array('i',[1,2,3,4,5])
b=ary.array('i',[6,7,8,9]) 
"""Run a for loop on the array "b". Fetch each number from "b" and append it to array "a" with the following loop statement −"""
for i in range(len(b)):
    a.append(b[i])
print("The two array are join(append): ",a)

#Example 2 Second Method
"""Using another method to join two arrays, first convert arrays to list objects −"""
a1=a.tolist()
b1=b.tolist()
c=a1+b1
result=ary.array('i')
result.fromlist(c)
print("joined array(tolist): ",result)

#Example 3 Third Method
"""
We can also use the extend() method from the List class to append elements from one list to another.
First, convert the array to a list and then call the extend() method to merge the two lists −"""

a.extend(b)
print("Extended array: ",a)