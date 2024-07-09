
file_path = 'og.txt'

# Function to calculate the alphabetical value of a name
def alphabetical_value(name):
    return sum(ord(char) - ord('A') + 1 for char in name)

# Reading the file and storing the names in a list
with open(file_path, 'r') as file:
    names_string = file.read().strip().replace('"', '')
    names_list = names_string.split(",")

# Sorting the list alphabetically
names_list.sort()

# Calculate the name score for each name and sum them up
total_score = sum(alphabetical_value(name) * (i+1) for i, name in enumerate(names_list))

# Save the sorted names into a new file named 'cc.py'
with open('cc.py', 'w') as cc_file:
    cc_file.write('sorted_names_list = ' + str(names_list))

total_score
