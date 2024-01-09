# Write a code to output the star pattern show (*,**,***,****,*****,****,***,**,*) using and if-else statement in combination with a single for loop

# Range will increase by 1 up to 5 included.
# Then when we reach 5, I needed to find a way to make it decrease by 1 each time as it moves up until one star is left, therefore the best way is to use 10 and subtract. 
for i in range(1, 10):
    if i <= 5:
        print("*" * i)
    else:
        print("*" * (10-i))