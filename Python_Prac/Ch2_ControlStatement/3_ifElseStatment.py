#program for discount if elif else
"""
The discount structure used in an earlier
example is modified to different slabs of discount −

20% on amount exceeding 10000,

10% for amount between 5-10000,

5% if it is between 1 to 5000.

no discount if amount<1000"""

discount=0
amount=int(input("Enter the amount: "))

if amount>10000:
    discount=amount*20/100
    print(f"The 20% discount on amount {amount} is ={discount}")    
elif amount>5000:
    discount=amount*10/100
    print(f"The 10% discount on amount {amount} is ={discount}")
elif amount>1000:
      discount=amount*5/100
      print(f"The 5% discount on amount {amount} is ={discount}")
else:
    print("Sorry! no discount applicable")
print("Payable amount is= ",amount-discount)

#program for discount if else
discount=0
amount=int(input("Enter the amount: "))

if amount>10000:
    discount=amount*20/100
    print(f"The 20% discount on amount {amount} is ={discount}")    
else:
    if amount>5000:
        discount=amount*10/100
        print(f"The 10% discount on amount {amount} is ={discount}")
    else:
        if amount>1000:
            discount=amount*5/100
            print(f"The 5% discount on amount {amount} is ={discount}")
        else:
            print("Sorry! no discount applicable")
print("Payable amount is= ",amount-discount)

# 1.3 Nested If Statements
"""
There may be a situation when you want to check for another condition after a condition resolves to true.
In such a situation, 
you can use the nested if construct."""

num=int(input("Enter the number: "))
if num%2==0:
    if num%3==0:
        print("divisible by 3 and 2")
    else:
        print("divisible by 2 not divisible by 3")
else:
    if num%3==0:
        print("divisible by 3 not divisible by 2 ")
    else:
        print("not divisible by 2 not divisible by 3")

