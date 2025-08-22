#built in datatypes
"""
Numeric - int, float, complex
String - str
Sequence - list, tuple, range
Binary - bytes, bytearray, memoryview
Mapping - dict
Boolean - bool
Set - set, frozenset
None - NoneType
    """
#1 Numeric datatypes
var=1  #int(signed integers)
var2=2.3 #float(floating point real values)
var3=3+4j #complix(complex numbers)
var4=True #bool (subtype of integers)

# 2 Sequence datatype

# 2.1 string datatypes 
#a string in python is in object of str class 
str1="khan" 
print(str1)#print complete
print(str1[1])#print second charactor
print(str1[0:3])#print from 0(first ch) to 3(3 exclude)
print(str1[1:])#from 1 to last
print(str1*2)#prints string two time
print(str1+str(1))#concatinated two string

# 2.2list datatypes...enclused [],elements and size can be changed,mutable
#collection of hetroginous data() 
list=[1,"Shahriyar Khan",3.12,4+6j,1.23e-4]

#nested list
nestedList=[["one","two","three"],[1,2,3],[1.2,1.3,1.4]]
print(list)
print(nestedList)

# 2.3 tuple datatype ...enclused(),immutable(cannot be update),read only
tuple=(1,"Shahriyar Khan",3.12,4+6j,1.23e-4)
print(tuple)
#tuple[0]=2 invalid in tuple
#list[0]=2 valid in list

#2.4 range function
for i in range(5):#start from 0 to 5(5 exclusive)
    print(i)
#print  from 1 to 5(5 not include) 
for i in range(1,5):
    print(i)
#print start from 1 with gap 2 to 10 
for i in range(1,10,2):
    print(i)

# dictionary datatype
#create empty dict
dictEmpty={}
#addding element in dict with key
dictEmpty["one"]="this is one"
dictEmpty[2]="this is two"
print(dictEmpty)#print full dict
print(dictEmpty['one'])
print(dictEmpty[2])

#create dict with key
dict1={1:"mangos",2:"oranges",3:"auro",4:"Keela"}
print(dict)
print(dict1.keys())#print only keys
print(dict1.values())#print only values

#set datatype
#create set
set1={"Monday","Tuesday","wednesday","thursday","friday","saturday","Sunday"}
print(set1)
print(type(set1))

#Frozanset

frozenset1=frozenset({"apple","Banana","cherry"})
print(frozenset1)
#Boolean Data Types
a=2
b=3
print(bool(a==b))#return false
print(a==b)#same 

a=None
print(bool(a))#return false

a=()
print(bool(a))#return false

a1=0.0
print(bool(a1))#return false

x=b"khan"
print(type(x))

#bytearay
xx=bytearray(5)
print(xx)
