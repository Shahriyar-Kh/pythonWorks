marks={"Shary":80,"Fahad":85,"Umair":87}
print("Marks dictionary before update: ",marks)
#Updation
marks["Umair"]=90
print("Marks dictionary after update: ",marks)

#Add new item with pair of key
marks["Ali"]=60
print("Marks dictionary after update: ",marks)

# 1. Using the update() Method
"""You can use the update() method in dict class in three different ways:"""

# 1.2 Update with Another Dictionary
"""In this case, the update() method's argument is another dictionary. 
Value of keys common in both dictionaries is updated. 
For new keys, key-value pair is added in the existing dictionary"""

#create another dic
marks1={"Muhammad":100,"Yaseen":86,"Ubaid":78}
#Update the first dict
marks.update(marks1)
print("Marks dictionary after update: ",marks)


# 1.3 Update with Iterable
"""
If the argument to update() method is a list or tuple of two item tuples,
an item each for it is added in the existing dictionary, 
or updated if the key is existing."""
marks2=[("Yasir",60),("Hamad",70)]
marks1.update(marks2)
print("\nMarks1 dictionary after update: ",marks1)

#1.4 Update with Keyword Arguments
"""
Third version of update() method accepts list of keyword arguments in name=value format. New k-v pairs are added, 
or value of existing key is updated."""
marks1.update(Sana=44,Shary=88)
print("\nMarks1 dictionary after update: ",marks1)

#Using the Unpack Operator
"""
The "**" symbol prefixed to a dictionary object unpacks it to a list of tuples, each tuple with key and value. 
Two dict objects are unpacked and merged together and obtain a new dictionary."""

newmarks={**marks1,**marks}
print("\nNewmarks: ",newmarks)

#Using the Union Operator (|)
"""It updates existing keys in dict object on left, and adds new key-value pairs to return a new dict object."""
newmarks2=marks|marks1
#Also mark|=marks1
print("Union of two dicts: \n",newmarks2)

