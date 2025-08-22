#Example 1
d1={"D":"Database","H":"HCI","J":"Java","P":"Python"}
print("Dict1: ",d1)
#remove items
del d1["H"]
print("After removing items from d1:\n ",d1)
#remove full dict
# del d1
# print("After removes d1: ",d1)

#Using pop() Method
"""The pop() method of dict class causes an element with the specified key to be removed from the dictionary."""
v1=d1.pop("J")
print("Remove item key J: ",v1)
#Return value The pop() method returns the value of the specified key after removing the key-value pair.


#Using popitem() Method
"""
The popitem() method in dict() class doesn't take any argument. It pops out the last inserted key-value pair, and returns the same as a tuple"""
v2=d1.popitem()
print("d1 dict After pop op:  ",d1)
print("value Poped:  ",v2)

#Add some items
d1.update(DS="Data Scienc",Op="Operating system")
print("UPdate d1: \n",d1)

#Using clear() Method
"""
The clear() method in dict class removes all the elements from the dictionary object and returns an empty object."""
d1.clear()
print("After clear the d1: ",d1)