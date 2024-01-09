# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")
print ("\n")                                                                                    #Syntax error. Wrong indentation; no parentheses and the \n command goes at the end of a sentence when the next thing printed is better in a new line. Otherwise it's ("\\n")

# Variables declaring the user's age, casting the str to an int, and printing the result        #Wrong indentation whole block.
age_Str = "24"                                                                       
age = int(age_Str)                                                                              #Runtime error, age_Str not defined and won't be converted to int as it isn't just a number. I'd suggest variable's name to be in lower case
print(f"I'm {age} years old.")                                                                  #Runtime error, need to use format or fstring as concatenation is only with strings.

# Variables declaring additional years and printing the total years of age
years_from_now = "3"                                                                            #Runtime error, string should be converted to an integer so it can be used to arithmetical operations.
years_from_now = int(years_from_now)
total_years = age + years_from_now                                                              

print(f"The total number of years: {total_years}")                                               #Logical error and syntax error; no parentheses; since the answer_years variable hasn't been declared, the message printed will be "answer_years" literally, and the variable shouldn't be "".
                                                                                                 #Fstring as well.
# Variable to calculate the total amount of months from the total amount of years and printing the result
extra_months = 6                                                                                 #New variable to add the extra amount of months that want to be calculated.
total_months = (total_years * 12) + extra_months                                                 #Logical error; you should convert this to float if you want to work with half years, plus full years * months won't reflect the actual age in months.
print (f"In 3 years and 6 months, I'll be {total_months} months old")                            #Also, there's an operation missing if the person wants to calculate. I'll consider full years for this to work with as 330 is the correct answer, though.
                                                                                                 #Syntax error, no parentheses and concatenation of strings and int.
#HINT, 330 months is the correct answer

