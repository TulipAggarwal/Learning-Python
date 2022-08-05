#Functions used in lists in python

#creating two lists
num = [1,2,3,4,5,6,7,8]
name= ["a", "b", "c", "d"]
print (num)
print (name)

name.extend(num) #adds the list num to list name
print(name)
name.append("e") #adds another element 'e' to the end of the already existing list
print(name)
name.insert(2, "e") #adds the element 'e' at an index 2 and pushes the other elements right
print(name)
name.remove("a") #removes element 'a' from the list
print(name)
#name.clear() #Removes all the element from the list
#print(name)
name.pop() #removes the last element
print(name)
print(name.index("d")) #prints the index of 'd' element in the list
print(name.count("a")) #counts the number of iteration a is in the list
name.sort() #sorts the elements in ascending order

num.sort() #sorts the elements in ascending order
print(num)
num.reverse() #reverses the list
print(num)
num2 = num.copy() #num2 will copy all the elements of num
print(num2)