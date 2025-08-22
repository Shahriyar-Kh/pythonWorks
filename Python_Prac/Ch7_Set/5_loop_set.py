#Example 1
langs={'C','C++','C#',"Python","java"}
for i in langs:
    print(i)
    
#Example 2
"""
The following example shows how you can run a for loop over the elements of one set, and use the add() method of set class to add in another set."""

s1={1,2,3,4,5}
s2={5,6,7,8,9}
for i in s2:
    s1.add(i)
print("Added two Sets: ",s1)   

 