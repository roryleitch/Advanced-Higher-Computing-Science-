ProductCodes = [210,225,240,255,300,315,330,345,360]   
ProductNames = ["Pen","Pencil","Eraser","Sharpener","Notebook","Folder","Stapler","Marker","Ruler"]

item = 400
found = False
startPos = 0
endPos = len(ProductCodes) - 1

while found == False and startPos <= endPos:
    middle = (startPos+endPos)//2
    if ProductCodes[middle] == item:
        found = True
    elif ProductCodes[middle] < item:
        startPos = middle + 1
    else:
        endPos = middle - 1

if found == True:
    print(f"The name of the product with number {item}, is {ProductNames[middle]}")
else:
    print(f"That product number does not exist.")
    