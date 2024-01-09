# Approached by a small financial company, they asked for a program that allows the user to access two different calculations: investment calculations and a home loan repayment one.
# The code should be able to: the user should be allowed to choose which calculation they want to do.
# All variables -named bond and investment- should be valid regardless of how the user capitalizes their selection: bond, Bond or BOND, for instance.

"""# For interest, when selected, we need to ask the user: 
# Amount of money to deposit
# Interest rate (number only)
# Number of years for the investment
# Interest type: either compound or simple.
# ...
# Simple interest formula---> total amount = initial deposit x (1 + interest rate x number of years of investment)
# Compound interest formula---> total amount = initial deposit x (1 + interest rate) ^ (number of years of investment)"""


"""# For home loan repayment, when selected, ask the user:
# The present value of the property
# Interest rate (annual)
# Number of months the user wants for loan repayment.
# ...
# Loan repayment formula---> repayment = (monthly interest x property value)/(1 - (1 + monthly interest))^(-number of months for repayment)"""

import math

#Options for the user to type in.

inv_calc = ["investment" , "Investment" , "INVESTMENT"] 

bond_calc = ["bond" , "Bond" , "BOND"]

#Ask user for input

user_choice = (input("Please type in the calculation you want to execute (bond/investment): "))

#Indented blocks depending on user's input

if user_choice in inv_calc:                                                                     #If that input is within the inv_calc options:
    print("You have selected the investment calculator\nLet's proceed.")
    principal_amount = float(input("What is the amount you'd like to deposit? (numbers only)"))     
    print(f"Your principal amount is: {principal_amount}")
    interest_rate = float(input("What's your annual interest rate (type numbers only)?"))          
    print(f"Your annual interest rate is: {interest_rate}%")
    years_of_investment = int(input("How many years will your investment plan last for (numbers only)?"))       
    print(f"Your investment plan will last for {years_of_investment} years")
    interest = input("What type of investment plan are you interested in? Simple or compound?")
    print(f"The interest plan selected is: {interest}")
    P = principal_amount                                                                        #Conversion of variables to the letters suggested for the exercise
    r = (interest_rate / 100)                                                                   #Conversion to accurately calculate interest rate.
    t = years_of_investment
    if P > 0 and r > 0 and t > 0:
        if interest in ["simple", "Simple", "SIMPLE"]:                                          #Calculations based on Simple interest formula. 
            A = P*(1+r*t)
            rounded_A = round(A, 2)                                                             #Round function to make it tidier.
            print(f"Your total amount by the end of your investment plan will be: {rounded_A}")
        elif interest == "compound" or interest == "Compound" or interest == "COMPOUND":        #Elif statement, when user chooses compound interest, instead of simple.
            A = P*math.pow((1+r), t)
            rounded_A = round(A, 2)
            print(f"The total amount at the end of your investment plan will be {rounded_A}")
    else:                                                                                       #If none of the inputs match, an error sign will show.
        print("Sorry, the values entered are incorrect. Try again.")
elif user_choice in bond_calc:                                                                  #Elif statement for the loan repayment calculations.
    print("You have selected the loan repayment calculator\nLet's move forward.")
    property_value = float(input("What is the value of the property (numbers only)?"))
    print(f"The value of the property is: {property_value}")
    loan_interest_rate = float(input("What is the annual interest rate for this loan (numbers only)?"))
    print(f"Loan interest is: {loan_interest_rate}%")
    months_for_repayment = int(input("Please type in the length in months for this loan repayment (numbers only)"))
    print(f"It will take you {months_for_repayment} months to fully repay your loan.")
    P = property_value
    i = (loan_interest_rate / 100)/12                                                           #New variable to calculate monthly interest.
    n = months_for_repayment
    if P > 0 and i > 0 and n > 0:                                                               #Of course, values should be higher than 0 in order to make this work.
        repayment = (i*P)/(1-(1+i)**(-n))
        rounded_repayment = round(repayment, 2) 
        print(f"Your monthly loan payment will be: {rounded_repayment}")
    else:
        print("Sorry, one or more values entered might be incorrect. Try again!")               #Statement in case any of the values are incorrect.
else:
    print("Sorry, there must be a mistake. Please try again.")                                  #If user's choice isn't between investment or bond, this message will pop up.
