#Example 1
a=10
b=0
try:
    print(a/b)
except Exception:
    print("General Exception")
finally:
    print("inside outer finally block")
"""
It will produce the following output −

General Exception
inside outer finally block
"""  
#Example 2
"""
Let us now see how to nest the try constructs. 
We put another "try − except − finally" blocks inside the existing try block. 
The except keyword for inner try now handles generic Exception, 
while we ask the except block of outer try to handle ZeroDivisionError.

Since exception doesn't occur in the inner try block, its corresponding generic Except isn't called. The division by 0 situation is handled by outer except clause."""
print("\nExample 2")
try:
    print(a/b)
    try:
       print("This is inner try block") 
    except Exception:
       print("General Exception")
    finally:
       print("inside inner finally block")
except ZeroDivisionError:
    print("Division by 0")
finally:
    print("inside Outer finally block ")
"""
It will produce the following output −

Division by 0
inside outer finally block
"""
    

#Example 3
"""
Now we reverse the situation. Out of the nested try blocks, 
the outer one doesn't have any exception raised, but the statement causing division by 0 is inside inner try, 
and hence the exception handled by inner except block. Obviously, the except part corresponding to outer try: will not be called upon."""
print("\nExample 3")
try:
     print("this is outer try block")
     try:
         print(a/b)
     except ZeroDivisionError:
        print("Division by 0")
     finally:
        print("Inside the inner finally block")
except Exception:
    print("General Exception")
finally:
    print("inside Outer finally block ")    

"""
It will produce the following output −

This is outer try block
Division by 0
inside inner finally block
inside outer finally block

    """
    
