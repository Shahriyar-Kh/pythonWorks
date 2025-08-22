#Example1 Following statements print the respective class of different built-in data type objects
print (type(10))
print (type(2.56))
print (type(2+3j))
print (type("Hello World"))
print (type([1,2,3]))
print (type({1:'one', 2:'two'}))


#EXample 2 Let us verify the type of an object of a user-defined class −
class test:
    pass
obj1=test()
print(type(obj1))


#EXample 3
print(isinstance(10,int))
print (isinstance(2.56,int))
print (isinstance(2+3j,complex))
print('\n')
print (isinstance([1,2,3], tuple))
print (isinstance({1:'one', 2:'two'}, set))

#Example 3
print("\n")
print (issubclass(int, object))
print (issubclass(str, object))
print (issubclass(test, object))

#Example 4 callable fuction
print("\n")
print(callable("Hello"))
print(callable(abs))
print(callable(test))

#Example 5 gettattr() function
class test:
    def __init__(self):
        self.name="Shary"
obj2=test()
print("Name of the attribute:",getattr(obj2,'name'))

#Example 6 settattr()
#Create new attribute
setattr(obj2,'Age',20)
print("Name:",obj2.name,"Age:",obj2.Age)
setattr(obj2,'name','sharyKhan')
print("Name:",obj2.name,"Age:",obj2.Age)

#Example 7 hasattr()
print(hasattr(obj2,'Age'))
print(hasattr(obj2,'name'))
print(hasattr(obj2,'marsk'))

#Example 8 dir()
print("\ndir(int)",dir(int))
print("\ndir(dict)",dir(dict))