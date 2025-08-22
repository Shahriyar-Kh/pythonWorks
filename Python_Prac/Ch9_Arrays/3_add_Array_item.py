#Example 1
import array as b
newArray=b.array('i',[1,2,3])
newArray.append(4)#append in lasts
print(newArray)

#The insert() Method
"""
The array class also defines insert() method. It is possible to insert a new element at the specified index."""
#Example 2
newArray.insert(1,10)#insert at index 1 
print(newArray)

#The extend() Method
"""
The extend() method in array class appends all the elements from another array of same typecode."""

#Example 3
newArray2=b.array('i',[5,6,7,8])
newArray.extend(newArray2)
print("Extended array: ",newArray)

