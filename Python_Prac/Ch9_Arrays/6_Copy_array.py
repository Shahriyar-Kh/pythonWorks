#Example 1
import array as arr
#create array
array=arr.array('i',[1,2,3,4,5,6])

#assign array to another by the assingment op
newarray=array#it refeence same object
print("Id: ",id(array),"Array: ",array)
print("Id: ",id(newarray),"Array: ",newarray)
#change in array reflect to newarray
array[3]=10
print("\nId: ",id(array),"Array: ",array)
print("Id: ",id(newarray),"Array: ",newarray)

#physical copy of an array named copy and use deepcopy() function in the module
import copy
newarray=copy.deepcopy(array)
print("\nafter copy the array:\n id: ",id(array),"Array: ",array)
print("after copy the array:\n id: ",id(newarray),"Array: ",newarray)
#chang in array not reflect newarray
array[4]=102
print("\nafter Changing the array:\n id: ",id(array),"Array: ",array)
print("after changing the array:\n id: ",id(newarray),"Array: ",newarray)



