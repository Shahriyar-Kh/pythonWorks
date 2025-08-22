#identity op two is and is not use for matching but when memory address same

a="shahriyar"
b=a 
print("id(a) and id(b)=",id(a)," and ",id(b))
print("a is b:",a is b)#true
print("a is not b:",a is not b)#false

a=[1,2,3]
b=[1,2,3]

print("a is b = ", a is b)#false
print("a is not b= ", a is not b)#true
