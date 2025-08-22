#Example 1
capital={"Kpk":"Peshawer","Pakistan":"Islamabad","Punjab":"Lahore","Sindh":"Karachi"}
print("Capital of pakistan: ",capital["Pakistan"])
print("Capital of Punjab: ",capital["Sindh"])

#Using the get() Method
"""The get() method in Python's dict class returns the value mapped to the given key."""
print("Capital of Punjab: ",capital.get("Punjab"))

"""The get() method accepts an optional string argument. If it is given, and if the key is not found, 
this string becomes the return value."""
print("Capital of Kashmir: ",capital.get("Kashmir","Not found"))




