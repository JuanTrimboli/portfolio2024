#The program created will output a variety of responses determined by the user's entry.
#If the user is 40 or older, output 'You're over the hill'.
#age is the name for the variable to take in user's input.
#It's up to a 100, otherwise you print out "Sorry, you're dead."
#If older than 65, print "Enjoy your retirement!"
#If user is under 13, output "You qualify for the kiddie discount"
#If user is 21, output "Congrats on your 21st"
#Any other age, output "Age is just a number"

age = int(input("Type your age in: "))

if age > 100:
    print("Sorry, you're dead.")
elif age > 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 0:
    print("I'm sorry, but you don't actually exist yet.")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is just a number.")

#I structured the ages in order as there could be an overlap depending on the value of that age. 
# For instance, if user inputs a number "a" that is greater than 40 but also greater than 65, and the if statement 40 is first, and the 65 second, both statements would be correct.
# If is say, "if age is greater than 40, print "x", otherwise, if age us greater than 65, print "y", and the user inputs 68, the first option would be valid and it'd print "x".
#However, the code, should print "y" as it's greater than 65. So, you need to arrange the ages in sort of segments. So:
# a) over a hundred. b)66-100 c)40-65 d)21 e)13 or lower.
#I also included a variable that if it's lower than 0, it should print that the user does not exist yet. When we are talking about smaller, the segments go the other way round.
#For instance if the used typed -1, this would be minor than 13 and 0, however, if the Elif age<13 was first, the program would print "You qualify..."
#whereas if the age<0 comes first, all the negative numbers will display "I'm sorry, you don't actually exist", and when that is false (0 or greater) it'll print "You qualify..."