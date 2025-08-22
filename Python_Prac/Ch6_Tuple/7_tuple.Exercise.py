#Example 1 Python program to find unique numbers in a given tuple
t1=(1,2,2,3,4,3,5,6,5,7,7,8,9,2)
t2=()
for x in t1:
    if x not in t2:
        t2+=(x,)
print("Orignal tuple: ",t1)
print("Unique numbers: ",t2)

#Example 2 Example 2 Python program to find sum of all numbers in a tuple −
sum=0
for i in t1:
    sum+=i
print("Sum of all numbers in tuple: ",sum)

#Example 3 Python program to create a tuple of 5 random integers −

import random
t3=()
for i in range(5):
    x=random.randint(0,100)
    t1+=x,
print("Tuple: ",t1) 

#Question 1 Python program to remove all duplicates numbers from a list.

t1=(1,2,2,3,7,4,4,1,8)
t2=()

for i in t1:
    if i not in t2:
        t2+=(i,)
        
print("Tuple without duplicates: ",t2)

#Question 2 Python program to sort a tuple of strings on the number of alphabets in each word.
def num_of_alpha(tS):
    sorted_t = sorted(tS, key=lambda x: sum(y.isalpha() for y in x))
    return sorted_t

input_t = ("Shahriyar", "Umair", "Fahad", "Ali")
result = num_of_alpha(input_t)

print("Original tuple:", input_t)
print("Sorted tuple:", result)

#Question 3 Python program to prepare a tuple of non-numeric items from a given tuple.
