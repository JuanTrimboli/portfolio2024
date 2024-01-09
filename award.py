#Design a program that determines the award the athlete will receive depending on their time.
#This program should read in the times in minutes for each event: swimming, cycling and running.
#Then, it should calculate and display the total time taken to complete the triathlon.
#The award will be based on the total time taken. Qualifying time (max) is 100 minutes.
#Display the award receive according based on the following criteria:
#(0-100) - Provincial colours / (101-105) - Provincial Half Colours / (106-110) - Provincial Scroll / (Over 110) - No award.

name = input("Enter athelete's name: ")
print("Athlete's name: " + name)
print(f"Hello {name}! The award you get will be determined by the total time taken to complete our three events.")

swimming = float(input("Please, enter athlete's time (in minutes) for the swimming event: "))
cycling = float(input("How long did the athlete take to complete the cycling event (in minutes)?: "))
running = float(input("Please, specify athlete's final time for the running event (in minutes): "))

if swimming <= 0 or running <= 0 or cycling <= 0: #Added this condition, as they all have to be positive numbers. Zero would mean, no participation and negative numbers aren't an option. 
    print("Apologies, you either haven't participated or the input typed in is incorrect.")
else:
    total = swimming + cycling + running
    print (f"Athlete's total time is: {total}")

    if total <= 100 and total > 0: #Input for the first award under 100.
        print("Congratulations! You are within our qualification time!\nYou've earned the 'Provincial Colours' award!")
    elif total > 100 and total < 105: #Input for the second category, above 100.
        print ("Well done! Although you haven't qualified, you were very close!\nYou've earned our 'Provincial Half Colours'.\nKeep up the good work!")
    elif total > 105 and total < 110: #Input for the third category, above 105.
        print("Good effort! You were less than 10 minutes away from our qualifying time!\nYou take home a 'Provincial Scroll' with you!")
    else: #Above 110, therefore, no award.
        print("It was great to have you this time and we look forward to seeing you again at the next race.\nUnfortunately, your time isn't good enough to get an award. Better luck next time!")