tuple1=(10,20,30,40)
tuple2=("one","two","Three","Four")
t3=tuple1+tuple2
print("Joined tuple: ",t3)

#Example 2 You can also use the augmented concatenation operator with the "+=" symbol to append T2 to T1

tuple1+=tuple2

#Example 3
"""
The same result can be obtained by using the extend() method. 
Here, we need cast the two tuple objects to lists, 
extend so as to add elements from one list to another, 
and convert the joined list back to a tuple."""

#Convert to list
l1=list(tuple1)
l2=list(tuple2)
l1.extend(l2)
tResult=tuple(l1)
print("The Extended tuple: ",tResult)

#Example 4 Python's built-in sum() function also helps in concatenating tuples. We use an expression
t1=(1,2,3)
t2=("a","b")
t3=sum((t1,t2),())
print("Joined tuple: ",t3)

#Example 5 A slightly complex approach for merging two tuples is using list comprehension

#convert to list
l1,l2=list(t1),list(t2)
#using list comprehension
l3=[y for x in [l1,l2] for y in x]
t3=tuple(l3)
print("Joined tuple (list comprehension): ",t3)

#Example 6 You can run a for loop on the items in second loop, convert each item in a single item tuple and concatenate it to first tuple with the "+=" operator

for i in t2:
    t1+=(i,)
print("joined tuple(for loop): ",t1)

