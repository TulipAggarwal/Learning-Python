#2D lists in python

#creating 2D list which is basically multiple lists in a list
#creating a grid with 4 rows and 3 columns
number_grid = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9],
    [0]
]
print(number_grid[1][2]) #printing row 1 column 2 i.e, 6 (as the index start from zero)

# Nested for loops and 2D lists together
for row in number_grid:
    for col in row: #Reaching out to each and every elemenet in each and every row
        print(col)
