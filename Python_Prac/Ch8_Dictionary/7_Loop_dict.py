#Example 1
"""
Running a simple for loop over the dictionary object traverses the keys used in it."""
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
#    print (x)
   """Once we are able to get the key, its associated value can be easily accessed either by using square brackets operator or with get() method"""
   print(x,":",numbers[x])
   
#Example 3
"""
The dict_items object is a list of key-value tuples over which a for loop can be run as follows:"""
for x in numbers.items():
   print(x)

#Example 5
"""
Similarly, the collection of keys in dict_keys object can be iterated over"""
print("\n\n")
for x in numbers.keys():
   print(x,":",numbers[x])

#Example 6
print("\n\n")
l=len(numbers)
for x in range(l):
   print(list(numbers.keys())[x], ":",list(numbers.values())[x])

