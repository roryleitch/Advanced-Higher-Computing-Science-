import random

#global variables
rows = 4
cols = 5

def initArray(rows: int,cols: int): 
    # Declares and initialises a 4 by 5 2D array
    newArray = [[None]*cols for i in range(rows)]
    return newArray

def populateArray(array: list):
    for x in range(len(array)):
        for y in range(len(array[x])):
            array[x][y] = random.randint(1,20)
    return array

def print2dArray(array: list):
    row = ""
    for x in range(len(array)):
        for y in range(len(array[x])):
            row += str(array[x][y]) + ", "
            
        row = row[:-2]
        print(row)
        row = ""

tickets = initArray(4,5)
tickets = populateArray(tickets)
print2dArray(tickets)
        
