#Using the "|" Operator
"""
The "|" symbol (pipe) is defined as the union operator. It performs the A∪B operation and returns a set of items in A, B or both. 
Set doesn't allow duplicate items."""

s1={1,2,2,2,3,4,5,6}
s2={6,7,8,9}
s3=s1|s2
print("The Union of two sets: ",s3)

#Using the union() Method
"""
The set class has union() method that performs the same operation as | operator. It returns a set object that holds all items in both sets, discarding duplicates."""

s4=s1.union(s2)
print("The Union of two sets(u): ",s4)

#Using the update() Method
"""The update() method also joins the two sets, as the union() method. 
However it doen't return a new set object. 
Instead, the elements of second set are added in first, 
duplicates not allowed."""

s1.update(s2)
print("The updated set: ",s1)

#Using the unpacking Operator
"""the "*" symbol is used as unpacking operator. The unpacking operator internally assign each element in a collection to a separate variable."""
s11={1,2}
s5=*s11,*s2
print("Unpacked sets: ",s5)
