BookIDs = [101,112,135,142,150,166,172,188]
BookTitles = ["Hamlet","Macbeth","Othello","Twelfth Night","King Lear","The Tempest","Romeo & Juliet","Much Ado"]
book = 14

found = False
startPos = 0
endPos = len(BookIDs) - 1

while found == False and startPos <= endPos:
    middle = (startPos+endPos)//2
    if BookIDs[middle] == book:
        found = True
    elif BookIDs[middle] < book:
        startPos = middle + 1
    else:
        endPos = middle - 1

if found == True:
    print(f"The title of the book with the ID {book}, is {BookTitles[middle]}")
else:
    print(f"That book ID does not exist.")