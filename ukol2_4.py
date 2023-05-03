import os
from collections import Counter

# Get the current working directory
cwd = os.getcwd()

# Specify the full path to the file
file_path = 'C:/Python/UKOL1/filename.txt'

with open(file_path, 'rb') as file:
    contents = file.read()

with open(file_path, 'r', encoding='utf-8') as file:
    # Split the contents of the file into words
    words = file.read().split()

    # Create an empty list to store numbers found in the file
    numbers = []

    # Loop through each word in the file
    for word in words:
        # Try to convert the word to a float
        try:
            num = float(word)
            # If successful, append the number to the list
            numbers.append(num)
        except ValueError:
            # If the conversion fails, ignore the word
            pass

    # Calculate the sum of the numbers found in the file
    sum_numbers = sum(numbers)

    # Convert the sum to an integer
    sum_int = int(sum_numbers)

    # Print the sum of the numbers found in the file without decimals
    print(f"The sum of the numbers found in the file is: {sum_int}")

    # Create a Counter object from the list of words
    word_counts = Counter(words)

    # Initialize the longest word and its length
    longest_word = ""
    longest_length = 0

    # Loop through each word in the file
    for word in words:
        # Get the length of the current word
        length = len(word)

        # If the current word is longer than the longest word found so far,
        # update the longest word and its length
        if length > longest_length:
            longest_word = word
            longest_length = length

    # Print the longest word found
    print(f"The longest word in the file is '{longest_word}' (length: {longest_length})")

    # Create a Counter object from the list of words
    word_counts = Counter(words)

    # Get the most common word and its count
    most_common_word, count = word_counts.most_common(1)[0]

    # Print the result
    print(f"The most frequent word in the file is '{most_common_word}' (occurs {count} times)")
