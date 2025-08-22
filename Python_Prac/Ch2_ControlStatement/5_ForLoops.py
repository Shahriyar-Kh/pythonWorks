#Using "for" with a String
"""
A string is a sequence of Unicode letters, 
each having a positional index. The following 
example compares each character and displays 
if it is not a vowel ('a', 'e', 'I', 'o' or 'u')"""

zen='''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
for char in zen:
    if char not in "aeiou":
        print(char,end='')
        
# Using "for" with a Tuple
"""
Python's tuple object is also an indexed sequence,
and hence we can traverse its items with a for loop.
Example
In the following example, the for loop traverses 
a tuple containing integers and returns the total of all numbers."""

numbers=(1,2,3,4,5,6,7,8,9,10)
total=0
for num in numbers:
    total+=num
print("\nSum of all numbers:",total)

#Using "for" with a List
"""
Python's list object is also an indexed sequence, 
and hence we can traverse its items with a for loop.

Example
In the following example, the for loop traverses 
a list containing 
integers and prints only those which are divisible by 2"""

lists=[2,4,6,7,2,9,8,16,18]
total=[]
for num in lists:
    if num%2==0:
        print("divisible by 2 numbers in lists: ",(num))
        total.append(num) 
print("All divisible by 2 numbers in lists: ",list(total))

#Using "for" with a Range Object
"""
Python's buil-in range() function returns a range object. 
Python's range object is an iterator which generates an integer with each iteration. 
The object contains integrrs from start to stop, separated by step parameter.
Syntax
The range() function has the following syntax −"""

numbers=range(5)
print("List:",list(numbers))
numbers=range(1,10)
print("List:",list(numbers))
numbers=range(0,20,2)
print("Even List: ",list(numbers))

for num in range(5):
    print(num,end=' ')
print()
for num in range(1,10):
    print(num,end=' ')
print()
for num in range(0,20,2):
    print(num,end=' ')
print()

#Factorial of a Number
"""
Factorial is a product of all numbers from 1 to that number say n. 
It can also be defined as product of 1, 2, up to n."""

#initialize fact 1
fact=1
#factorial of 5
n=5
for x in range(1,n+1):
    fact*=x
   # print(fact)
print(f"factorial of {n} is {fact}")

#Using "for" Loop with Sequence Index
"""
To iterate over a sequence, we can obtain the 
list of indices using the range() function

"""
numbers=[10,20,30,40,50,60,70]
indexes=range(len(numbers))
for index in indexes:
    print("Index: ",index,"numbers: ",numbers[index])

# Using "for" with Dictionaries
"""
Unlike a list, tuple or a string, dictionary data type in Python is not a sequence, as the items do not have a positional index. However, 
traversing a dictionary is still possible with different techniques.

Running a simple for loop over 
the dictionary object traverses the keys used in it."""
dicts={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}
for x in dicts:
    #print(x)#show only keys
    print(x," : ",dicts[x])#show data with keys
#return a tuple of keys with data
for y in dicts.items():
    print(y)
#return without tuple same data
for x,y in dicts.items():
    print(x," : ",y)

