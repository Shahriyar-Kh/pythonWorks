#Example1 Empty tuple
tuple1=()
tuple1=(2,)
print(tuple1)

#Example2 Accessing Tuple items
tuple2=(1,2,3,4,4,5,"Shary","Khan","Hamad")
print(tuple2[2])

#Example3 Updating Tuple
"""Tuples are immutable which means you cannot update or change the values of tuple elements."""
# tuple2[2]=100 Show error means not changing
tuple3=(10,20,30)
t3=tuple2+tuple3# by this technique can update
print(t3)

#Example 4 delete tuple item
del t3
print(t3)