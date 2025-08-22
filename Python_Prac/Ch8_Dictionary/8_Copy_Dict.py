#Example 1
"""
In this example, we have a dictionary "d1" and we assign it to another variable "d2". If "d1" is updated, the changes also reflect in "d2"""

d1={"a":11,"b":22,"c":33}
d2=d1
print("id: ",id(d1),"dict: ",d1)
print("id: ",id(d2),"dict: ",d2)

d1["d"]=100
print("id: ",id(d1),"dict: ",d1)
print("id: ",id(d2),"dict: ",d2)

#Example 2
"""To avoid this, and make a shallow copy of a dictionary, use the copy() method instead of assignment."""
print("\n\n")
d3=d1.copy()
print("\nid: ",id(d1),"dict: ",d1)
print("id: ",id(d3),"dict: ",d3)

d1["E"]=120
print("\nid: ",id(d1),"dict: ",d1)
print("id: ",id(d3),"dict: ",d3)
"""
Output
When "d1" is updated, "d2" will not change now because "d2" is the copy of dictionary object,
not merely a reference.
"""

