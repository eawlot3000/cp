#!/usr/bin/env python3

# Let's write a Python program to solve the given problem.

# The approach is to define strings for each unique word that appears in the numbers from 1 to 1000,
# then calculate the number of times each word is used when writing out all the numbers from 1 to 1000.
# Note that this solution adheres to British usage as per the problem statement.

# Create lists to hold the lengths of the number words
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ones_lengths = [len(word) for word in ones]

teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
         "seventeen", "eighteen", "nineteen"]
teens_lengths = [len(word) for word in teens]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
tens_lengths = [len(word) for word in tens]

# "hundred" and "thousand" and "and"
hundred_length = len("hundred")
thousand_length = len("thousand")
and_length = len("and")

# Function to calculate the total length of words for 1-99
def calculate_1_to_99():
    total = 0
    # Sum lengths of one to nine
    total += sum(ones_lengths)
    # Sum lengths of ten to nineteen
    total += sum(teens_lengths)
    # Sum lengths of twenty, thirty, ..., ninety-nine
    for tens_length in tens_lengths[2:]:  # Start from 'twenty'
        total += tens_length * 10  # The tens word appears 10 times per hundred
        total += sum(ones_lengths)  # One to nine follows each tens word
    return total

# Function to calculate the total length of words for 1-1000
def calculate_total():
    total = 0
    total_1_to_99 = calculate_1_to_99()

    # Sum lengths for 1-99, appears 10 times in total (1-99, 101-199, ..., 901-999)
    total += total_1_to_99 * 10

    # Sum lengths for each hundred (one hundred, two hundred, ..., nine hundred)
    # Each appears 100 times, plus the word "hundred", plus "and" for 1-99
    for ones_length in ones_lengths[1:]:
        total += ones_length * 100  # The word "one", "two", etc., appears 100 times
        total += hundred_length * 100  # The word "hundred" appears 100 times
        total += and_length * 99  # The word "and" appears for 1-99 after each hundred

    # Add one thousand
    total += ones_lengths[1] + thousand_length

    return total

# Calculate and print the total length
total_length = calculate_total()
print(total_length)
