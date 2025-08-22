h_count={}
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

for line in handle:
    if line.startswith("From"):    
        words=line.split()
        if len(words)>=6:
            time=words[5].split(':')
            h=time[0]            
            h_count[h]=h_count.get(h,0)+1

            
sorted_h_count=sorted(h_count.items())
for k,v in sorted_h_count:
    print(k,v)


# Initialize an empty dictionary to store hour counts.
hour_counts = dict()

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
        words = line.split()

        # Check if there are enough elements in the 'words' list.
        if len(words) >= 6:
            # Extract the time from the line (assuming it is in the format HH:MM:SS).
            time = words[5].split(':')

            # Check if there are enough elements in the 'time' list.
            if len(time) >= 1:
                # Extract the hour from the time.
                hour = time[0]

                # Increment the count for the corresponding hour.
                hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Close the file.
handle.close()

# Sort the hour counts by hour and print the results.
sorted_hour_counts = sorted(hour_counts.items())

for hour, count in sorted_hour_counts:
    print(f"Hour: {hour}, Count: {count}")

        