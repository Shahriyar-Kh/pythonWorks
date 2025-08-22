#Example 1
"""
Python program to create a new dictionary by extracting the keys from a given dictionary"""

d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}

keys={"two","one"}
d2={}
for k in keys:
    d2[k]=d1[k]
    
print("Orignal dic: \n",d1)
print("new dict: \n",d2)

#Example 2
"""
Python program to convert a dictionary to list of (k,v) tuples."""
l1=list(d1.items())
print("\nList of tuple: \n",l1)

#Example 3
"""
Python program to remove keys with same values in a dictionary."""

D1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}
val=list(D1.values()) #all values
unique_val=[v for v in val if val.count(v)==1]#unique values

d2={}
for k,v in D1.items():
     if v in unique_val:
         d={k:v}
         d2.update(d)
         
         
print("dict with unique value: ",d2)

#Example 4 Python program to sort list of dictionaries by values

# Sample list of dictionaries
D11 = [
    {'name': 'John', 'age': 30, 'score': 95},
    {'name': 'Alice', 'age': 25, 'score': 85},
    {'name': 'Bob', 'age': 35, 'score': 92},
]
sorted_D1=sorted(D11,key=lambda x:x['score'])
for i in sorted_D1:
    print(i)

        
#Python program to extract dictionary with each key having non-numeric value from a given dictionary.

dict1={1:10,2:20,3:30,4:40,5:"khan",6:"ali"}
for k,v in dict1.items():#taking all element 
    if not isinstance(v,(int,float)):#check condition the pair value is not int or float
        print(k,":",v)#key and value print
        

#Python program to build a dictionary from list of two item (k,v) tuples

#creating list of tuples
list1=[('HCI',40),('DSA',70),('MAD',80),('MPL',60)]
#convert list of tuple to dict
dict2=dict(list1)
print("Convert list to dict: ",dict2)

#Python program to merge two dictionary objects, using unpack operator.

#using the above dict1 and dict2 to combine

merg_dict={**dict1,**dict2}
print("merge dict: ",merg_dict)