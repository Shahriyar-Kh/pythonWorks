#Example 1 creating set
set1=set([1,2,3,3,"Shary","Khan"])
set2={1,2,3,'umair','hamad'}
print(set1)
print(set2)

#Example 2 Accessing Values in a Set
"""
We cannot access individual values in a set. We can only access all the elements together as shown above. But we can also get a list of individual elements by looping through the set."""
#print(set1[2]) not working index
for i in set1:
    print(i)

#Example 3 Adding Items to a Set
"""
We can add elements to a set by using add() method. Again as discussed there is no specific index attached to the newly added element."""

set1.add('Ali')
print(set1)

#Example4 Removing Item from a Set
"""
We can remove elements from a set by using discard() method. Again as discussed there is no specific index attached to the newly added element"""

set1.discard('Ali')
print(set1)

#Example 5 Union of Sets
"""
The union operation on two sets produces a new set containing all the distinct elements from both the sets. """

newSet=set1|set2
print(newSet)

#Example 6 Intersection of Sets
"""
The intersection operation on two sets produces a new set containing only the common elements from both the sets."""

result=set1&set2
print(result)

#Example 7 Difference of Sets
"""
The difference operation on two sets produces a new set containing only the elements from the first set and none from the second set."""
result2=set1-set2
print(result2)

#Example Compare Sets
"""
We can check if a given set is a subset or superset of another set. The result is True or False depending on the elements present in the sets.
"""
set3={1,2,'Khan'}
supset=set1>=set3
print(supset)