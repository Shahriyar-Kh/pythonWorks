class Parent:
    def __init__(self):#parent constructor
        self.attr=100
        print("Calling parent constructor")
    def parentMethod(self):
        print("Parent method")
    def set_attr(self,attr):
        self.attr=attr
    
    def get_attr(self):
        print("Parent attr:",self.attr) 
    
class child(Parent):#define child class
    def __init__(self):
        print("Calling child constructor")
    def childMethod(self):
        print("Calling child method")

obj1=child()# instace of child c
obj1.parentMethod()#calling parent method
obj1.childMethod()# calling child method
obj1.set_attr(200)#caliing parent method

class division:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def divide(self):
      return self.n/self.d
class modulus:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def mod_divide(self):
      return self.n%self.d      
class div_mod(division,modulus):
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def div_and_mod(self):
      divval=division.divide(self)
      modval=modulus.mod_divide(self)
      return (divval, modval)
x=div_mod(10,3)
print ("division:",x.divide())
print ("mod_division:",x.mod_divide())
print ("divmod:",x.div_and_mod())

# Example 2

# Define a class 'division' with an initializer (__init__) and a method 'div'
class division:
    def __init__(self, a, b):
        self.n = a
        self.d = b
    def div(self):
        return self.n / self.d
# Define a class 'modules' with an initializer (__init__) and a method 'mdiv'
class modules:
    def __init__(self, a, b):
        self.n = a
        self.d = b
    def mdiv(self):
        return self.n % self.d
# Define a class 'div_mod' that inherits from both 'division' and 'modules'
class div_mod(division, modules):
    def __init__(self, a, b):      # When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
        """
        Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
        To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function: """
        division.__init__(self,a,b)
        """Use the super() Function
        Python also has a super() function that will make the child class 
        inherit all the methods and properties from its parent:
        """        
        # Initialize the attributes of the base classes
        super().__init__(a, b)
        """
        By using the super() function, you do not have to use the name of the parent element, 
        it will automatically inherit the methods and properties from its parent.
        """

    def div_mod_f(self):
        # Call the 'div' method from the 'division' class and 'mdiv' method from the 'modules' class
        div_value = self.div()
        mod_value = self.mdiv()
        return div_value, mod_value

# Create an instance of the 'div_mod' class with values 10 and 3
obj2 = div_mod(10, 3)

# Print the results of calling methods on the 'div_mod' instance
print("Division:", obj2.div())            # Output: 3.3333333333333335
print("Mod Division:", obj2.mdiv())       # Output: 1
print("Div and Mod:", obj2.div_mod_f())   # Output: (3.3333333333333335, 1)
