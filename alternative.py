# Write a programme that reads in a string and makes each alternate character into an upper case character and each other alternate character a lower case one.
# Now, try starting with the same string but making each alternative word lower and upper case.
# Tip: use split() and join() functions will help you here.

# Original string.
original_str = "I am learning to apply the join and split functions."

# Empty list to store modified characters.
char_list = []

for i in range(len(original_str)):
    # If the index is even, convert the character to uppercase; otherwise, to lowercase
    if i % 2 == 0:
        char_list.append(original_str[i].upper())
    else:
        char_list.append(original_str[i].lower())

# I used characters to form the result string
result_alternate_case = ''.join(char_list)

# Print result
print("Alternate Case example (characters):", result_alternate_case)


# Original string
input_str = "I am learning to apply the join and split functions."

# I Split the original string into a list of words.
words = input_str.split()

# Created an empty list to store the modified words.
word_list = []

# Iterate through the words now considered indexes. 
for i in range(len(words)):
    # If the index is even, convert the word to lowercase; otherwise, to uppercase.
    if i % 2 == 0:
        word_list.append(words[i].lower())
    else:
        word_list.append(words[i].upper())

# Join the modified words to form the result string.
new_alternate_word_case = ' '.join(word_list)

# Print the result
print("Alternate Case Example (words):", new_alternate_word_case)