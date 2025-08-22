
# Initialize an empty dictionary to store word counts.
counts = dict()
# Create an empty list to store words extracted from lines.
words = []
# Initialize variables to keep track of the most frequent word and its count.
bigcount = None
bigword = None
# Initialize a counter to keep track of the total number of words.
count = 0

# Prompt the user for a file name; if none is provided, use the default "mbox-short.txt".
name = input("Enter file name: ")
if len(name) < 1:
    name = "mbox-short.txt"

# Open the specified file.
handle = open(name)

# Iterate through each line in the file.
for line in handle:
    # Check if the line starts with "From ".
    if line.startswith("From "):
        # Split the line into words.
        word = line.split()

        # Check if there is at least one word.
        if len(word) > 1:
            # Append the second word (email address) to the list.
            words.append(word[1])

            # Increment the word count and print it.
            count += 1
            print(count)

# Iterate through the list of words to count their occurrences.
for word in words:
    counts[word] = counts.get(word, 0) + 1

# Find the most frequent word (email address) and its count.
for word, count in counts.items():
    # Check if the current count is larger than the previous maximum.
    if bigcount is None or count > bigcount:
        # Update the most frequent word and its count.
        bigword = word
        bigcount = count

# Print the most frequent word (email address) and its count.
print("Most frequent email address:", bigword)
print("Count:", bigcount)
