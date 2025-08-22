#Example 1 IndexError
#It is shown when trying to access item at invalid index.
num=[10,20,30,40]
#for n in (range(5)):#IndexError: list index out of range
for n in range(4):
    print(num[n])

#Example 2 ModuleNotFoundError
#This is displayed when module could not be found.

"""
import notamodule
Traceback (most recent call last):

   import notamodule
ModuleNotFoundError: No module named 'notamodule'

"""
#Example 3 KeyError
#It occurs as dictionary key is not found.

d1={1:'aa',2:'bb',3:'cc'}
#print(d1['4'])
"""
Traceback (most recent call last):
   D1['4']
KeyError: '4'
    """
    
#Example 4 ImportError
#It is shown when specified function is not available for import.
"""
from math import cube
Traceback (most recent call last):

   from math import cube
ImportError: cannot import name 'cube'"""


#Example 5 StopIteration error
#This error appears when next() function is called after iterator stream exhausts.
it=iter([1,2,3])
print(next(it))
print(next(it))
print(next(it))

#print(next(it))
"""
Traceback (most recent call last):

   next(it)
StopIteration
    """

#Example 6 TypeError
#This is shown when operator or function is applied to an object of inappropriate type.

#print('2'+2)
#TypeError: can only concatenate str (not "int") to str


#Example 7 ValueError
#It is displayed when function's argument is of inappropriate type.
#print(int('xyz'))
#ValueError: invalid literal for int() with base 10: 'xyz'

#Example 8 NameError
#This is encountered when object could not be found.
#print(age)
#NameError: This is encountered when object could not be found.

#Example 9 ZeroDivisionError
#It is shown when second operator in division is zero.
#x=100/0
#ZeroDivisionError: It is shown when second operator in division is zero.


#Example 9 KeyboardInterrupt
#When user hits the interrupt key normally Control-C during execution of program.
"""
name=input('enter your name')
enter your name^c
Traceback (most recent call last):

   name=input('enter your name')
KeyboardInterrupt
    """