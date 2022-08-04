#Working with strings

phrase= "Hello I am Tulip"
print(phrase.lower()) #converting the phrase to lowercase
print(phrase.upper()) #converts the phrase to uppercase
print(phrase.islower()) #checks if the phrase is in lowercase
print(phrase.isupper()) #checks if the phrase is in uppercase
print(phrase.upper().isupper()) #conveting the phrase in uppercase and then checking if it is uppercase or not
print(len(phrase)) #checking the length of the phrase
print(phrase[0]) #prints the 0th index of the string
print(phrase[-1]) #prints the last index of the string
print(phrase.index("I")) #prints the index of "I" in the above string
#print(phrase.index("y")) #gives an error because y is not in the above string
print(phrase.replace("Tulip", "Tara")) #prints the phrase by replacing Tulip with Tara
print(phrase.capitalize()) #prints the phrase by capitalizing the first letter of the string