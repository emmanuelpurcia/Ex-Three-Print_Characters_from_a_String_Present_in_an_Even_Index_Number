# Hello! This program prints the characters of a string that are present at an even index number.

# Accept input string from a user
word = input('Hello User! Please enter a word: ')
print("Original String Given:", word)

# Iterate over each character of the string at even indices
print("Okay, Printing only even index characters. Here we go:")
for i in range(0, len(word), 2):
    print(f"Index[{i}]: {word[i]}")
    