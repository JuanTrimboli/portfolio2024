"""Given certain variables, it is asked to convert them into new ones.
The variables given are num1 = 99.23 to an integer, num2 = 23 into a float, num3 = 150 into a string and string1 = 100 into a integer and print them.
In order to do this, we can give the print command and simply include the new format to change them. Can also transform them first, replacing the format and then giving the print command."""
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

print(int(num1))
print(float(num2))
print(str(num3))
print(int(string1))

"""The other version would be 
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100" 

Then replace the format:

num1 = int(num1)
num2 = float(num2)
num3 = str(num3)
string1 = int(string1)

And after replacing the format just print
print(num1)
print(num2)
print(num3)
print(string1)"""