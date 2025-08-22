#Create function
def computepay(h,r):
    #check condition
    if h<=40:
        pay1=h*r
        return pay1
    elif h>40:
        pay2=40*r+(h-40)*1.5*r
        return pay2
    else:
        print("Error.Please input a valid value!")

#Enter hour from user
hrs=int(input("Enter hours: "))
rate=float(input("Enter rate per hour: "))
p=computepay(hrs,rate)
print("Pay: ",p)