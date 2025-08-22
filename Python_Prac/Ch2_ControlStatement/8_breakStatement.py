#Python break Statement
"""
It terminates the current loop and resumes 
execution at the next statement
The break statement can be used in both 
while and for loops.

If you are using nested loops, 
the break statement stops the execution of the 
innermost loop and start executing the next line
of code after the block."""

#break in for loop
letters="Python"
for letter in letters:
    if letter=="h":
        break
    print("Current letter: ",letter)
#break in while loop
var=10
while var>0:
    print("Current variable value: ",var)
    var-=1
    #var=var-1
    if var==5:
        break
    
print("Good bye!")