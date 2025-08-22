#decalre variables
list1=[]
smallest=None
largest=None
#Check condition we using while loop when we dont idia how many iteration
while True:
    num=input("Enter the number: ")
    if num=="done":
        break
    try:
        num1=int(num)
    except:
        print("Invalid input")
    
    if largest is None:
        largest=num1
    elif num1>largest:
        largest=num1
    elif smallest is None:
        smallest=num1
    elif num1<smallest:
        smallest=num1
print("Maximum is",largest)
print("Minimum is",smallest)