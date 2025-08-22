#Example 1 To store tuple items in individual variables, use multiple variables on the left of assignment operator

tuple1=(2,4,6,8)
a,b,c,d=tuple1
print("a:",a," b:",b," C:",c," d:",d)

#Example 2 If the number of variables is more or less than the length of tuple, Python raises a ValueError.

# a1,b1=tuple1
# print("a1:",a1,"b1:",b1)

#the "*" symbol is used for unpacking. Prefix "*" to "y", as

a1,*b1=tuple1
print("a1:",a1,"b1: ",b1)

#Example 3  the tuple contains 6 values and variables to be unpacked are 3. We prefix "*" to the second variable.

tuple2=(1,2,3,4,5,6)
x,*y,z=tuple2
print("x:",x,"y:",y,"z:",z)