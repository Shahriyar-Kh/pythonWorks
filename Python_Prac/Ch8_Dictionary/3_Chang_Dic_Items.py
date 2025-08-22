#Example Empty Dic
d1=dict()
d2={}#both are dic same output
print(d1)
print(d2)

#Dictionary from List of Tuples
"""
The dict() function constructs a dictionary from a list or tuple of two-item tuples. First item in a tuple is treated as key, and the second as its value."""

d1=dict([('a',100),('b',200)])
d2=dict((('a',"One"),("b","Two")))
print("\nd1: ",d1)
print("d2: ",d2)

#Dictionary from Keyword Arguments
"""
The dict() function can take any number of keyword arguments with name=value pairs.
It returns a dictionary object with the name as key and associates it to the value."""

d3=dict(a=10,b=20,c=30)
d4=dict(d=40,e=50)
print("\nd3: ",d3)
print("d4: ",d4)