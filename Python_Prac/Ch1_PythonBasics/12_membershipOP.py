#using two op in not in return boolean value
string="Shahriyar khan"
a="khan"
b="jan"
print(f"{a} in {string}=",a in string) 
print(f"{b} in {string}=",b in string) 

#using list
list=[2,4,6,8,10]
a=2
b=3
c=a in list
print("{0} in {1} ={2}".format(a,list,c))
print(f"{b} in {list} = {b in list}")

#using dictionary
#finding only keys not values
dict={1:"khan",2:40,3:10,3:4,4:6}
a=2
b=40
print(f"{a} in {dict} ={a in dict}")
print(f"{b} in {dict} ={b in dict}")