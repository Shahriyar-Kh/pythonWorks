#Example 1
capital={"Kpk":"Peshawer","Pakistan":"Islamabad","Punjab":"Lahore","Sindh":"Karachi"}
print(capital)

#Example 2
number={10:"Ten",20:"Twenty",30:"Therty",40:"Fourty"}
print(number)

#Example 1
"""
Only a number, string or tuple can be used as key. 
All of them are immutable. You can use an object of any type as the value. Hence following definitions of dictionary are also valid −"""

d1={"Fruit":["Mango,Banana"],"Flower":["Rose","Lotu"]}
d2={("Pakistan,USA"):"Countries",("Islamabad","New York"):"Capitals"}

print("Dict: ",d1)
print("Dict: ",d2)

#Example 2 Python doesn't accept mutable objects such as list as key, and raises TypeError.
d1 = {["Mango","Banana"]:"Fruit", "Flower":["Rose", "Lotus"]}

