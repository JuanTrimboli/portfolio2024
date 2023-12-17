#Take user's favourite restaurant (string_fav) and favourite number (int_fav).
#Print both out in separate statements.
#Once it's working try to cast sting_fav to an int. Add a comment explaining what happens.

string_fav = input("Please, type in the name of your favourite restaurant: ")
int_fav = int(input("Now, we'd like to know what your favourite number is: "))

print(f"Your favourite restaurant is: {string_fav}")
print(f"Your favourite number is: {int_fav}")

string_fav = int(string_fav) #When you try to cast a string (that saves information of all kind) to an integer, that only stores numbers with no decimals, it shows a Value error.
#The reason being is that basically, you are trying to save words into a format that does not allow anything but entire numbers, either positive or negative.
#So, as it contains characters that aren't valid, an error will be raised in the code. You can save numbers as strings, but not words as integers or float.