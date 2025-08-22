#Example 1  array.count()
import array as ary
a=ary.array('i',[1,2,3,4,5,8,9,10,2,3,2,1,2])
c=a.count(2)
print("Count of 2: ",c)

#Example 2 array.index() method
"""The index() method in array class finds the position of first occurrence of a given element in the array."""
ind=a.index(4)
print("index of 4 is: ",ind)

#Example 3 array.fromlist() Method
"""The fromlist() method appends items from a Python list to the array object.
i − The list, items of which are appended to the array. All items in the list must be of same arrtype.
"""
ary1=ary.array('i',[1,2,3,4,5])
list1=[5,6,7,8]
#appending list into array
ary1.fromlist(list1)
print("After the  appended list  array is: \n",ary1)


#Example 4 array.tofile() Method
"""
The tofile() method in array class writes all items (as machine values) in the array to the file object f.

Syntax array.tofile(f)
Parameters
f − the file object obtained with open() function. The file to be opened in wb mode."""

f=open('list.txt','wb')
ary.array('i',[10,20,30,40,50]).tofile(f)
f.close()
"""
Output
After running the above code, a file named as "list.txt" will be created in the current directory.
"""

#Example 5  array.fromfile() Method
"""
The fromfile() method reads a binary file and appends specified number of items to the array object.
Syntax array.fromfile(f, n)
Parameters
f − The file object referring to a disk file opened in rb mode

n − number of items to be appended"""
ary2=ary.array('i',[1,2,3,4,5])
f=open('list.txt','rb')#open the file for read only
ary2.fromfile(f,5)#append the file all value to this array
print(ary2)

