#Example 1
try:
    fh=open("testfile",'w')
    fh.write("This is the second file for exception handling")
finally:
    print("Error.can\' finde the file or read data")
    fh.close()
"""
If you do not have permission to open the file in writing mode, then it will produce the following output −

Error: can't find file or read data
"""   
#The same example can be written more cleanly as follows −
try:
    fh=open("testfile1.txt","w")
    try:
        fh.write("This is the second file for exception handling")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error.can\' finde the file or read data")
    

#Example 3 Following is an example for a single exception −
#define a function here
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Arg:
        print("The argument does not contain numbers\n",Arg)
        
#call the above function
temp_convert('cyz')

"""It will produce the following output −

The argument does not contain numbers
invalid literal for int() with base 10: 'xyz'"""