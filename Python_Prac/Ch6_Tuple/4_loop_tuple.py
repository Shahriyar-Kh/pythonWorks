#Example 1 The following example shows a simple Python for loop construct −
tuple1=(2,3,5,7,8,9)

for i in tuple1:
    print(i,end=' ')
    
#Example 2 To iterate through the items in a tuple, obtain the range object of integers "0" to "len-1"

indexes=range(len(tuple1))
for i in indexes:
    print("tuple1[{}]:".format(i),tuple1[i])
    
