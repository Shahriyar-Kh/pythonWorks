"""he algorithm for finding prime factors is as follows −

Accept input from user (n)

Set divisor (d) to 2

Perform following till n>1

Check if given number (n) is divisible by divisor (d).

If n%d==0

a. Print d as a factor

Set new value of n as n/d

Repeat from 4

If not

Increment d by 1

Repeat from 3
"""

n=int(input("Enter the number: "))
divisor=2
print(f"Prime factors for {n}")
while n>1:
    if n%divisor==0:
        print(divisor)
        n=n/divisor
        continue
    divisor=divisor+1
    