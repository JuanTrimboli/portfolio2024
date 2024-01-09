# Program with a logic error in a while loop
# It is meant to be a program that can count up to 5.
# In this case, the break will actually stop the program from printing more numbers. Plus, it won't get to 5. Moreover, the if statement is redundant as it won't go any further than 4.

counter = 1
while counter < 5:
    print(f"I can only count up to 5.\n Here's the next number: {counter}")
    counter += 1
    break
if counter > 6:
    print("That's out of my knowledge")