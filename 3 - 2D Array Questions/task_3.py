def initArray(rows: int, cols: int) -> list:
    # Declares and initialises a 2D array with given rows and columns
    newArray = [[None] * rows for x in range(cols)]
    return newArray
    


def readFile(filename):
    print(f"Reading file: {filename}")
    names = []
    scores = []
    with open(filename, 'r') as file:
        line = file.readline().rstrip('\n')
        while line:
            items = line.split(',')
            names.append(items.pop(0))
            scores.append(list(int(items[x]) for x in range(len(items))))
            line = file.readline().rstrip('\n')
    return [names, scores] 

def printPercentages(data: list):
    print("Student Percentages:")
    for x in range(1,len(data[0])):
        total = 0
        toPrint = f"{data[0][x]}: "
        for y in range(0,len(data[1][x])):
            total += round(data[1][x][y]/data[1][0][y]*100)
            toPrint += f"{data[1][x][y]/data[1][0][y]*100:.0f}% "
        spaces = ""
        nameLengths = []
        for i in range(0,len(data[0])): nameLengths.append(len(data[0][i]))
        for _ in range(len(toPrint),(max(nameLengths)+2+(4*len(data[1][0])))): spaces = spaces + " "
        toPrint += f"{spaces}Average = {round(total/len(data[1][0]))}%"
        print(toPrint)

data = initArray(rows=6, cols=2)
data = readFile('testscores.csv')

printPercentages(data)
