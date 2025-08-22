count = 0

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

try:
    with open(fname, 'r') as file:
        for line in file:
            if line.startswith('From '):
                words = line.split()
                if len(words) > 1:
                    print(words[1])
                    count += 1

except FileNotFoundError:
    print("File not found:", fname)

print("There were", count, "lines in the file with From as the first word")
