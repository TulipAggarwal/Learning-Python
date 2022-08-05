#Lerning about lists

friends = ["ABC", "DEF", "GHI", "JKL", "MNO"] #Creating a list named friends
print(friends) #Prints the entire list
print (friends[3]) #Prints the element in the list which is at index 3
print(friends[-1]) #Prints the last element of the list
print(friends[1:3]) #Print elements from 1-2 including both
print(friends[2:]) #Prints all the elements from 1 to the end of the list
friends[1] = "ASD" #Modifies the first value as ASD 
print(friends)