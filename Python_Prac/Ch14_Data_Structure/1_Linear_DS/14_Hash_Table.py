#Example 1 Accessing Values in Dictionary
"""
To access dictionary elements, you can use the familiar square brackets along with the key to obtain its value"""

#decalre dict
d1={"name":"Shary","Age":26,"Class":"BSSE"}

#Access dict with keys
print("d1[Name]:",d1["name"])
print("d1[Age]:",d1["Age"])
print("D1:\n",d1)
#Example 2 Updating Dictionary
"""
You can update a dictionary by adding a new entry or a key-value pair, modifying an existing entry, or deleting an existing entry as shown below in the simple example −"""

#change the age 
d1["Age"]=20

#Add new value with key
d1["Marks"]=400

print("d1[Marks]:",d1["Marks"])
print("d1[Age]:",d1["Age"])
print("\nAfter Update:",d1)
#Example 3 Delete Dictionary Elements

"""
You can either remove individual dictionary elements or clear the entire contents of a dictionary. You can also delete entire dictionary in a single operation.To explicitly remove an entire dictionary, just use the del statement."""

#Remove entry key with value
del d1["Class"]
print("\nAfter delete item:",d1)

#Remove all entries
d1.clear()
print("\n After clear all elements: ",d1)

#Delete entire dict
del d1