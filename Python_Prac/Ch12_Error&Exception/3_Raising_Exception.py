def functionName(level):
    if level<1:
        raise Exception(level)
     # The code below to this would not be executed
      # if we raise the exception
    return level
try:
    l=functionName(-10)
    print('level=',1)
except Exception as e:
    print("Error in level arg",e.args[0])
"""
This will produce the following output −

error in level argument -10
    """