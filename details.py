#Need to get specific information about the user. There are four variables for the user to type in and then show it in a single sentence.
#These variables are Name, Age, House Number and Street Name, all with a string format. -House number won't be an int format, in case there's a letter included (i.e 14A)-
#To create a single phrase we can use concatenation, but a f(string) would work better.
#Ask for input and then print with an f string. 
name = input("Please enter your full name: ")
age = int(input("How old are you?: "))
house_number = (input("Please type your house number in:"))
street_name = input("And your street name, please: ")
print(f"My name is {name}. I'm {age} years old. And I live in no. {house_number} on {street_name} ")