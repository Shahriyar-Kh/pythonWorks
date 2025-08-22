#Example for discount on purchase

discount=0
amount=int(input("Enter the amount: "))
if amount>1000:
    discount=amount*10/100
    print(f"The 10% discount on amount {amount} is ={discount}")
else:
    print("Sorry! No discount is applicable")
