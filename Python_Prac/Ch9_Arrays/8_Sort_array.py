#Example 1 sorting array using bubble sort a sorting alg
import array as ary
#create array
CreateArray=ary.array('i',[9,2,4,10,30,20,5,7,8])
print("Orignal array: ",CreateArray)
#length
for i in range(0,len(CreateArray)):
    for j in range(i+1,len(CreateArray)):
        if CreateArray[i]>CreateArray[j]:
            temp=CreateArray[i]
            CreateArray[i]=CreateArray[j]
            CreateArray[j]=temp
print("Sorted array:",CreateArray)            


#Using the sort() Method from List
"""
Even though array doesn't have a sort() method, Python's built-in List class does have a sort method. 
We shall use it in the next example.
First, declare an array and obtain a list object from it, using tolist() metho"""

a = ary.array('i', [10,5,15,4,6,20,9])
b=a.tolist()
b.sort()
a = ary.array('i')
a.fromlist(b)
print ("Sorted array(sort method): ",a)

#Example 3  Using the Builtin sorted() Function

a1=ary.array("i",[4,5,6,9,2,1,3])
a1=ary.array('i',sorted(a1))
print("Sort array(sorted func): ",a1)
