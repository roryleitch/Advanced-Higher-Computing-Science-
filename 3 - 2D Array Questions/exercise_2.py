from exercise_1 import initArray, print2dArray

def populateArray(array: list, fileName: str):
    rowcounter = 0
    colcounter = 0
    with open(fileName, 'r') as file:
        line = file.readline().rstrip('\n')
        while line:
            items = line.split(',')
            print(f"Items: {items}")
            colcounter = 0
            for item in items:
                array[rowcounter][colcounter] = int(items[colcounter])
                colcounter += 1
            rowcounter += 1
            line = file.readline().rstrip('\n')
    return array

def yearly(array: list):
    total = 0
    for x in range(len(array)):
        for y in range(len(array[x])):
            total += array[x][y]
    return total

def smallestEachWeek(array: list):
    min = 0
    for x in range(len(array)):
        min = array[x][0]
        for y in range(len(array[x])):
            if array[x][y] < min:
                min = array[x][y]
        print(f"Smallest for week {x+1}: {min}")
        
def largestEachWeek(array: list):
    max = 0
    for x in range(len(array)):
        max = array[x][0]
        for y in range(len(array[x])):
            if array[x][y] > max:
                max = array[x][y]
        print(f"Largest for week {x+1}: {max}")

print("Populating array from file...")
rainfall = initArray(52,7)
rainfall = populateArray(rainfall, 'rainfall.csv')
total = yearly(rainfall)
print(f"Total rainfall for the year: {total}")
smallestEachWeek(rainfall)
largestEachWeek(rainfall)