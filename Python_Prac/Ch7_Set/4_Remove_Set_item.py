#Example The intersection() method returns a set object, retaining only those items common in itself and obj.

s1={1,2,3,4,5}
s2={3,4,5,6,7}
s3=s1.intersection(s2)
print("S1: ",s1," S2: ",s2)
print("The common in two sets: ",s3)
s5=s2 & s1 
print("Common Item in two sets: ",s5)


#symmetric_difference_update() method
"""
The symmetric difference between two sets is the collection of all the uncommon items, rejecting the common elements. 
The symmetric_difference_update() method updates a set with 
symmetric difference between itself and the set given as argument.
"""

s1.symmetric_difference_update(s2)
print("S1 after running symmetric difference: ",s1)


#symmetric_difference() Method
"""
The symmetric_difference() method in set class is similar to symmetric_difference_update() method, 
except that it returns a new set object that holds all the items from two sets minus the common items."""

s4=s1.symmetric_difference(s2)
print("Symmetrics diff: ",s4)
#also worked ^
s6=s1^s2
print("Symmetrics diff(^): ",s6)





