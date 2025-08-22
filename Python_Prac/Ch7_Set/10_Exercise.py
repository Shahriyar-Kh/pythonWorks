#Example 1 Python program to find common elements in two lists with the help of set operations −"""
s1={1,2,3,4,5}
s2={1,2,5,6,7}
s3=s1&s2
print(f"The Common in both sets:\n {s1} & {s2}= {s3}")

#Example 2 Python program to check if a set is a subset of another −"""
s1={1,2,3,4,5,6,7}
s2={1,3,5,7}
s4=s2.issubset(s1)
print(f"{s2} is the subset of {s1} ={s4}")

#Example 3Python program to obtain a list of unique elements in a list −

l1=[1,2,2,3,4,3,4,5]
print("Oringal list: ",l1)
s1=set(l1)
print("Unique Set: ",s1)

#Exercise Programs

# 1. Python program to find the size of a set object

print(f"The size of set1 {s1}= {len(s1)} ")

# 2. Python program that splits a set into two based on odd/even numbers.

s_num={1,2,3,4,5,6,7,8,9,10}
s_even=set()
s_odd=set()
for i in s_num:
    if i%2==0:
        s_even.add(i)
    else:
        s_odd.add(i)
print(f"Set {s_num}\n Set_Even: {s_even}\n Set_Odd: {s_odd}") 

# 3. Python program to remove all negative numbers from a set.

s1={1,2,3,4,-1,-2,-3,-4}
s2=set()

for i in s1:
    if i>0:
        s2.add(i)
print("\n\nOrignal Set: ",s1)
print("Set without negative numbers: ",s2)

# 4. Python program to build another set with absolute value of each number in a set.
set1={1,2,3,-3,0,-1,-1.1,-0.5}
s_abs=set()
for i in set1:
    j=abs(i)
    s_abs.add(j)
print(f"Absulote set: ",s_abs)

#also 
abs_set={abs(num) for num in set1}
print(f"Absulote set: ",abs_set)


#Python program to remove all strings from a set which has elements of different types.
mixed_S={1,"a",2,"b",3,"c"}
filter_S={num for num in mixed_S if not isinstance(num,str)}
print("Mixed set: ",mixed_S)
print("Filterd set: ",filter_S)
