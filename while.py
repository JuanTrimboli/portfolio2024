#Write a program that continually asks the user to enter a number.
#When the user enters "-1", the program should stop requesting numbers and then calculate the average of the ones entered (excluding the -1).
#Use a while loop statement.

total = 0                                                                           # Starting point is zero; if there's no numbers entered, input is 0.
num_of_inputs = 0                                                                   

user_num = int(input("Please enter a number (type in -1 to stop):"))                

while user_num != -1:                                                               # While loop, if the number isn't -1 (already excluding -1), then:
    
    total += user_num                                                               # Total would be the addition of all the numbers entered.
    num_of_inputs += 1                                                              # Inputs will increase by one determined by the amount of entries the user executes.    
    user_num = int(input("Please enter a number (type in -1 to stop):"))
    
if user_num == -1 and num_of_inputs > 0:                                            # When the input equals -1 and there are more inputs than zero then:
    print(f"The sum between all the inputs is: {total}")                            # The program will print total and number of inputs. And then calculate average with new variable.
    print(f"The amount of inputs was: {num_of_inputs}") 
    average = total/num_of_inputs                                                   
    rounded_avg = round(average, 2)
    print(f"The average between the numbers you typed in is: {rounded_avg}")        
else:
    print("Sorry, there weren't enough inputs provided to run this program.")        
