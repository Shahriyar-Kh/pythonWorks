#EXample 1
from enum import Enum

class subjects(Enum):
    English=1
    Maths=2
    HCI=3
    MAD=4
"""
In the above code, "subjects" is the enumeration. 
It has different enumeration members, e.g., subjects.MATHS. Each member is assigned a value.

Each member is ab object of the enumeration class subjects, 
and has name and value attributes
""" 

obj1=subjects.Maths
obj2=subjects.HCI
print(type(obj1),obj1.value)
print(type(obj2),obj2.value)

#Example 2 Value bound to the enum member needn't always be an integer, it can be a string as well.

class subjects(Enum):
    English="E"
    Maths="M"
    HCI="H"
    MAD="MD"
    
obj1=subjects.Maths
obj2=subjects.HCI
print("\n",obj1.name,obj1.value)
print(obj2.name,obj2.value,"\n")

#Example 3  You can iterate through the enum members in the order of their appearance in the definition
for sub in subjects:
    print(sub.name,sub.value)

#Example 4
"""
An enum class cannot have same member appearing twice, 
however, more than one members may be assigned same value. 
To ensure that each member has a unique value bound to it, 
use the @unique decorator."""

from enum import Enum,unique
#@unique
class subjects(Enum):
       ENGLISH = 1
       MATHS = 2
       GEOGRAPHY = 3
       HCI = 2
obj3=subjects.MATHS
print(obj3.name,obj3.value,"\n")
"""
unique
    raise ValueError('duplicate values found in 
%r: %s' %
ValueError: duplicate values found in <enum 'subjects'>: HCI -> MATH
    """
#Example 5
"""The Enum class is a callable class, hence you can use the following alternative method of defining enumeration −
"""
from enum import Enum
subjects1 = Enum("subjects", "ENGLISH MATHS SCIENCE SANSKRIT")
for sub in subjects1:
    print(sub.name)