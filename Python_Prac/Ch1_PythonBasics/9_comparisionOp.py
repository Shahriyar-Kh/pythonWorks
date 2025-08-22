#using less then op(<) and grater then(>)
a=5
b=5
c=6
result=a>b
print("{0} > {1}: {2} ".format(a,b,result))
result1=a<b
print("{0} < {1}: {2} ".format(a,b,result1))
result2=c>a
print("{0} > {1}: {2} ".format(c,a,result2))

#using less then or equal to(<=)
result2=a<=b
print("{0} <= {1}: {2} ".format(a,b,result2))

#using less then or equal to(>=)
result2=a>=b
result3=c>=a
#using less then or equal to(<=)
result2=a<=b
print("{0} <= {1}: {2} ".format(a,b,result2))
print("{0} >= {1}: {2} ".format(c,a,result3))

#using equal(==)
result4=a==b
result5=a==c
print("{0} == {1}: {2} ".format(a,b,result4))
print("{0} == {1}: {2} ".format(a,c,result5))

#using != is not equal
result6=a!=c
result7=a!=b
print("{0} != {1}: {2} ".format(a,c,result6))
print("{0} != {1}: {2} ".format(a,b,result7))

