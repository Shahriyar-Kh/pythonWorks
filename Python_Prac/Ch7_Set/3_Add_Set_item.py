#Example
langs={"C",'C+','Java','Python'}
print("Orignal set: ",langs)
langs.add("Php")
print("Modify Set: ",langs)

#update() Method
"""
The update() method of set class includes the items of the set given as argument. 
If elements in the other set has one or more items that are already existing, 
they will not be included."""

#Example 2
lang2={'Perl','Pascal','C+'}
langs.update(lang2)
print("Update Set: ",langs)

#Example 3
"""
The update() method also accepts any sequence object as argument. Here, 
a tuple is the argument for update() method."""

t1=(1,2,3)
langs.update(t1)
print(langs)

#Example 4 
"""
Example
In this example, a set is constructed from a string, and another string is used as argument for update() method.
"""
set1=set("Hello")
set1.update("World")
print("From string to set: ",set1)

#union() Method
"""The union() method of set class also combines the unique items from two sets, but it returns a new set object."""
langs3=langs.union(lang2)
print("Union of two sets: ",langs3)

#Example
""" a set is constructed from a string, and another string is used as argument for union() method."""

set3=(set("Hello"))
set3.union("World")
print(set3)