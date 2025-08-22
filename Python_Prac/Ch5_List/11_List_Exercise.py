#Example 1 Python program to find unique numbers in a given list."""
list1=[1,2,3,2,4,4,5,6,5,2]
u_nums=[]

for x in list1:
    if x not in u_nums:
        u_nums.append(x)
print("Orignal list: ",list1)
print("Unique numbers in list: ",u_nums)

#Example 2  Python program to find sum of all numbers in a list.

total=0
for x in u_nums:
    total+=x

print("Orignal list: ",u_nums)
print("Sum of all elements in List: ",total)

#Example 3 Python program to create a list of 5 random integers.
import random
list2=[]
for i in range(5):
     x=random.randint(0,100)
     list2.append(x)
     
print("Random List: ",list2)

#Example 4 Python program to remove all odd numbers from a list.
l_Mix=[1,2,3,4,5,6,7,8,9]
l_even=[]
for i in l_Mix:
    if i%2==0:
        l_even.append(i)
        
print("Orignal list: ",l_Mix)
print("Even list: ",l_even) 

#Example 5 Python program non-numeric items in a list in a separate list.

list3=['a','b','c','d',1,2,3]
l_num=[]
for i in list3:
    if not isinstance (i,(int,float)) :
        l_num.append(i)
        
print("Orignal list: ",list3)
print("Non numaric item in a list: ",l_num)

#Example 6 Python program to sort a list of strings on the number of alphabets in each word.

def sort_by_alphaCount(input_l):
    sorted_list=sorted(input_l,key=lambda x: sum(c.isalpha() for c in x))
    return sorted_list

list4=['apple','Banana','Orange','graps','mangoes']
sorted_list=sort_by_alphaCount(list4)

print("Orignal list: ",list4)
print("Sorted list: ",sorted_list)

#Example 7 Python program to create a list of integers representing each character in a string

def char_to_int(input_list):
    #using list comprehension to convert character to ASCII values
    int_list=[ord(char) for char in input_list]
    
    return int_list

mylist="Shahriyar khan"
print("Orignal list:",mylist)

reultlist=char_to_int(mylist)
print("list of ASCII values: ",reultlist)


#Example 8 Python program to find numbers common in two lists.
#Method 1 using intersection method 
l1=[1,2,3,4,5,6]
l2=[2,3,6,4,8,9]

#Using list comprehension
c_list=[x for x in l1 if x in l2]
print("List1 : ",l1)
print("List2: ",l2)
print("Commen in both list: ",c_list)

#using for loop
c_list2=[]
for x in l1:
    if x in l2:
        c_list2.append(x)
print("Common in both list(for): ",c_list2)