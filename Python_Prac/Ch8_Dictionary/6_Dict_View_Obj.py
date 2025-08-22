#EXample 1 items() Method

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
obj = numbers.items()
print("the type of obj: ",type(obj))
print("obj: ",obj)
#update the dict
numbers.update({50:"Fifty"})
print("View automaticaly update: ",obj)

#keys() Method
"""
The keys() method of dict class returns dict_keys object which is a list of all keys defined in the dictionary. 
It is a view object, as it gets automatically updated whenever any update action is done on the dictionary object"""

obj1=numbers.keys()
print("The keys of number dict: ",obj1)

#values() Method
"""The values() method returns a view of all the values present in the dictionary. The object is of dict_value type, which gets automatically updated."""
obj2=numbers.values()
print("The values of dict: ",obj2)