#Example 1
"""Suppose we want to separate each letter in a string and put all non-vowel letters in a list object."""

string="Shahriyar khan"
char=[]
vowels='aeiou'
for x in string:
    if x not in vowels:
        char.append(x)
    
print("List without vowels: ",char)

#List Comprehension Technique
"""
We can easily get the same result by a list comprehension technique. A general usage of list comprehension is as follows −"""
chars=[char for char in 'Shahriyar khan ' if char not in 'aioue']
print("List :",char)


#Example 2
"""
Use list comprehension to build a list of squares of numbers between 1 to 10"""

num=[x*x for x in range(1,11)]
print(num)

#Nested Loops in List Comprehension
"""
all combinations of items from two lists in the form of a tuple are added in a third list object."""

list1=[1,2,3,4]
list2=[4,5,6,7]
comblst=[(x,y) for x in list1 for y in list2]
print("combinations of items from two lists:  \n",comblst)

#Condition in List Comprehension
"""
The following statement will create a list of all even numbers between 1 to 20."""
list1=[x for x in range(1,21) if x%2==0]
print("List of even numbers: ",list1)

