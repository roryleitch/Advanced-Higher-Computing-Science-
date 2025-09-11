CardData = [11,12,25,33,52,56,57,59,85,91]
item = int(input("Enter the number you're searching for: "))
found = False
startPos = 0
endPos = len(CardData) - 1

while found == False and startPos <= endPos:
    middle = (startPos+endPos)//2
    if CardData[middle] == item:
        found = True
    elif CardData[middle] < item:
        startPos = middle + 1
    else:
        endPos = middle - 1
if found == True:
    print(item,"found at position", middle)
else:
    print(item,"not in array.")