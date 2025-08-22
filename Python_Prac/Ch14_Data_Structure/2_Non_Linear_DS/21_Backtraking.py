def permut(a, s):
    # Define a function called permut that takes two arguments: list (an integer) and s (a list of characters)
    if a == 1:
        # Base case: if the value of 'a' is 1, return the list 's'
        return s
    else:
        # Recursive case:
        return [
            y + x  # For each character 'y' in the result of permut(1, s)
            for y in permut(1, s)
            for x in permut(a - 1, s)  # For each character 'x' in the result of permut(list - 1, s)
        ]

# Example 1: permut(1, ["a", "b", "c"])
print(permut(1, ["a", "b", "c"]))
# Example 2: permut(2, ["a", "b", "c"])
print(permut(2, ["a", "b", "c"]))
