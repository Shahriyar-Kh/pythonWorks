def weekday(n):
    match n:
        case 0: return "Monday"
        case 1: return "Tuesday"
        case 2: return "Wednesday"
        case 3: return "Thursday"
        case 4: return "Friday"
        case 5: return "Saturday"
        case 6: return "Sunday"
        case _: return "invalid day number"
        
print(weekday(0))
print(weekday(3))
print(weekday(8))

#Combined Cases 
"""
Sometimes, there may be a situation where for more thanone cases, 
a similar action has to be taken. For this, you can combine cases 
with the OR operator represented by "|" symbol"""
def access(user):
    match user:
        case "admin" | "Manager": return "Full access"
        case "Guest": return "Limited access"
        case  _:return "No access"
print(access("Manager"))
print(access("Guest"))
print(access("Ravi"))

#List as the Argument
"""
Since Python can match the expression against any literal, 
you can use a list as a case value. Moreover, 
for variable number of items in the list, 
they can be parsed to a sequence with "*" operator."""

def greeting(details):
    match details:
        case [time,name]:
            return (f"Good {time} {name}!")
        case [time,*names]:
            msg=""
            for name in names:
                msg+=(f"Good {time} {name}!\n")
            return msg
            
print(greeting(["Morning","shary"]))
print(greeting(["Afternoon","Khan"]))
print(greeting(["Evening","Umair","Fahad","Ali"]))


#Using "if" in "Case" Clause
"""
Normally Python matches an expression against literal cases.
However, it allows you to include if statement in 
the case clause for conditional computation of match variable."""

def interest(detials):
    match detials:
        case [amount,duration] if amount<10000:
            return amount*10*duration/100
        case [amount,duration] if amount>=10000:
            return amount*duration*15/100
print("Interest=",interest([5000,5]))
print("Interest= ",interest([12000,3]))
