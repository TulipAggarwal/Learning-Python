#for loops in python

for letter in "Tulip Aggarwal": #for loop with strings
    print(letter)
friends = ["a", "b", "c", "d"]

for friend in friends: #for loop with array
    print(friend) 

for index in range(10): #for loop with numbers
    print(index) #will print all values from 0-9 and not 10

for index in range(3,10):
    print(index) #Will print all numbers from 3-9

for index in range(len(friends)): #will execute the loop for number of times as that of the elements in the array friends
    print(friends[index]) 

for index in range(5): #giving conditions in the for loops
    if index ==0:
        print("First Iteration")
    else:
        print("Not the first iteration")