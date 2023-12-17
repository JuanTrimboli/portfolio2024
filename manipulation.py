#Ask the user to input a sentence called str_manip.
#step one: calculate and display the length of the sentence.
#step two: find the last letter of the sentence and replace it with the character "@".
#step three: print the last three characters of that phrase.
#step four: create a 5 character phrase with the three first and the last two characters of the phrase.

str_manip = input("Please enter a sentence fo us to work with: ")

print(len(str_manip))

char1 = str_manip[-1] #char1 represents the last character of the sentence. This wouldn't work well if the user finishes the sentence with a character that isn't a letter. 
#Could a loop be created to remove the characters until char1 is a letter?

str_manip_2 = str_manip.replace(char1 , "@") #New variable created as the original sentence will need to be used on the following steps, replacing the last character for "@". 
#Since last character is equal to char 1, it should replaced that character if it's included in any other word. 

print(str_manip_2) #sentence should print with with "@"

last_three_char = str_manip[-3 : ] #Last three characters selected in a new variable to print.
last_three_inv= last_three_char[: : -1] #-1 inverts it
print(last_three_inv) 

characters_new_word = str_manip.replace(" " ,"")
first_three_char = characters_new_word [ : 3]
last_two_char = characters_new_word [-2 : ]
new_word = first_three_char + last_two_char
print(new_word)
