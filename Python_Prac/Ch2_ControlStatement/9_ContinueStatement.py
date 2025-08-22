#Python Continue Statement
"""
The continue statement in Python returns the control to the 
beginning of the current loop. When encountered,
the loop starts next iteration without executing the remaining 
statements in the current iteration.

The continue statement can 
be used in both while and for loops."""

#continue in for loop
letters="Python"
for letter in letters:
    if letter=="h":
        continue
    print("Current letter: ",letter)
#continue in while loop
var=10
while var>0:
    var-=1
    #var=var-1
    if var==5:
        continue
    print("Current variable value: ",var)
print("Good bye!")
