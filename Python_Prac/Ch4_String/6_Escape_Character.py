#Example
"""when a normal string is printed the escape character '\n' is processed to introduce a newline"""
normal="Hello\nWord"
print("Normal:",normal)

"""However, because of the raw string operator 'r' the effect of escape character is not translated as per its meaning."""
raw="Hello\nWord"
print("Raw: ",raw)

#Example for all
# 1.8.1 ignore \
s='this string will not include \
blackslashes or newline character.'
print(s)

# 1.8.2 Escape blacksalsh \\
s="The \\ character is called blackslash"
print(s)

#1.8.3 Escape single quote 'Python'
s='Hello \'Python \''
print(s)

#1.8.4 Escape double quote "Python"
s='Hello \"Python\"'
print(s)

#1.8.5 escape \b to generate ASCII backspace
s='Hel\blo'
print (s)

# 1.8.6 ASCII Bell character
s='Hello\a'
print (s)

#1.8.7 Horizontal tab
s='Hello\tPython'
print (s)

# 1.8.7 form feed
s= "hello\fworld"
print (s)

#1.8.8 Octal notation
s="\101"
print(s)

# 1.8.9 Hexadecimal notation
s="\x41"
print (s)