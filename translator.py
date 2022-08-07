#Creating a translator

#rules of our translator:
#all the vowels -> oo

def translate():
    translation = " "
    phrase = input("Enter you phrase: ")
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "OO"
            else:
                translation = translation + "oo"
        else:
            translation = translation + letter
    return translation

print(translate())
