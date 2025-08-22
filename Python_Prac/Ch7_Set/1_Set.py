#Example 1
s1={"Rohan","Physics",1,2,3,4.5}
s2={'a','b',True,-55,1+4j}
print(s1)
print(s2)

#set() Function 
"""
set() is one of the built-in functions. It takes any sequence object (list, tuple or string) as argument and returns a set object"""

l1=[1,2,4,5]
t1=('a','b','c')
s1="Shahriyar khan"
print(set(s1))
print(set(l1))
print(set(t1))

#Example 3
"""
Set is a collection of distinct objects. Even if you repeat an object in the collection,
only one copy is retained in it"""
s2={1,2,2,3,3,4,5}
print(s2)