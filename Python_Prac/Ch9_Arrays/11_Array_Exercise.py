#Example 1 Python program to find the largest number in an array −

import array as ary
ary1=ary.array('i',[1,2,9,20,10,3,4,99,4,23])
print("Orignal array: ",ary1)
#let assign largest value 
largest=ary1[0]
for i in range(1,len(ary1)):
    if ary1[i]>largest:
        largest=ary1[i]
        
print("Largest value is : ",largest)

#Example 2 Python program to store all even numbers from an array in another array −

#using the above ary1
ary2=ary.array('i',[])

for i in range(0,len(ary1)):
    if i%2==0:
        ary2.append(i)
print("array of even number: ",ary2)

#Example 3 Python program to find the average of all numbers in a Python array −"""
ary3=ary.array('i',[5,10,15,20,25,5,20])
sum=0
avg=0
print("\nOrignal array:",ary3)
for i in range(0,len(ary3)):
    sum+=ary3[i]
    avg=sum/len(ary3)

print("The sum of all items: ",sum)    
print("The average of %d: %f" %(sum,avg))

#Example 4 Python program to convert a string in an array
string="Shahriyarkhan"
charArray=ary.array('b',[ord(char) for char in string])

print("The string array: ",charArray)