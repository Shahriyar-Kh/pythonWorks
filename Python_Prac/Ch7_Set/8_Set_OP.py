s1={1,2,3,4,5,5}
s2={1,3,6,7,8}
s3=s1|s2
#also use union method
s3=s1.union(s2)
print(f"{s1} U {s2}= {s3}")

#Intersection Operator (&)
"""
The intersection of two sets AA and BB, denoted by A∩B, consists of all elements that are both in A and B. For example,"""
s5=s1 & s1
print(f"{s1} intersection {s2}={s5}")

#Difference Operator (-)
"""
The difference (subtraction) is defined as follows. The set A−B consists of elements that are in A but not in B. For example,"""
s6=s1-s2
s7=s2-s1
print(f"Difference of s1-s2 \n {s1} - {s2}={s6}")
print(f"Difference of s1-s2 \n {s2} - {s1}={s7}")

#Symmetric Difference Operator
"""
The symmetric difference of A and B is denoted by "A Δ B" and is defined by
A Δ B = (A − B) ⋃ (B − A)
Python uses the "^" symbol as a symbolic difference operator."""
s8=s1^s2
print(f"S_Difference of s1-s2:\n{s1} ^ {s2}= {s8}")

