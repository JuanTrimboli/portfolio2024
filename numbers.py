#According to the exercise, we have to ask the user to type in three integers and then do some operations with them
#These operations are: the sum of all numbers; first number minus second number; third number times first number; and the sum of all them divided by the third number.

num1 = int(input("Please enter a number: ")) #asking for a first number
num2 = int(input ("Enter a second number: ")) #asking for a second number
num3 = int(input ("And now type in a third one, please: ")) #asking for a third number to work with

print("The sum between the three of them is: {}".format(num1+num2+num3)) #applying format as I included a string whilst I have to calculate a new numbers with integers
print("The first number minus the secon number is {}".format(num1-num2)) #Keep printing the requested operations.
print(f"The third number multiplied by the first number is {num3*num1}") #Can also use f strings
print(f"The sum of all numbers divided by the third number is {(num1+num2+num3)/num3}")
#Note that parenthesis is needed in the last one as otherwise, operations will be executed in a different order (as + and - divide terms).10