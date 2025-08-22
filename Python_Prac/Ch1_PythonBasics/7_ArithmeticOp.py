# using + op for addition 
a=4
b=6
c=a+b
#1st method using format function
print("The addition of {0} and {1} is = {2}".format(a,b,c))

#2nd method
print(f"Result:{a}+{b}={c}")

#3rd method
print(f"Result:{a+b}")

#addition of integer and complix numbers
a1=4+5j
b1=4
c=a1+b1
print("The addition of {0} and {1} is = {2}".format(a1,b1,c))
#using - for subtraction
c=a-b
print("The subtraction of {0} and {1} is = {2}".format(a,b,c))

#using * for mult
c=a*b
print("The multiplication of {0} and {1} is = {2}".format(a,b,c))

#using / for divid but result in float
c=a/b
print(f"Division:{a}/{b}={c} ")

#using double // for divid but result in int
c=a//b
print("Division of {0} and {1} is = {2}".format(a,b,c))

#using % modulas for remainder
a2=13
b2=5
c=a2%b2
print("The remainder of {0} and {1} is = {2}".format(a2,b2,c))

#using exponent op ** or power
a3=4+5j
b3=2
c=a3**b3
print("{0} Power {1} is = {2}".format(a3,b3,c))
print("""
      (4+5j)^2=16+40j+25j^2
      Remember that j^2 is equal to -1
      so the expression simplifies to
      16+40j−25=−9+40j
      """)

