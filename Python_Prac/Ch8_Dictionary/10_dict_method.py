#EXample 1 clear()
dict = {'Name': 'Zara', 'Age': 7};
print ("Start Len : %d" % len(dict))
dict.clear()
print("End len: %d"% len(dict))

#Example 2 method fromkeys()

"""
Python dictionary method fromkeys() creates a new dictionary 
with keys from seq and values set to value.
"""



#Example 3 method get()
"""Python dictionary method get() returns a value for the given key. If key is not available then returns default value None"""
dict1 = {'Name': 'Zara', 'Age': 7};
print("\nValue :%d " % dict1.get("Age"))
print("\nValue :%s " % dict1.get("Shary","No here"))

#Example 4  dict.has_key(key) method
"""
Returns true if a given key is available in the dictionary, otherwise it returns a false."""
#not working .has_key method for this condition use in op
print("\nValue :%s" % ('Age' in dict1))

#Example5 dict.items() method
#Returns a list of dict's (key, value) tuple pairs."""

print("Return a list of dict(key,value) tuple pairs: \n",dict1.items())

#Example 6 dict.keys() Returns list of dictionary dict's keys.

print("Return a list of keys: \n",dict1.keys())

