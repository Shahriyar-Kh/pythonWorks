#Example 1 create 2d array
array=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(array)

#Example Accessing element
print(array[0])#[1,2,3,4]
print(array[1][1])#6

#Example all element access of the array
for i in array:
    for j in i:
        print(j,end=" ")
    print()
#Example Insert the another row
array.insert(1,[1.1,2.2,3.3,4.4])
for i in array:
    for j in i:
        print(j,end=" ")
    print()
    
#Example Update
array[1]=[1.1,1.2,1.3,1.4]
for i in array:
    for j in i:
        print(j,end=" ")
    print()
    
#Example Delete items
del array[1]
for i in array:
    for j in i:
        print(j,end=" ")
    print()