#Example1 
import array as ar
newarray=ar.array('i',[1,2,3,4,5,6,7])
"""
    The array class doesn't have any built-in method to reverse array. Hence, we have to use another array. An empty array "b" is declared as follows −
"""
newarray2=ar.array('i')
"""
Next, we traverse the numbers in array "a" in reverse order, and append each element to the "b" array −
"""
for i in range(len(newarray)-1,-1,-1):
    newarray2.append(i)
print("Orignal array:",newarray)
print("Exteded array is: ",newarray2)
    
#Example 2  
"""
We can also reverse the sequence of numbers in an array using the reverse() method in list class.
List is a built-in type in Python.
We have to first transfer the contents of an array to a list with tolist() method of array class −
"""
a=ar.array('i',[10,5,15,2,3,4,5])
print("\n\n orignal array: ",a)
b=a.tolist()
print("convert to list: ",b)
#We can call the reverse() method now −
b.reverse()
print("Reverse the list: ",b)
"""If we now convert the list back to an array, we get the array with reversed order,"""
a=ar.array('i')
a.fromlist(b)
print("Reverse the orignal array: ",a)
