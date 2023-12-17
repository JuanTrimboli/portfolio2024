#We're being asked to replace the "!" character in a sentence given.
#For this I'll use the replace method under a new variable. 
#After this, need to use the upper one, to be able to print in capital letters.
#Finally, use the slice method to print the phrase, but now inverted.

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
sentence_rep = sentence.replace("!" , " ") #The .replace will change the "!" for a space as indicated.
print(sentence_rep) #Now a sentence with spaces between words will be printed

sentence_cap = sentence_rep.upper() #sentence will be fully displayed in capital letters
print(sentence_cap)

sentence_inv = (sentence_cap[: : -1]) #This method will take the whole phrase and invert it due to the -1 at the end.
print(sentence_inv)

sentence_inv_2 = sentence_rep[: : -1] #Just in case I needed to invert the original sentence and not the upper case one.
print (sentence_inv_2)

#Note that you can also simplify this without storing the new types for the variable "sentence". i.e. stating print(sentence_cap[: : -1]) would have worked too.