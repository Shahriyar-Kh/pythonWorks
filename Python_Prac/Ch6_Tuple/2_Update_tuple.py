#Example tuple i simmutable so we convert to list
tuple1=(1,2,3,4,5,6)
print("tuple before update: ",tuple1,"id(): ",id(tuple1))
#Convert tuple to dictionary
list1=list(tuple1)
#now we can modify
#changing value of index 0
list1[0]=10
#appending value at the end
list1.append(77)

#sorted in decending order
list1.reverse()
print("Update List: ",list1)

#list convert to tuple
tuple1=tuple(list1)
print("Updated tuple: ",tuple1,"id():",id(tuple1))

