#Building another mini project named guessing word

secret_word = "tulip"
guess = " "
i =3
while i>=1 : #giving the user with only 3 chances 
    guess = input("Enter the guess: ")
    if (guess != secret_word):
        i-= 1
        print("you have " +str(i) +" more chances left!")
    else:
        i=0
        print("You win!")
     