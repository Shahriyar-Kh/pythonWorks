# 1. Decision-making Statement
"""python provide if elif else control statements a part of decision making"""

# 1.1 if Statement
marks=100
result=""
if marks < 30:
    result="Failed"
elif marks > 75:
    result="Passed with distinction"
else:
    result="Passed"
    
print(result)

# 1.2 match Statement
"""Python supports Match-Case statement, 
which can also be used as a part of decision making."""

def checkVowel(n):
    match n:
        case "a": return "Vowel Alphabet"
        case "e": return "Vowel alphabet"
        case "i": return "Vowel alphabet"
        case "o": return "Vowel alphabet"
        case "u": return "Vowel alphabet"
        case _:return "Simple alphabet"
        
print(checkVowel("a"))
print(checkVowel("u"))
print (checkVowel("d")) 


# 1.3 Loops or Iteration Statements
"""
Most of the processes require a group of instructions to be repeatedly executed. In programming terminology, it is called a loop. 
Instead of the next step, 
if the flow is redirected towards any earlier step,
it constitutes a loop."""   

# 1.3.1 for loop when we have the range
words=("one","Two","Three")
for x in words:
    print(x)

# 1.3.2 while loop using 
i=1
while i<6:
    print(i)
    i+=1


